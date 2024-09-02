from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog
from classes_comparaison import DataHandler, InputSelectionDialog, OutputSelectionDialog
import pandas as pd

class OutilComparison(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Outil de Comparaison des Bancs d'Essai")
        self.setGeometry(100, 100, 1400, 900)

        self.data_handler = DataHandler()

        # Boutons de chargement des données
        self.bouton_charger_reel = QPushButton("Charger les données réelles", self)
        self.bouton_charger_reel.setGeometry(50, 50, 200, 40)
        self.bouton_charger_reel.clicked.connect(self.data_handler.load_real_data)

        self.bouton_charger_virtuel = QPushButton("Charger les données virtuelles", self)
        self.bouton_charger_virtuel.setGeometry(50, 100, 200, 40)
        self.bouton_charger_virtuel.clicked.connect(self.data_handler.load_virtual_data)

        # Bouton de sélection des paramètres
        self.bouton_selection_parametres = QPushButton("Sélectionner les paramètres", self)
        self.bouton_selection_parametres.setGeometry(50, 150, 200, 40)
        self.bouton_selection_parametres.clicked.connect(self.select_parameters)

        # Bouton de comparaison
        self.bouton_comparer = QPushButton("Comparer", self)
        self.bouton_comparer.setGeometry(50, 200, 200, 40)
        self.bouton_comparer.clicked.connect(self.compare_data)

        self.input_column = None
        self.output_columns = []

        # Tableau des résultats de la comparaison
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(300, 50, 1000, 800)
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["Paramètre", "Moyenne Réelle", "Moyenne Virtuelle", "Écart Moyen", "Écart Moyen (%)"])
        self.table_widget.setColumnWidth(0, 200)
        self.table_widget.setColumnWidth(1, 200)
        self.table_widget.setColumnWidth(2, 200)
        self.table_widget.setColumnWidth(3, 200)
        self.table_widget.setColumnWidth(4, 200)

    def select_parameters(self):
        if self.data_handler.data_real is None or self.data_handler.data_virtual is None:
            QMessageBox.warning(self, "Erreur", "Veuillez charger les données réelles et virtuelles d'abord !")
            return

        dialog = OutputSelectionDialog(self)
        dialog.set_column_names(self.data_handler.data_real.columns)
        if dialog.exec():
            self.output_columns = dialog.get_selected_columns()
            QMessageBox.information(self, "Paramètres sélectionnés", f"Paramètres sélectionnés : {', '.join(self.output_columns)}")

    def compare_data(self):
        if self.output_columns:
            comparison_results = self.data_handler.compare_data(self.output_columns)
            self.populate_table(comparison_results)
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les paramètres à comparer !")

    def populate_table(self, results):
        self.table_widget.setRowCount(len(results))
        for i, result in enumerate(results):
            self.table_widget.setItem(i, 0, QTableWidgetItem(result['param']))
            self.table_widget.setItem(i, 1, QTableWidgetItem(f"{result['mean_real']:.2f}"))
            self.table_widget.setItem(i, 2, QTableWidgetItem(f"{result['mean_virtual']:.2f}"))
            self.table_widget.setItem(i, 3, QTableWidgetItem(f"{result['ecart_mean']:.2f}"))
            self.table_widget.setItem(i, 4, QTableWidgetItem(f"{result['ecart_percent_mean']:.2f}%"))

if __name__ == "__main__":
    app = QApplication([])
    window = OutilComparison()
    window.show()
    app.exec()
