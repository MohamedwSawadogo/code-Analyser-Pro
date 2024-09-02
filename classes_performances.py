import pandas as pd
from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QListWidget, QPushButton, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DataHandler:
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

class ReferenceHandler:
    def __init__(self):
        self.references = {
            'Couple': {'min': 100, 'nominal': 173, 'max': 200, 'unit': 'Nm'},
            'Puissance': {'min': 120, 'nominal': 132, 'max': 140, 'unit': 'HP'},
            'RPM': {'min': 700, 'nominal': 4000, 'max': 6500, 'unit': 'tr/min'},
            'Conso Carburant': {'min': 6.5, 'nominal': 7.6, 'max': 8.5, 'unit': 'L/100km'},
            'Température': {'min': 85, 'nominal': 90, 'max': 110, 'unit': '°C'},
            'Conso Air': {'min': 20, 'nominal': 25, 'max': 30, 'unit': 'g/s'}
        }

    def get_reference(self, parameter):
        return self.references.get(parameter, None)

class PerformanceAnalysis:
    def __init__(self, data, input_column, output_columns, reference_handler):
        self.data = data
        self.input_column = input_column
        self.output_columns = output_columns
        self.reference_handler = reference_handler
        self.units = {
            'Couple': 'Nm',
            'Puissance': 'HP',
            'RPM': 'tr/min',
            'Conso Carburant': 'L/100km',
            'Température': '°C',
            'Conso Air': 'g/s',
            'Temps': 's',
            'Distance': 'km'
        }

    def analyze(self):
        results = {}
        anomalies = []
        for column in self.output_columns:
            reference = self.reference_handler.get_reference(column)
            if reference:
                min_val = reference['min']
                nom_val = reference['nominal']
                max_val = reference['max']
                deviations = (self.data[column] - nom_val) / nom_val * 100
                within_bounds = (self.data[column] >= min_val) & (self.data[column] <= max_val)
                results[column] = {
                    'mean': self.data[column].mean(),
                    'std': self.data[column].std(),
                    'min': min_val,
                    'max': max_val,
                    'nominal': nom_val,
                    'unit': reference['unit'],
                    'within_bounds': within_bounds,
                    'deviations': deviations
                }
                for idx, value in self.data[[self.input_column, column]].iterrows():
                    ecart_percent, comment, correction = self.generate_comment_and_correction(column, value[column], min_val, nom_val, max_val)
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

    def generate_comment_and_correction(self, parameter, value, min_val, nom_val, max_val):
        if value < min_val:
            ecart = min_val - value
            ecart_percent = (ecart / min_val) * 100 if min_val != 0 else 0
            comment = f"La valeur de {parameter} ({value}) est en dessous de la limite minimale ({min_val}) par {ecart} ({abs(ecart_percent):.2f}%)."
            correction = self.get_correction(parameter, "low", ecart_percent)
        elif value > max_val:
            ecart = value - max_val
            ecart_percent = (ecart / max_val) * 100 if max_val != 0 else 0
            comment = f"La valeur de {parameter} ({value}) dépasse la limite maximale ({max_val}) par {ecart} ({abs(ecart_percent):.2f}%)."
            correction = self.get_correction(parameter, "high", ecart_percent)
        else:
            ecart = value - nom_val
            ecart_percent = (ecart / nom_val) * 100 if nom_val != 0 else 0
            comment = f"La valeur de {parameter} ({value}) est proche de la valeur nominale ({nom_val}) avec un écart de {abs(ecart_percent):.2f}%."
            correction = self.get_correction(parameter, "nominal", ecart_percent)
        
        return abs(ecart_percent), comment, correction

    def get_correction(self, parameter, condition, ecart_percent):
        corrections = {
            'Couple': {
                'low': [
                    "Augmentez la pression de suralimentation.",
                    "Vérifiez l'état des injecteurs et nettoyez-les si nécessaire.",
                    "Assurez-vous que le mélange air-carburant est optimal."
                ],
                'high': [
                    "Réduisez la pression de suralimentation.",
                    "Vérifiez les paramètres de l'ECU pour éviter une suralimentation.",
                    "Contrôlez les capteurs de couple pour des lectures précises."
                ],
                'nominal': [
                    "Ajustez légèrement les paramètres pour optimiser la performance.",
                    "Vérifiez les systèmes auxiliaires pour assurer un fonctionnement optimal."
                ]
            },
            'Puissance': {
                'low': [
                    "Vérifiez la qualité du carburant.",
                    "Assurez-vous que le moteur fonctionne à la température optimale.",
                    "Contrôlez les filtres à air et à carburant."
                ],
                'high': [
                    "Vérifiez les niveaux de liquide de refroidissement.",
                    "Assurez-vous que le système de refroidissement fonctionne correctement.",
                    "Contrôlez les capteurs de puissance pour des lectures précises."
                ],
                'nominal': [
                    "Optimisez les réglages du moteur.",
                    "Assurez-vous que tous les composants fonctionnent correctement."
                ]
            },
            'RPM': {
                'low': [
                    "Vérifiez le système d'allumage.",
                    "Assurez-vous que l'accélérateur fonctionne correctement.",
                    "Contrôlez les paramètres de l'ECU pour des réglages appropriés."
                ],
                'high': [
                    "Vérifiez le régulateur de vitesse.",
                    "Assurez-vous que le moteur n'est pas en sur-régime.",
                    "Contrôlez les capteurs de régime pour des lectures précises."
                ],
                'nominal': [
                    "Ajustez les paramètres de gestion du moteur.",
                    "Vérifiez les systèmes auxiliaires pour un fonctionnement optimal."
                ]
            },
            'Conso Carburant': {
                'low': [
                    "Vérifiez l'efficacité de la combustion.",
                    "Assurez-vous qu'il n'y a pas de fuites de carburant.",
                    "Contrôlez les injecteurs pour un fonctionnement optimal."
                ],
                'high': [
                    "Réduisez la charge sur le moteur.",
                    "Assurez-vous que le moteur fonctionne à la température optimale.",
                    "Vérifiez les filtres à carburant."
                ],
                'nominal': [
                    "Optimisez les paramètres de combustion.",
                    "Assurez-vous que tous les systèmes fonctionnent correctement."
                ]
            },
            'Température': {
                'low': [
                    "Vérifiez le thermostat.",
                    "Assurez-vous que le système de refroidissement fonctionne correctement.",
                    "Contrôlez les capteurs de température."
                ],
                'high': [
                    "Inspectez le radiateur.",
                    "Vérifiez les niveaux de liquide de refroidissement.",
                    "Assurez-vous que le ventilateur de refroidissement fonctionne correctement."
                ],
                'nominal': [
                    "Maintenez les niveaux de liquide de refroidissement.",
                    "Assurez-vous que le système de refroidissement fonctionne correctement."
                ]
            },
            'Conso Air': {
                'low': [
                    "Vérifiez les filtres à air.",
                    "Assurez-vous que le système de prise d'air est propre.",
                    "Contrôlez les capteurs de débit d'air."
                ],
                'high': [
                    "Vérifiez le débitmètre d'air.",
                    "Assurez-vous que le turbo fonctionne correctement.",
                    "Contrôlez les conduits d'admission d'air."
                ],
                'nominal': [
                    "Assurez-vous que le système de prise d'air fonctionne correctement.",
                    "Maintenez les filtres à air propres."
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

class DataVisualizer:
    def __init__(self, data, layout):
        self.data = data
        self.layout = layout
        self.units = {
            'Couple': 'Nm',
            'Puissance': 'HP',
            'RPM': 'tr/min',
            'Conso Carburant': 'L/100km',
            'Température': '°C',
            'Conso Air': 'g/s',
            'Temps': 's'
        }

    def plot_with_reference(self, input_column, results):
        fig = Figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        y_labels = []

        for column, stats in results.items():
            ax.plot(self.data[input_column], self.data[column], label=f"{column} ({stats['unit']})")
            ax.axhline(stats['min'], color='green', linestyle='--', label=f'{column} Minimum')
            ax.axhline(stats['nominal'], color='blue', linestyle='--', label=f'{column} Nominal')
            ax.axhline(stats['max'], color='red', linestyle='--', label=f'{column} Maximum')

            # Coloration des zones en dessous, entre et au-dessus des limites
            ax.fill_between(self.data[input_column], self.data[column], stats['min'], 
                            where=(self.data[column] < stats['min']), color='blue', alpha=0.5, interpolate=True)
            ax.fill_between(self.data[input_column], stats['min'], stats['max'], 
                            where=((self.data[column] >= stats['min']) & (self.data[column] <= stats['max'])), 
                            color='green', alpha=0.3, interpolate=True)
            ax.fill_between(self.data[input_column], self.data[column], stats['max'], 
                            where=(self.data[column] > stats['max']), color='red', alpha=0.5, interpolate=True)
            
            y_labels.append(f"{column} ({stats['unit']})")

        ax.set_title(f"Analyse des performances avec références", fontsize=12, fontweight='bold')
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

class InputSelectionDialog(QDialog):
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

class OutputSelectionDialog(QDialog):
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
