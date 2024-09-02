from PySide6.QtWidgets import QMainWindow, QTableView, QFileDialog, QPushButton, QVBoxLayout, QWidget, QMessageBox, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from fpdf import FPDF
import xlsxwriter
from datetime import datetime
from PySide6.QtCore import Qt
from tableau_analyse import Ui_MainWindow  # Assurez-vous que ce fichier est généré à partir de votre fichier .ui

class DataExporter:
    def __init__(self, file_path):
        self.logo_path = "SII-removebg-preview.png"
        self.file_path = file_path

    def export(self, data, export_format):
        if export_format == "PDF":
            self.export_to_pdf(data)
        else:
            self.export_to_excel(data)

    def export_to_pdf(self, data):
        pdf = FPDF('L', 'mm', 'A4')
        pdf.add_page()
        self.add_logo(pdf)
        pdf.set_font("Arial", size=10)

        pdf.ln(20)  # Ajouter un espace après le logo

        title = data["title"]
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, txt=f"{title} - {date_time}", ln=True, align='C')

        pdf.set_font("Arial", size=10)

        for row in data["content"]:
            for i, item in enumerate(row):
                if i == 4:  # Correction column
                    width = 115
                else:
                    width = 30
                pdf.cell(width, 10, txt=item, border=1)
            pdf.ln(10)

        pdf.output(self.file_path)
        print(f"Data exported to PDF successfully! File saved at: {self.file_path}")

    def export_to_excel(self, data):
        workbook = xlsxwriter.Workbook(self.file_path)
        worksheet = workbook.add_worksheet()

        row = 0
        for line in data["content"]:
            col = 0
            for item in line:
                worksheet.write(row, col, item)
                col += 1
            row += 1

        worksheet.set_column(4, 4, 70)  # Set the width of the Correction column to 70

        workbook.close()
        print(f"Data exported to Excel successfully! File saved at: {self.file_path}")

    def add_logo(self, pdf):
        pdf.image(self.logo_path, 10, 10, 30)  # Position et taille ajustées pour le logo

class TableauAnalyseWindow(QMainWindow):
    def __init__(self, data, columns, parent=None):
        super(TableauAnalyseWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data = data
        self.columns = columns
        self.init_ui()

    def init_ui(self):
        self.populate_table()
        self.ui.pushButton.clicked.connect(self.export_table)

    def populate_table(self):
        model = QStandardItemModel(len(self.data), len(self.columns))
        model.setHorizontalHeaderLabels(self.columns)

        for row, entry in enumerate(self.data):
            for col, column in enumerate(self.columns):
                model.setItem(row, col, QStandardItem(str(entry.get(column, 'N/A'))))

        self.ui.tableView.setModel(model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def export_table(self):
        options = QFileDialog.Options()
        file_filter = "PDF Files (*.pdf);;Excel Files (*.xlsx);;All Files (*)"
        file_path, _ = QFileDialog.getSaveFileName(self, "Exporter le tableau", "", file_filter, options=options)

        if file_path:
            if file_path.endswith(".pdf"):
                self.export_to_format("PDF", file_path)
            elif file_path.endswith(".xlsx"):
                self.export_to_format("Excel", file_path)
            else:
                QMessageBox.warning(self, "Erreur", "Format de fichier non supporté.")

    def export_to_format(self, export_format, file_path):
        data_exporter = DataExporter(file_path)
        data = {
            "title": "Tableau d'Analyse",
            "content": [
                self.columns
            ]
        }
        for entry in self.data:
            data["content"].append([str(entry.get(column, 'N/A')) for column in self.columns])

        data_exporter.export(data, export_format)
        QMessageBox.information(self, "Succès", f"Tableau exporté en format {export_format} avec succès !")

