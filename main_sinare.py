import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFileDialog, QListWidget, QDialog, QDialogButtonBox, QLabel, QTableWidget, QTableWidgetItem, QSpacerItem, QSizePolicy, QMessageBox, QComboBox
from PySide6.QtCore import Qt
import analysis  # Importer le fichier analysis.py
import pandas as pd
from fpdf import FPDF
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Analyse des Émissions")

        # Main layout
        main_layout = QHBoxLayout()

        # Left panel for buttons
        button_layout = QVBoxLayout()

        self.import_button = QPushButton("Importer")
        self.import_button.clicked.connect(self.import_file)

        self.x_axis_button = QPushButton("Choisir l'axe des X")
        self.x_axis_button.clicked.connect(self.choose_x_axis)

        self.y_axis_button = QPushButton("Choisir l'axe des Y")
        self.y_axis_button.clicked.connect(self.choose_y_axis)

        self.analyze_button = QPushButton("Analyser")
        self.analyze_button.clicked.connect(self.analyze_data)

        self.export_button = QPushButton("Exporter")
        self.export_button.clicked.connect(self.export_data)

        button_layout.addWidget(self.import_button)
        button_layout.addWidget(self.x_axis_button)
        button_layout.addWidget(self.y_axis_button)
        button_layout.addWidget(self.analyze_button)
        button_layout.addWidget(self.export_button)
        button_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Right panel for graphs and table
        self.graph_widget = QWidget()
        self.graph_layout = QVBoxLayout()
        self.graph_widget.setLayout(self.graph_layout)

        self.table_widget = QTableWidget()  # Table vide, nous allons la remplir dynamiquement
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["Temps", "Polluant", "Valeur", "Écart (%)", "Commentaire", "Correction"])

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.graph_widget, stretch=2)
        right_layout.addWidget(self.table_widget, stretch=1)

        main_layout.addLayout(button_layout)
        main_layout.addLayout(right_layout)

        # Main widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Placeholder for file path and selected axes
        self.file_path = ""
        self.x_axis = ""
        self.y_axes = []

    def import_file(self):
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName(self, "Importer le fichier CSV", "", "CSV Files (*.csv)")
        if self.file_path:
            QMessageBox.information(self, "Importation réussie", f"Fichier importé : {self.file_path}")

    def choose_x_axis(self):
        if not self.file_path:
            QMessageBox.warning(self, "Attention", "Veuillez d'abord importer un fichier CSV.")
            return
        dialog = AxisSelectionDialog(self.file_path, single_selection=True)
        if dialog.exec():
            self.x_axis = dialog.selected_axis
            QMessageBox.information(self, "Axe X sélectionné", f"Axe X sélectionné : {self.x_axis}")

    def choose_y_axis(self):
        if not self.file_path:
            QMessageBox.warning(self, "Attention", "Veuillez d'abord importer un fichier CSV.")
            return
        dialog = AxisSelectionDialog(self.file_path, single_selection=False)
        if dialog.exec():
            self.y_axes = dialog.selected_axes
            QMessageBox.information(self, "Axes Y sélectionnés", f"Axe(s) Y sélectionné(s) : {', '.join(self.y_axes)}")

    def analyze_data(self):
        if not self.file_path or not self.x_axis or not self.y_axes:
            QMessageBox.warning(self, "Attention", "Veuillez importer un fichier et sélectionner les axes X et Y.")
            return

        # Nettoyer l'ancien graphique
        self.clear_layout(self.graph_layout)

        # Générer les nouveaux graphiques
        canvas = analysis.generate_graphs(self.file_path, self.x_axis, self.y_axes)
        self.graph_layout.addWidget(canvas)

        # Analyse des anomalies et mise à jour du tableau
        data = analysis.import_data(self.file_path)
        anomalies = analysis.calculate_anomalies_and_generate_report(data, self.x_axis, self.y_axes)

        self.table_widget.setRowCount(len(anomalies))

        for row_idx, anomaly in enumerate(anomalies):
            self.table_widget.setItem(row_idx, 0, QTableWidgetItem(str(anomaly['Temps'])))
            self.table_widget.setItem(row_idx, 1, QTableWidgetItem(anomaly['Polluant']))
            self.table_widget.setItem(row_idx, 2, QTableWidgetItem(f"{anomaly['Valeur']:.2f}"))
            self.table_widget.setItem(row_idx, 3, QTableWidgetItem(f"{anomaly['Écart (%)']:.2f}"))
            self.table_widget.setItem(row_idx, 4, QTableWidgetItem(anomaly['Commentaire']))
            self.table_widget.setItem(row_idx, 5, QTableWidgetItem(anomaly['Correction']))

        # Ajuster la largeur des colonnes pour mieux afficher les commentaires et corrections
        self.table_widget.setColumnWidth(4, 240)
        self.table_widget.setColumnWidth(5, 240)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

    def export_data(self):
        export_dialog = ExportDialog()
        if export_dialog.exec():
            format_selected = export_dialog.get_format_selected()
            if format_selected:
                if format_selected == "Excel":
                    self.export_to_excel()
                elif format_selected == "PDF":
                    self.export_to_pdf()

    def export_to_excel(self):
        path, _ = QFileDialog.getSaveFileName(self, "Enregistrer sous", "", "Excel Files (*.xlsx)")
        if path:
            data = self.get_table_data()
            df = pd.DataFrame(data, columns=["Temps", "Polluant", "Valeur", "Écart (%)", "Commentaire", "Correction"])
            with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Analyse des Emissions')
                worksheet = writer.sheets['Analyse des Emissions']
                worksheet.set_column('A:F', 20)
                worksheet.set_column('E:E', 120)
                worksheet.set_column('F:F', 120)
                worksheet.write('A1', 'Analyse des Emissions', writer.book.add_format({'bold': True, 'font_size': 14}))
                worksheet.write('A2', f"Date d'exportation : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            QMessageBox.information(self, "Exportation réussie", f"Données exportées avec succès vers {path}")

    def export_to_pdf(self):
        path, _ = QFileDialog.getSaveFileName(self, "Enregistrer sous", "", "PDF Files (*.pdf)")
        if path:
            data = self.get_table_data()
            title = "Analyse des Émissions"
            analysis.export_to_pdf(data, path, title)
            QMessageBox.information(self, "Exportation réussie", f"Données exportées avec succès vers {path}")

    def get_table_data(self):
        data = []
        for row in range(self.table_widget.rowCount()):
            row_data = []
            for column in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            data.append(row_data)
        return data

class AxisSelectionDialog(QDialog):
    def __init__(self, file_path, single_selection=True):
        super().__init__()
        self.setWindowTitle("Choisir les axes")
        self.selected_axis = ""
        self.selected_axes = []

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SingleSelection if single_selection else QListWidget.MultiSelection)
        layout.addWidget(self.list_widget)

        # Load the column names from the CSV file
        df = pd.read_csv(file_path)
        for col in df.columns:
            self.list_widget.addItem(col)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def accept(self):
        if self.list_widget.selectedItems():
            if self.list_widget.selectionMode() == QListWidget.SingleSelection:
                self.selected_axis = self.list_widget.selectedItems()[0].text()
            else:
                self.selected_axes = [item.text() for item in self.list_widget.selectedItems()]
        super().accept()

class ExportDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choisir le format d'exportation")
        layout = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Excel", "PDF"])
        layout.addWidget(QLabel("Sélectionnez le format d'exportation :"))
        layout.addWidget(self.combo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_format_selected(self):
        return self.combo.currentText()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

