import pandas as pd
from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QListWidget, QPushButton, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class EmissionDataHandler:
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
                    self.data = self.rename_emission_columns(self.data)
                    QMessageBox.information(None, "Succès", "Données chargées avec succès !")
                else:
                    QMessageBox.warning(None, "Erreur", "Données invalides ou manquantes.")
            except Exception as e:
                QMessageBox.warning(None, "Erreur", f"Erreur lors du chargement des données : {str(e)}")

    def validate_data(self, data):
        return not data.empty and 'Temps' in data.columns

    def rename_emission_columns(self, data):
        rename_mapping = {
            'CO': 'CO_cum',
            'NOx': 'NOx_cum',
            'HC': 'HC_cum',
            'PM': 'PM_cum'
        }
        return data.rename(columns=rename_mapping)

class EmissionReferenceHandler:
    def __init__(self):
        self.references = {
            'CO_cum': (0, 1.0),
            'NOx_cum': (0, 0.06),
            'HC_cum': (0, 0.10),
            'PM_cum': (0, 0.005)
        }

    def get_reference(self, pollutant):
        if pollutant in self.references:
            return self.references[pollutant]
        return None, None

class EmissionAnalysis:
    def __init__(self, data, input_column, output_columns, reference_handler):
        self.data = data
        self.input_column = input_column
        self.output_columns = output_columns
        self.reference_handler = reference_handler
        self.units = {
            'Temps': 's',
            'Distance': 'km',
            'CO_cum': 'g/km',
            'NOx_cum': 'g/km',
            'HC_cum': 'g/km',
            'PM_cum': 'g/km'
        }

    def analyze(self):
        results = {}
        anomalies = []
        for column in self.output_columns:
            lower, upper = self.reference_handler.get_reference(column)
            if lower is not None and upper is not None:
                within_bounds = (self.data[column] >= lower) & (self.data[column] <= upper)
                results[column] = {
                    'mean': self.data[column].mean(),
                    'std': self.data[column].std(),
                    'min': self.data[column].min(),
                    'max': self.data[column].max(),
                    'within_bounds': within_bounds,
                    'lower': lower,
                    'upper': upper
                }
                for idx, value in self.data.loc[~within_bounds, [self.input_column, column]].iterrows():
                    ecart_percent, comment, correction = self.generate_comment_and_correction(column, value[column], lower, upper)
                    anomalies.append({
                        'Temps': f"{value[self.input_column]:.2f} {self.units.get('Temps', 's')}",
                        'Paramètre': column,
                        'Valeur': f"{value[column]:.2f} {self.units.get(column, '')}",
                        'Écart (%)': f"{ecart_percent:.2f}",
                        'Commentaire': comment,
                        'Correction': correction,
                    })
        return results, anomalies

    def generate_comment_and_correction(self, pollutant, value, lower, upper):
        if value < lower:
            ecart = lower - value
            ecart_percent = (ecart / lower) * 100 if lower != 0 else 0
            comment = f"La valeur de {pollutant} ({value}) est en dessous de la limite inférieure ({lower}) par {ecart} ({ecart_percent:.2f}%)."
            correction = self.get_correction(pollutant, "low", ecart_percent)
        elif value > upper:
            ecart = value - upper
            ecart_percent = (ecart / upper) * 100 if upper != 0 else 0
            comment = f"La valeur de {pollutant} ({value}) dépasse la limite supérieure ({upper}) par {ecart} ({ecart_percent:.2f}%)."
            correction = self.get_correction(pollutant, "high", ecart_percent)
        else:
            ecart_percent = 0
            comment = ""
            correction = ""
        return ecart_percent, comment, correction

    def get_correction(self, pollutant, condition, ecart_percent):
        corrections = {
            'CO_cum': {
                'low': [
                    "Vérifiez l'efficacité de la combustion.",
                    "Assurez-vous qu'il n'y a pas de fuite d'air.",
                    "Réglez le mélange air/carburant."
                ],
                'high': [
                    "Vérifiez le système d'injection de carburant.",
                    "Assurez-vous qu'il n'y a pas de problèmes d'allumage.",
                    "Contrôlez l'état du catalyseur."
                ]
            },
            'NOx_cum': {
                'low': [
                    "Assurez-vous que le moteur fonctionne à la température optimale.",
                    "Vérifiez le bon fonctionnement du système EGR.",
                    "Assurez-vous que les capteurs de température sont corrects."
                ],
                'high': [
                    "Vérifiez le système de réduction catalytique sélective (SCR).",
                    "Ajustez le rapport air/carburant.",
                    "Contrôlez l'état du convertisseur catalytique."
                ]
            },
            'HC_cum': {
                'low': [
                    "Vérifiez les bougies d'allumage.",
                    "Assurez-vous que les injecteurs de carburant ne fuient pas.",
                    "Contrôlez le système d'allumage pour une combustion complète."
                ],
                'high': [
                    "Vérifiez les injecteurs de carburant.",
                    "Assurez-vous que le système d'allumage est en bon état.",
                    "Vérifiez les composants du moteur pour des dépôts de carbone."
                ]
            },
            'PM_cum': {
                'low': [
                    "Assurez-vous que le moteur fonctionne à la température optimale.",
                    "Vérifiez le système de gestion de la température.",
                    "Assurez-vous que le filtre à particules fonctionne correctement."
                ],
                'high': [
                    "Vérifiez les filtres à particules.",
                    "Assurez-vous que les filtres ne sont pas obstrués.",
                    "Vérifiez l'état et le fonctionnement du système de régénération des filtres."
                ]
            }
        }
        correction_messages = corrections.get(pollutant, {}).get(condition, [])
        if ecart_percent > 50:
            return correction_messages[0]
        elif 20 < ecart_percent <= 50:
            return correction_messages[1]
        else:
            return correction_messages[2] if len(correction_messages) > 2 else ""

class EmissionDataVisualizer:
    def __init__(self, data, layout):
        self.data = data
        self.layout = layout
        self.units = {
            'Temps': 's',
            'Distance': 'km',
            'CO_cum': 'g/km',
            'NOx_cum': 'g/km',
            'HC_cum': 'g/km',
            'PM_cum': 'g/km'
        }

    def plot_with_reference(self, input_column, results):
        fig = Figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        y_labels = []

        for column, stats in results.items():
            ax.plot(self.data[input_column], self.data[column], label=f"{column} ({self.units.get(column, '')})")
            ax.axhline(stats['lower'], color='green', linestyle='--', label=f'{column} Limite Inférieure')
            ax.axhline(stats['upper'], color='red', linestyle='--', label=f'{column} Limite Supérieure')

            # Coloration des zones en dessous, entre et au-dessus des limites
            ax.fill_between(self.data[input_column], self.data[column], stats['lower'], 
                            where=(self.data[column] < stats['lower']), color='yellow', alpha=0.5, interpolate=True)
            ax.fill_between(self.data[input_column], stats['lower'], stats['upper'], 
                            where=((self.data[column] >= stats['lower']) & (self.data[column] <= stats['upper'])), 
                            color='green', alpha=0.3, interpolate=True)
            ax.fill_between(self.data[input_column], self.data[column], stats['upper'], 
                            where=(self.data[column] > stats['upper']), color='red', alpha=0.5, interpolate=True)
            
            y_labels.append(f"{column} ({self.units.get(column, '')})")

        ax.set_title("Analyse des émissions avec références (Norme Euro 6)", fontsize=12, fontweight='bold')
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

class EmissionInputSelectionDialog(QDialog):
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

class EmissionOutputSelectionDialog(QDialog):
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
