from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QVBoxLayout, QPushButton, QDialog, QMessageBox, QComboBox
from PySide6.QtGui import QColor, QPalette
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fenêtre principale")
        self.setGeometry(100, 100, 800, 600)

        self.load_data_button = QPushButton("Charger les données", self)
        self.load_data_button.clicked.connect(self.load_data)
        self.load_data_button.setGeometry(50, 50, 200, 50)

        self.select_input_button = QPushButton("Sélectionner l'entrée", self)
        self.select_input_button.clicked.connect(self.select_input_data)
        self.select_input_button.setGeometry(50, 100, 200, 50)

        self.select_output_button = QPushButton("Sélectionner les sorties", self)
        self.select_output_button.clicked.connect(self.select_output_data)
        self.select_output_button.setGeometry(50, 150, 200, 50)

        self.visualize_button = QPushButton("Visualiser", self)
        self.visualize_button.clicked.connect(self.plot_data)
        self.visualize_button.setGeometry(50, 200, 200, 50)

        self.graph_type_combo = QComboBox(self)
        self.graph_type_combo.addItems(["Graphique en ligne", "Graphique en barres", "Nuage de points"])
        self.graph_type_combo.setGeometry(50, 250, 200, 50)

        self.data = None
        self.selected_input_column = None
        self.selected_output_columns = []

    def load_data(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Fichiers CSV (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            try:
                self.data = pd.read_csv(file_path)
                QMessageBox.information(self, "Succès", "Données chargées avec succès !")
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"Erreur lors du chargement des données : {str(e)}")

    def select_input_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        column_names = self.data.columns.tolist()
        dialog = InputSelectionDialog(self)
        dialog.set_column_names(column_names)
        if dialog.exec_():
            self.selected_input_column = dialog.get_selected_column()
            if self.selected_input_column:
                QMessageBox.information(self, "Colonne d'entrée sélectionnée", f"Colonne sélectionnée : {self.selected_input_column}")

    def select_output_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        column_names = self.data.columns.tolist()
        dialog = OutputSelectionDialog(self)
        dialog.set_column_names(column_names)
        if dialog.exec_():
            self.selected_output_columns = dialog.get_selected_columns()
            if self.selected_output_columns:
                QMessageBox.information(self, "Colonne(s) de sortie sélectionnée(s)", f"Colonnes sélectionnées : {', '.join(self.selected_output_columns)}")

    def plot_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        input_column = self.selected_input_column
        output_columns = self.selected_output_columns

        if not input_column or not output_columns:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les colonnes d'entrée et de sortie d'abord !")
            return

        # Plot data based on selected graph type
        graph_type = self.graph_type_combo.currentText()

        if graph_type == "Graphique en ligne":
            self.plot_line_graph(input_column, output_columns)
        elif graph_type == "Graphique en barres":
            self.plot_bar_graph(input_column, output_columns)
        elif graph_type == "Nuage de points":
            self.plot_scatter_graph(input_column, output_columns)

    def plot_line_graph(self, input_column, output_columns):
        plt.figure(figsize=(10, 6))
        for output_column in output_columns:
            plt.plot(self.data[input_column], self.data[output_column], label=output_column)

        plt.xlabel(input_column)
        plt.ylabel(', '.join(output_columns))
        plt.title("Graphique en ligne",  fontweight='bold')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_bar_graph(self, input_column, output_columns):
        plt.figure(figsize=(10, 6))
        width = 0.2
        for i, output_column in enumerate(output_columns):
            plt.bar(self.data[input_column] + i * width, self.data[output_column], width=width, label=output_column)

        plt.xlabel(input_column)
        plt.ylabel(', '.join(output_columns))
        plt.title("Graphique en barres",  fontweight='bold')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_scatter_graph(self, input_column, output_columns):
        plt.figure(figsize=(10, 6))
        for output_column in output_columns:
            plt.scatter(self.data[input_column], self.data[output_column], label=output_column)

        plt.xlabel(input_column)
        plt.ylabel(', '.join(output_columns))
        plt.title("Nuage de points",  fontweight='bold')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
