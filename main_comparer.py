from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem
from classes_comparer import DataHandler, ComparisonVisualizer, ParameterSelectionDialog, StatisticalAnalysis
import pandas as pd

class ComparaisonBancsEssais(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comparaison des bancs d'essai")
        self.setGeometry(100, 100, 1400, 900)

        self.data_handler_real = DataHandler()
        self.data_handler_virtual = DataHandler()

        self.bouton_charger_reel = QPushButton("Charger les données réelles", self)
        self.bouton_charger_reel.setGeometry(50, 50, 200, 40)
        self.bouton_charger_reel.clicked.connect(self.load_real_data)

        self.bouton_charger_virtuel = QPushButton("Charger les données virtuelles", self)
        self.bouton_charger_virtuel.setGeometry(50, 100, 200, 40)
        self.bouton_charger_virtuel.clicked.connect(self.load_virtual_data)

        self.bouton_select_param = QPushButton("Sélectionner les paramètres à comparer", self)
        self.bouton_select_param.setGeometry(50, 150, 250, 40)
        self.bouton_select_param.clicked.connect(self.select_parameters)

        self.bouton_comparer = QPushButton("Comparer les résultats", self)
        self.bouton_comparer.setGeometry(50, 200, 200, 40)
        self.bouton_comparer.clicked.connect(self.compare_results)

        self.bouton_histo_ecarts = QPushButton("Afficher les histogrammes des écarts", self)
        self.bouton_histo_ecarts.setGeometry(50, 250, 250, 40)
        self.bouton_histo_ecarts.clicked.connect(self.plot_histogram_ecarts)

        self.chart_widget = QWidget(self)
        self.chart_widget.setGeometry(300, 50, 1000, 400)
        self.chart_layout = QVBoxLayout(self.chart_widget)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(50, 470, 1300, 400)
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["Paramètre", "Moyenne réelle (± écart type)", "Moyenne virtuelle (± écart type)", "Écart moyen (%)", "Corrélation", "Conclusion"])
        self.table_widget.setColumnWidth(0, 200)
        self.table_widget.setColumnWidth(1, 200)
        self.table_widget.setColumnWidth(2, 200)
        self.table_widget.setColumnWidth(3, 150)
        self.table_widget.setColumnWidth(4, 150)
        self.table_widget.setColumnWidth(5, 300)

        self.selected_parameters = []

    def load_real_data(self):
        self.data_handler_real.load_data("Données réelles")

    def load_virtual_data(self):
        self.data_handler_virtual.load_data("Données virtuelles")

    def select_parameters(self):
        if self.data_handler_real.data is not None and self.data_handler_virtual.data is not None:
            dialog = ParameterSelectionDialog(self)
            dialog.set_column_names(self.data_handler_real.data.columns)
            if dialog.exec():
                self.selected_parameters = dialog.get_selected_columns()
                QMessageBox.information(self, "Paramètres sélectionnés", f"Paramètres sélectionnés : {', '.join(self.selected_parameters)}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez charger les données réelles et virtuelles d'abord !")

    def compare_results(self):
        if self.selected_parameters:
            visualizer = ComparisonVisualizer(self.data_handler_real.data, self.data_handler_virtual.data, self.chart_layout)
            visualizer.plot_comparison(self.selected_parameters)

            analysis = StatisticalAnalysis(self.data_handler_real.data, self.data_handler_virtual.data)
            self.populate_table(analysis, self.selected_parameters)
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les paramètres à comparer d'abord !")

    def populate_table(self, analysis, parameters):
        self.table_widget.setRowCount(len(parameters))
        for i, param in enumerate(parameters):
            stats = analysis.calculate_statistics(param)
            correlation = analysis.calculate_correlation(param)

            conclusion = self.determine_conclusion(stats['error_rel'])

            self.table_widget.setItem(i, 0, QTableWidgetItem(param))
            self.table_widget.setItem(i, 1, QTableWidgetItem(f"{stats['mean_real']:.2f} ± {stats['std_real']:.2f}"))
            self.table_widget.setItem(i, 2, QTableWidgetItem(f"{stats['mean_virtual']:.2f} ± {stats['std_virtual']:.2f}"))
            self.table_widget.setItem(i, 3, QTableWidgetItem(f"{stats['error_rel']:.2f} %"))
            self.table_widget.setItem(i, 4, QTableWidgetItem(f"{correlation:.2f}"))
            self.table_widget.setItem(i, 5, QTableWidgetItem(conclusion))

    def determine_conclusion(self, error_rel):
        if error_rel <= 5:
            return "Fiable"
        elif 5 < error_rel <= 15:
            return "Modérément fiable"
        else:
            return "Peu fiable"

    def plot_histogram_ecarts(self):
        if self.selected_parameters:
            visualizer = ComparisonVisualizer(self.data_handler_real.data, self.data_handler_virtual.data, self.chart_layout)
            for param in self.selected_parameters:
                visualizer.plot_histogram(param, self.data_handler_real.data[param], self.data_handler_virtual.data[param])
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les paramètres à comparer d'abord !")

if __name__ == "__main__":
    app = QApplication([])
    window = ComparaisonBancsEssais()
    window.show()
    app.exec()
