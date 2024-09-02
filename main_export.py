from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QComboBox, QLabel
from classes_export import DataExporter
import pandas as pd

class ExportTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Outil d'exportation")
        self.setGeometry(100, 100, 800, 600)

        self.exporter = DataExporter()

        layout = QVBoxLayout()

        self.label_select_analysis = QLabel("Sélectionnez ce que vous voulez exporter :", self)
        layout.addWidget(self.label_select_analysis)

        self.combobox_analysis = QComboBox(self)
        self.combobox_analysis.addItems(["Analyse", "Comparaison"])
        layout.addWidget(self.combobox_analysis)

        self.label_select_format = QLabel("Sélectionnez le format d'exportation :", self)
        layout.addWidget(self.label_select_format)

        self.combobox_format = QComboBox(self)
        self.combobox_format.addItems(["PDF", "Excel"])
        layout.addWidget(self.combobox_format)

        self.button_export = QPushButton("Exporter", self)
        self.button_export.clicked.connect(self.export_data)
        layout.addWidget(self.button_export)

        self.button_generate_report = QPushButton("Générer un rapport détaillé", self)
        self.button_generate_report.clicked.connect(self.generate_report)
        layout.addWidget(self.button_generate_report)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def export_data(self):
        analysis_type = self.combobox_analysis.currentText()
        export_format = self.combobox_format.currentText()
        self.exporter.export(analysis_type, export_format)

    def generate_report(self):
        export_format = self.combobox_format.currentText()
        self.exporter.generate_detailed_report(export_format)

if __name__ == "__main__":
    app = QApplication([])
    window = ExportTool()
    window.show()
    app.exec()
