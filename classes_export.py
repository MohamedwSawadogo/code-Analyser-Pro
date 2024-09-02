import pandas as pd
from fpdf import FPDF
import xlsxwriter
from datetime import datetime

class DataExporter:
    def __init__(self):
        self.logo_path = "SII-removebg-preview.png"  # Chemin vers le logo de la société

    def export(self, analysis_type, export_format):
        if analysis_type == "Analyse":
            data = self.get_analysis_data()
        else:
            data = self.get_comparison_data()

        if export_format == "PDF":
            self.export_to_pdf(data)
        else:
            self.export_to_excel(data)

    def get_analysis_data(self):
        # Placeholder function to get analysis data
        # Replace with actual data retrieval
        return {
            "title": "Analyse des données",
            "content": [
                ["Paramètre", "Valeur moyenne", "Écart-type", "Commentaire", "Suggestion"],
                ["CO", "0.5", "0.1", "Niveau de CO conforme", "Aucune action nécessaire"],
                ["NOx", "0.03", "0.01", "Niveau de NOx conforme", "Aucune action nécessaire"],
                ["HC", "0.05", "0.02", "Niveau de HC élevé", "Vérifier le système d'injection"],
                ["PM", "0.002", "0.001", "Niveau de PM conforme", "Aucune action nécessaire"]
            ]
        }

    def get_comparison_data(self):
        # Placeholder function to get comparison data
        # Replace with actual data retrieval
        return {
            "title": "Comparaison des bancs d'essai",
            "content": [
                ["Paramètre", "Valeur réelle", "Valeur virtuelle", "Écart moyen (%)", "Corrélation", "Conclusion"],
                ["CO", "0.5", "0.5", "0.0%", "0.99", "Fiable"],
                ["NOx", "0.03", "0.03", "0.0%", "0.98", "Fiable"],
                ["HC", "0.05", "0.05", "0.0%", "0.97", "Fiable"],
                ["PM", "0.002", "0.002", "0.0%", "0.96", "Fiable"]
            ]
        }

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
                if i == 3:  # Commentaire column
                    width = 70
                elif i == 4:  # Suggestion column
                    width = 90
                else:
                    width = 35
                pdf.cell(width, 10, txt=item, border=1)
            pdf.ln(10)

        pdf.output("exported_data.pdf")
        print("Data exported to PDF successfully!")

    def export_to_excel(self, data):
        workbook = xlsxwriter.Workbook("exported_data.xlsx")
        worksheet = workbook.add_worksheet()

        row = 0
        for line in data["content"]:
            col = 0
            for item in line:
                worksheet.write(row, col, item)
                col += 1
            row += 1

        workbook.close()
        print("Data exported to Excel successfully!")

    def generate_detailed_report(self, export_format):
        analysis_data = self.get_analysis_data()
        comparison_data = self.get_comparison_data()

        if export_format == "PDF":
            self.generate_detailed_pdf_report(analysis_data, comparison_data)
        else:
            self.generate_detailed_excel_report(analysis_data, comparison_data)

    def generate_detailed_pdf_report(self, analysis_data, comparison_data):
        pdf = FPDF('L', 'mm', 'A4')
        pdf.add_page()
        self.add_logo(pdf)
        pdf.set_font("Arial", size=10)

        pdf.ln(20)  # Ajouter un espace après le logo

        # Add analysis data
        title = analysis_data["title"]
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, txt=f"{title} - {date_time}", ln=True, align='C')

        pdf.set_font("Arial", size=10)

        for row in analysis_data["content"]:
            for i, item in enumerate(row):
                if i == 3:  # Commentaire column
                    width = 70
                elif i == 4:  # Suggestion column
                    width = 90
                else:
                    width = 35
                pdf.cell(width, 10, txt=item, border=1)
            pdf.ln(10)

        pdf.add_page()
        self.add_logo(pdf)
        pdf.ln(20)  # Ajouter un espace après le logo
        title = comparison_data["title"]
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, txt=f"{title} - {date_time}", ln=True, align='C')

        pdf.set_font("Arial", size=10)

        for row in comparison_data["content"]:
            for i, item in enumerate(row):
                if i == 3:  # Commentaire column
                    width = 70
                elif i == 4:  # Suggestion column
                    width = 90
                else:
                    width = 35
                pdf.cell(width, 10, txt=item, border=1)
            pdf.ln(10)

        pdf.output("detailed_report.pdf")
        print("Detailed report exported to PDF successfully!")

    def generate_detailed_excel_report(self, analysis_data, comparison_data):
        workbook = xlsxwriter.Workbook("detailed_report.xlsx")
        worksheet = workbook.add_worksheet()

        row = 0
        # Add analysis data
        worksheet.write(row, 0, analysis_data["title"])
        row += 1
        for line in analysis_data["content"]:
            col = 0
            for item in line:
                worksheet.write(row, col, item)
                col += 1
            row += 1

        row += 2  # Add some space between sections
        # Add comparison data
        worksheet.write(row, 0, comparison_data["title"])
        row += 1
        for line in comparison_data["content"]:
            col = 0
            for item in line:
                worksheet.write(row, col, item)
                col += 1
            row += 1

        workbook.close()
        print("Detailed report exported to Excel successfully!")

    def add_logo(self, pdf):
        pdf.image(self.logo_path, 10, 10, 30)  # Position et taille ajustées pour le logo
