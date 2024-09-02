from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QFileDialog
from classes_analyse import DataHandler, ReferenceHandler, EmissionAnalysis, DataVisualizer, InputSelectionDialog, OutputSelectionDialog
import pandas as pd
from fpdf import FPDF

class OutilAnalyse(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Outil d'analyse des émissions")
        self.setGeometry(100, 100, 1400, 900)

        self.data_handler = DataHandler()
        self.reference_handler = ReferenceHandler()

        self.bouton_charger = QPushButton("Charger les données", self)
        self.bouton_charger.setGeometry(50, 50, 200, 40)
        self.bouton_charger.clicked.connect(self.data_handler.load_data)

        self.bouton_colonne_entree = QPushButton("Sélectionner la colonne d'entrée", self)
        self.bouton_colonne_entree.setGeometry(50, 100, 200, 40)
        self.bouton_colonne_entree.clicked.connect(self.select_input_column)

        self.bouton_colonnes_sortie = QPushButton("Sélectionner les colonnes de sortie", self)
        self.bouton_colonnes_sortie.setGeometry(50, 150, 200, 40)
        self.bouton_colonnes_sortie.clicked.connect(self.select_output_columns)

        self.bouton_analyser = QPushButton("Analyser les émissions", self)
        self.bouton_analyser.setGeometry(50, 200, 200, 40)
        self.bouton_analyser.clicked.connect(self.analyze_emissions)

        self.bouton_exporter = QPushButton("Exporter les résultats", self)
        self.bouton_exporter.setGeometry(50, 250, 200, 40)
        self.bouton_exporter.clicked.connect(self.export_results)

        self.input_column = None
        self.output_columns = []

        self.chart_widget = QWidget(self)
        self.chart_widget.setGeometry(300, 50, 1000, 400)
        self.chart_layout = QVBoxLayout(self.chart_widget)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(50, 470, 1300, 400)
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["Temps", "Polluant", "Valeur", "Écart (%)", "Commentaire", "Correction"])
        self.table_widget.setColumnWidth(0, 100)
        self.table_widget.setColumnWidth(1, 100)
        self.table_widget.setColumnWidth(2, 100)
        self.table_widget.setColumnWidth(3, 100)
        self.table_widget.setColumnWidth(4, 500)
        self.table_widget.setColumnWidth(5, 500)

    def select_input_column(self):
        dialog = InputSelectionDialog(self)
        dialog.set_column_names(self.data_handler.data.columns)
        if dialog.exec():
            self.input_column = dialog.get_selected_column()
            QMessageBox.information(self, "Colonne d'entrée sélectionnée", f"Colonne sélectionnée : {self.input_column}")

    def select_output_columns(self):
        dialog = OutputSelectionDialog(self)
        dialog.set_column_names(self.data_handler.data.columns)
        if dialog.exec():
            self.output_columns = dialog.get_selected_columns()
            QMessageBox.information(self, "Colonnes de sortie sélectionnées", f"Colonnes sélectionnées : {', '.join(self.output_columns)}")

    def analyze_emissions(self):
        if self.input_column and self.output_columns:
            analysis = EmissionAnalysis(self.data_handler.data, self.input_column, self.output_columns, self.reference_handler)
            results, anomalies = analysis.analyze()
            visualizer = DataVisualizer(self.data_handler.data, self.chart_layout)
            visualizer.plot_with_reference(self.input_column, results)
            self.populate_table(anomalies)
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les colonnes d'entrée et de sortie d'abord !")

    def populate_table(self, anomalies):
        self.table_widget.setRowCount(len(anomalies))
        for i, anomaly in enumerate(anomalies):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(anomaly['Temps'])))
            self.table_widget.setItem(i, 1, QTableWidgetItem(anomaly['Polluant']))
            self.table_widget.setItem(i, 2, QTableWidgetItem(str(anomaly['Valeur'])))
            self.table_widget.setItem(i, 3, QTableWidgetItem(f"{anomaly['Écart (%)']:.2f}"))
            self.table_widget.setItem(i, 4, QTableWidgetItem(anomaly['Commentaire']))
            self.table_widget.setItem(i, 5, QTableWidgetItem(anomaly['Correction']))

    def export_results(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Exporter les résultats", "", "Fichiers Excel (*.xlsx);;Tous les fichiers (*)", options=options)
        if file_path:
            self.save_results_to_excel(file_path)

    def save_results_to_excel(self, file_path):
        data = []
        for row in range(self.table_widget.rowCount()):
            row_data = []
            for column in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, column)
                row_data.append(item.text() if item else "")
            data.append(row_data)
        df = pd.DataFrame(data, columns=["Temps", "Polluant", "Valeur", "Écart (%)", "Commentaire", "Correction"])
        df.to_excel(file_path, index=False)
        QMessageBox.information(self, "Succès", "Les résultats ont été exportés avec succès !")



if __name__ == "__main__":
    app = QApplication([])
    window = OutilAnalyse()
    window.show()
    app.exec()
