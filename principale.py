from ui_principale import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QVBoxLayout, QPushButton, QDialog, QMessageBox, QComboBox, QSizePolicy 
from PySide6.QtGui import QPainter
from PySide6.QtGui import QFont
import pandas as pd
from PySide6 import QtCharts
from dialogue_performances import Ui_Dialog as PerformancesDialog
from dialogue_émissions import Ui_Dialog as EmissionDialog
from dialogue_dynamique import Ui_Dialog as DynamiqueDialog  

from PySide6.QtCharts import QChartView

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


class Myprincipale(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Fenêtre Principale")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setGeometry(100, 100, 400, 300)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1200, 900)

        self.widget_2.setHidden(True)
        self.frame.setHidden(True)
        self.frame_4.setHidden(True)
        self.data = None
        self.selected_input_column = None
        self.selected_output_columns = []

        self.pushButton.clicked.connect(self.switch_to_AccueilPage)
        self.pushButton_2.clicked.connect(self.switch_to_AccueilPage)
        self.pushButton_15.clicked.connect(self.switch_to_rouleauxPage)
        self.pushButton_16.clicked.connect(self.switch_to_moteurPage)
        self.pushButton_4.clicked.connect(self.switch_to_VisualisationPage)
        self.pushButton_9.clicked.connect(self.switch_to_VisualisationPage)
        self.pushButton_17.clicked.connect(self.switch_to_AnalyserPage)
        self.pushButton_18.clicked.connect(self.switch_to_ComparerPage)
        self.pushButton_6.clicked.connect(self.switch_to_ExporterPage)
        self.pushButton_11.clicked.connect(self.switch_to_ExporterPage)
        self.pushButton_8.clicked.connect(self.switch_to_ParamètresPage)
        self.pushButton_13.clicked.connect(self.switch_to_ParamètresPage)
        self.pushButton_32.clicked.connect(self.open_dialogue_performances)
        self.pushButton_33.clicked.connect(self.open_dialogue_emission)
        self.pushButton_34.clicked.connect(self.open_dialogue_dynamique)  # Connecter le bouton pour ouvrir le dialogue dynamique

    def switch_to_AccueilPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_rouleauxPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_moteurPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_VisualisationPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_AnalyserPage(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_ComparerPage(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_ExporterPage(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_ParamètresPage(self):
        self.stackedWidget.setCurrentIndex(7)

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

        graph_type = self.comboBox.currentText()
        if graph_type == "Courbe":
            self.plot_line_graph(input_column, output_columns)
        elif graph_type == "Histogramme":
            self.plot_bar_graph(input_column, output_columns)
        elif graph_type == "Diagramme de dispersion":
            self.plot_scatter_graph(input_column, output_columns)

    def plot_line_graph(self, input_column, output_columns):
        chart = QtCharts.QChart()
        chart.setTitle("Graphique en ligne")

        for output_column in output_columns:
            series = QtCharts.QLineSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, self.data[output_column][i])

            series.setName(output_column)
            chart.addSeries(series)

        chart.createDefaultAxes()
        self.display_chart(chart)

    def plot_bar_graph(self, input_column, output_columns):
        chart = QtCharts.QChart()
        chart.setTitle("Graphique en barres")

        for output_column in output_columns:
            series = QtCharts.QBarSeries()
            for i, value in enumerate(self.data[input_column]):
                bar_set = QtCharts.QBarSet(output_column)
                bar_set.append(value)
                series.append(bar_set)

            series.setName(output_column)
            chart.addSeries(series)

        chart.createDefaultAxes()
        self.display_chart(chart)

    def plot_scatter_graph(self, input_column, output_columns):
        chart = QtCharts.QChart()
        chart.setTitle("Nuage de points")

        for output_column in output_columns:
            series = QtCharts.QScatterSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, value)
            series.setName(output_column)
            chart.addSeries(series)

        chart.createDefaultAxes()
        self.display_chart(chart)

    def display_chart(self, chart):
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setChart(chart)

    def open_dialogue_performances(self):
        from dialogue_performances import Ui_Dialog as PerformancesDialog

        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        dialogue = PerformancesDialog(self, self.data)
        dialogue.exec_()

    def open_dialogue_emission(self):
        from dialogue_émissions import Ui_Dialog as EmissionDialog

        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        dialogue = EmissionDialog(self, self.data)
        dialogue.exec_()

    def open_dialogue_dynamique(self):
        from dialogue_dynamique import Ui_Dialog as DynamiqueDialog

        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        dialogue = DynamiqueDialog(self, self.data)
        dialogue.exec_()

    def plot_line_graph_analyse(self, input_column, output_columns, graphic_view):
        chart = QtCharts.QChart()
        chart.setTitle("Graphique en ligne")

        for output_column in output_columns:
            series = QtCharts.QLineSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, self.data[output_column][i])

            series.setName(output_column)
            chart.addSeries(series)

        chart.createDefaultAxes()
        self.display_chart_analyse(chart, graphic_view)

    def plot_bar_graph_analyse(self, input_column, output_columns, graphic_view):
        chart = QtCharts.QChart()
        chart.setTitle("Graphique en barres")

        for output_column in output_columns:
            series = QtCharts.QBarSeries()
            for i, value in enumerate(self.data[input_column]):
                bar_set = QtCharts.QBarSet(output_column)
                bar_set.append(value)
                series.append(bar_set)

            series.setName(output_column)
            chart.addSeries(series)

        chart.createDefaultAxes()
        self.display_chart_analyse(chart, graphic_view)

    def plot_scatter_graph_analyse(self, input_column, output_columns, graphic_view):
        chart = QtCharts.QChart()
        chart.setTitle("Nuage de points")

        for output_column in output_columns:
            series = QtCharts.QScatterSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, value)
            series.setName(output_column)
            chart.addSeries(series)

        chart.createDefaultAxes()
        self.display_chart_analyse(chart, graphic_view)

    def display_chart_analyse(self, chart, graphic_view):
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        graphic_view.setChart(chart)

if __name__ == "__main__":
    app = QApplication([])
    window = Myprincipale()
    window.show()
    app.exec()
