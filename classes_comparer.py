import pandas as pd
from scipy.stats import pearsonr, ttest_ind
from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QListWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DataHandler:
    def __init__(self):
        self.data = None

    def load_data(self, data_type):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Fichiers CSV (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                self.data = pd.read_csv(file_path)
                if self.validate_data(self.data):
                    QMessageBox.information(None, "Succès", f"{data_type} chargées avec succès !")
                else:
                    QMessageBox.warning(None, "Erreur", f"{data_type} invalides ou manquantes.")
            except Exception as e:
                QMessageBox.warning(None, "Erreur", f"Erreur lors du chargement des {data_type} : {str(e)}")

    def validate_data(self, data):
        return not data.empty

class ComparisonVisualizer:
    def __init__(self, real_data, virtual_data, layout):
        self.real_data = real_data
        self.virtual_data = virtual_data
        self.layout = layout
        self.units = {
            'Temps': 's',
            'Couple': 'Nm',
            'Puissance': 'HP',
            'RPM': 'tr/min',
            'Conso Carburant': 'L/100km',
            'Température': '°C',
            'Conso Air': 'g/s',
            'CO': 'g/s',
            'HC': 'g/s',
            'PM': 'g/s',
            'NOx': 'g/s',
            'CO_cum': 'g/km',
            'HC_cum': 'g/km',
            'PM_cum': 'g/km',
            'NOx_cum': 'g/km',
            'Accélération': 'm/s²',
            'Vitesse': 'km/h',
            'Temps Accé': 's',
            'Freinage': 'm/s²',
            'Vibration': 'm/s²',
            'Distance': 'km'
        }

    def plot_comparison(self, parameters):
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.set_title("Comparaison des paramètres", fontsize=12, fontweight='bold')

        for param in parameters:
            ax.plot(self.real_data['Temps'], self.real_data[param], label=f'Real {param}')
            ax.plot(self.virtual_data['Temps'], self.virtual_data[param], linestyle='--', label=f'Virtual {param}')

        ax.set_xlabel(f'Temps (s)')
        y_labels = ', '.join([f"{param} ({self.units.get(param, '')})" for param in parameters])
        ax.set_ylabel(y_labels)
        ax.legend()

        canvas = FigureCanvas(fig)
        for i in reversed(range(self.layout.count())):
            widgetToRemove = self.layout.itemAt(i).widget()
            self.layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
        self.layout.addWidget(canvas)
        fig.tight_layout(pad=2.0, w_pad=2.0, h_pad=2.0)
        canvas.draw()

    def plot_histogram(self, parameter, real_data, virtual_data):
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.set_title(f"Histogramme des écarts pour {parameter}")

        ecarts = real_data - virtual_data
        ax.hist(ecarts, bins=20, alpha=0.75, color='blue', edgecolor='black')
        ax.set_xlabel('Écart')
        ax.set_ylabel('Fréquence')

        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)
        canvas.draw()

class ParameterSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sélectionnez les paramètres à comparer")
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

class StatisticalAnalysis:
    def __init__(self, real_data, virtual_data):
        self.real_data = real_data
        self.virtual_data = virtual_data
        self.units = {
            'Temps': 's',
            'Couple': 'Nm',
            'Puissance': 'HP',
            'RPM': 'tr/min',
            'Conso Carburant': 'L/100km',
            'Température': '°C',
            'Conso Air': 'g/s',
            'CO': 'g/s',
            'HC': 'g/s',
            'PM': 'g/s',
            'NOx': 'g/s',
            'CO_cum': 'g/km',
            'HC_cum': 'g/km',
            'PM_cum': 'g/km',
            'NOx_cum': 'g/km',
            'Accélération': 'm/s²',
            'Vitesse': 'km/h',
            'Temps Accé': 's',
            'Freinage': 'm/s²',
            'Vibration': 'm/s²',
            'Distance': 'km'
        }

    def calculate_statistics(self, parameter):
        real_values = self.real_data[parameter]
        virtual_values = self.virtual_data[parameter]
        mean_real = real_values.mean()
        mean_virtual = virtual_values.mean()
        std_real = real_values.std()
        std_virtual = virtual_values.std()
        error_abs = abs(mean_real - mean_virtual)
        error_rel = (error_abs / mean_real) * 100 if mean_real != 0 else 0

        return {
            'mean_real': mean_real,
            'mean_virtual': mean_virtual,
            'std_real': std_real,
            'std_virtual': std_virtual,
            'error_abs': error_abs,
            'error_rel': error_rel
        }

    def calculate_correlation(self, parameter):
        real_values = self.real_data[parameter]
        virtual_values = self.virtual_data[parameter]
        correlation, _ = pearsonr(real_values, virtual_values)
        return correlation

    def perform_statistical_tests(self, parameter):
        real_values = self.real_data[parameter]
        virtual_values = self.virtual_data[parameter]
        t_stat, p_value = ttest_ind(real_values, virtual_values)
        return {
            't_stat': t_stat,
            'p_value': p_value
        }

    def get_comparison_data(self, analysis, parameters):
        comparison_data = []
        for param in parameters:
            stats = analysis.calculate_statistics(param)
            correlation = analysis.calculate_correlation(param)
            conclusion = self.determine_conclusion(stats['error_rel'])

            comparison_data.append({
                'Paramètre': f"{param} ({self.units.get(param, '')})",
                'Moyenne réelle': f"{stats['mean_real']:.4f}",
                'Moyenne virtuelle': f"{stats['mean_virtual']:.4f}",
                'Écart moyen (%)': f"{stats['error_rel']:.4f} %",
                'Corrélation': f"{correlation:.4f}",
                'Conclusion': conclusion
            })
        return comparison_data

    def determine_conclusion(self, error_rel):
        if error_rel <= 5:
            return "Fiable"
        elif 5 < error_rel <= 15:
            return "Modérément fiable"
        else:
            return "Peu fiable"
