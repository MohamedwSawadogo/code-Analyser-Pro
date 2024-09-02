import pandas as pd
from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QListWidget, QPushButton, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DynamicDataHandler:
    def __init__(self):
        self.data = None

    def load_data(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Fichiers CSV (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                self.data = pd.read_csv(file_path)
                if self.validate_data(self.data):
                    QMessageBox.information(None, "Succès", "Données chargées avec succès !")
                else:
                    QMessageBox.warning(None, "Erreur", "Données invalides ou manquantes.")
            except Exception as e:
                QMessageBox.warning(None, "Erreur", f"Erreur lors du chargement des données : {str(e)}")

    def validate_data(self, data):
        return not data.empty and 'Temps' in data.columns

class DynamicReferenceHandler:
    def __init__(self):
        self.references = {
            'Accélération': {'min': -5, 'max': 5, 'unit': 'm/s²'},
            'Vitesse': {'min': 0, 'max': 200, 'unit': 'km/h'},
            'Temps Accé': {'min': 2, 'max': 10, 'unit': 's'},
            'Freinage': {'min': 0, 'max': 3, 'unit': 'm/s²'},
            'Vibration': {'min': 0, 'max': 2, 'unit': 'm/s²'}
        }

    def get_reference(self, parameter):
        return self.references.get(parameter, None)

class DynamicAnalysis:
    def __init__(self, data, input_column, output_columns, reference_handler):
        self.data = data
        self.input_column = input_column
        self.output_columns = output_columns
        self.reference_handler = reference_handler
        self.units = {
            'Temps': 's'
        }

    def analyze(self):
        results = {}
        anomalies = []
        for column in self.output_columns:
            reference = self.reference_handler.get_reference(column)
            if reference:
                min_val = reference['min']
                max_val = reference['max']
                range_val = max_val - min_val
                deviations = (self.data[column] - (min_val + max_val) / 2) / ((min_val + max_val) / 2) * 100
                within_bounds = (self.data[column] >= min_val) & (self.data[column] <= max_val)
                results[column] = {
                    'mean': self.data[column].mean(),
                    'std': self.data[column].std(),
                    'min': min_val,
                    'max': max_val,
                    'unit': reference['unit'],
                    'within_bounds': within_bounds,
                    'deviations': deviations
                }
                for idx, value in self.data[[self.input_column, column]].iterrows():
                    ecart_percent, comment, correction = self.generate_comment_and_correction(column, value[column], min_val, max_val, range_val)
                    if value[column] < min_val or value[column] > max_val:
                        anomalies.append({
                            'Temps': f"{value[self.input_column]:.2f} {self.units.get('Temps', 's')}",
                            'Paramètre': column,
                            'Valeur': f"{value[column]:.2f} {reference['unit']}",
                            'Écart (%)': f"{abs(ecart_percent):.2f}",
                            'Commentaire': comment,
                            'Correction': correction
                        })
        return results, anomalies

    def generate_comment_and_correction(self, parameter, value, min_val, max_val, range_val):
        if value < min_val:
            ecart = min_val - value
            ecart_percent = (ecart / range_val) * 100 if range_val != 0 else 0
            comment = f"La valeur de {parameter} ({value}) est en dessous de la limite minimale ({min_val}) par {ecart} ({abs(ecart_percent):.2f}%)."
            correction = self.get_correction(parameter, "low", ecart_percent)
        elif value > max_val:
            ecart = value - max_val
            ecart_percent = (ecart / range_val) * 100 if range_val != 0 else 0
            comment = f"La valeur de {parameter} ({value}) dépasse la limite maximale ({max_val}) par {ecart} ({abs(ecart_percent):.2f}%)."
            correction = self.get_correction(parameter, "high", ecart_percent)
        else:
            ecart_percent = 0
            comment = "La valeur est dans la plage acceptable."
            correction = ""

        return abs(ecart_percent), comment, correction

    def get_correction(self, parameter, condition, ecart_percent):
        corrections = {
            'Accélération': {
                'low': [
                    "Vérifiez le moteur et le système de transmission.",
                    "Assurez-vous que le véhicule n'est pas surchargé.",
                    "Inspectez les capteurs d'accélération."
                ],
                'high': [
                    "Vérifiez le contrôle de traction.",
                    "Assurez-vous que les pneus sont en bon état.",
                    "Inspectez les freins pour toute usure ou dysfonctionnement."
                ]
            },
            'Vitesse': {
                'low': [
                    "Vérifiez la qualité du carburant.",
                    "Assurez-vous que le moteur fonctionne à la température optimale.",
                    "Contrôlez les filtres à air et à carburant."
                ],
                'high': [
                    "Vérifiez les niveaux de liquide de refroidissement.",
                    "Assurez-vous que le système de refroidissement fonctionne correctement.",
                    "Contrôlez les capteurs de vitesse pour des lectures précises."
                ]
            },
            'Temps Accé': {
                'low': [
                    "Vérifiez le moteur et le système de transmission.",
                    "Assurez-vous que le véhicule n'est pas surchargé.",
                    "Inspectez les capteurs de temps."
                ],
                'high': [
                    "Vérifiez le contrôle de traction.",
                    "Assurez-vous que les pneus sont en bon état.",
                    "Inspectez les freins pour toute usure ou dysfonctionnement."
                ]
            },
            'Freinage': {
                'low': [
                    "Vérifiez le système de freinage pour des anomalies.",
                    "Assurez-vous que les plaquettes et les disques de frein sont en bon état.",
                    "Inspectez les capteurs de freinage."
                ],
                'high': [
                    "Vérifiez la puissance de freinage.",
                    "Assurez-vous que le système ABS fonctionne correctement.",
                    "Contrôlez l'état des pneus pour une bonne adhérence."
                ]
            },
            'Vibration': {
                'low': [
                    "Assurez-vous que le moteur fonctionne sans à-coups.",
                    "Vérifiez l'état des pneus et des amortisseurs.",
                    "Inspectez les capteurs de vibration."
                ],
                'high': [
                    "Vérifiez les composants du châssis pour des dommages.",
                    "Assurez-vous que le système de suspension fonctionne correctement.",
                    "Contrôlez l'équilibrage des roues."
                ]
            }
        }
        correction_messages = corrections.get(parameter, {}).get(condition, [])
        
        if ecart_percent > 50:
            return correction_messages[0]  # Correction majeure
        elif 20 < ecart_percent <= 50:
            return correction_messages[1]  # Correction modérée
        else:
            return correction_messages[2] if len(correction_messages) > 2 else ""  # Correction mineure

class DynamicDataVisualizer:
    def __init__(self, data, layout):
        self.data = data
        self.layout = layout
        self.units = {
            'Temps': 's',
            'Accélération': 'm/s²',
            'Vitesse': 'km/h',
            'Temps Accé': 's',
            'Freinage': 'm/s²',
            'Vibration': 'm/s²',
            'Distance': 'km'
        }

    def plot_with_reference(self, input_column, results):
        fig = Figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        y_labels = []

        for column, stats in results.items():
            ax.plot(self.data[input_column], self.data[column], label=f"{column} ({stats['unit']})")
            ax.axhline(stats['min'], color='green', linestyle='--', label=f'{column} Minimum')
            ax.axhline(stats['max'], color='red', linestyle='--', label=f'{column} Maximum')

            # Colorier les zones en dessous, entre et au-dessus des limites
            ax.fill_between(self.data[input_column], self.data[column], stats['min'], 
                            where=(self.data[column] < stats['min']), color='blue', alpha=0.5, interpolate=True)
            ax.fill_between(self.data[input_column], stats['min'], stats['max'], 
                            where=((self.data[column] >= stats['min']) & (self.data[column] <= stats['max'])), 
                            color='green', alpha=0.3, interpolate=True)
            ax.fill_between(self.data[input_column], self.data[column], stats['max'], 
                            where=(self.data[column] > stats['max']), color='red', alpha=0.5, interpolate=True)
            
            y_labels.append(f"{column} ({stats['unit']})")

        ax.set_title("Analyse des paramètres dynamiques", fontsize=12, fontweight='bold')
        ax.set_xlabel(f"{input_column} ({self.units.get(input_column, 's')})")
        ax.set_ylabel(", ".join(y_labels))
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()

        for i in reversed(range(self.layout.count())):
            widgetToRemove = self.layout.itemAt(i).widget()
            self.layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
        self.layout.addWidget(canvas)

        fig.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
        canvas.draw()

class DynamicInputSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sélectionnez la donnée d'entrée")
        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("""
            QListWidget::item:hover { background-color: #444444; }
            QListWidget::item:selected { background-color: #2C3E50; color: white; }
        """)
        self.layout.addWidget(self.list_widget)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

    def set_column_names(self, column_names):
        self.list_widget.addItems(column_names)

    def get_selected_column(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            return selected_item.text()
        return None

class DynamicOutputSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sélectionnez la/les donnée(s) de sortie")
        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.list_widget.setStyleSheet("""
            QListWidget::item:hover { background-color: #444444; }
            QListWidget::item:selected { background-color: #2C3E50; color: white; }
        """)
        self.layout.addWidget(self.list_widget)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

    def set_column_names(self, column_names):
        self.list_widget.addItems(column_names)

    def get_selected_columns(self):
        selected_items = [item.text() for item in self.list_widget.selectedItems()]
        return selected_items
