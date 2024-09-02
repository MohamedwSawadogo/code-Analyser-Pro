import pandas as pd
from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QListWidget, QPushButton
import scipy.io

class DataHandler:
    def __init__(self):
        self.data_real = None
        self.data_virtual = None

    def load_real_data(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Fichiers CSV (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                self.data_real = pd.read_csv(file_path)
                QMessageBox.information(None, "Succès", "Données réelles chargées avec succès !")
            except Exception as e:
                QMessageBox.warning(None, "Erreur", f"Erreur lors du chargement des données réelles : {str(e)}")

    def load_virtual_data(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Fichiers MATLAB (*.mat);;Fichiers CSV (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            try:
                if file_path.endswith('.mat'):
                    mat = scipy.io.loadmat(file_path)
                    self.data_virtual = pd.DataFrame(mat['data'])  # Assurez-vous que le format est correct
                else:
                    self.data_virtual = pd.read_csv(file_path)
                QMessageBox.information(None, "Succès", "Données virtuelles chargées avec succès !")
            except Exception as e:
                QMessageBox.warning(None, "Erreur", f"Erreur lors du chargement des données virtuelles : {str(e)}")

    def compare_data(self, parameters):
        comparison_results = []
        for param in parameters:
            if param in self.data_real.columns and param in self.data_virtual.columns:
                real_values = self.data_real[param]
                virtual_values = self.data_virtual[param]
                ecart = real_values - virtual_values
                ecart_percent = (ecart / real_values) * 100
                comparison_results.append({
                    'param': param,
                    'mean_real': real_values.mean(),
                    'mean_virtual': virtual_values.mean(),
                    'ecart_mean': ecart.mean(),
                    'ecart_percent_mean': ecart_percent.mean()
                })
        return comparison_results

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
