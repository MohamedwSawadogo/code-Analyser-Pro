from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QVBoxLayout, QMenu, QHeaderView, QSizePolicy, QApplication
from PySide6.QtCharts import QChart, QLineSeries, QBarSeries, QBarSet, QScatterSeries, QValueAxis 
from PySide6.QtGui import QStandardItemModel, QStandardItem, QAction, QFont
import pandas as pd
from tableau_export import TableauAnalyseWindow
from datetime import datetime
from indexmomo import Ui_MainWindow as MainUI
from dialogue_performances import Ui_Dialog as PerformancesDialog
from dialogue_émissions import Ui_Dialog as EmissionDialog
from dialogue_dynamique import Ui_Dialog as DynamiqueDialog
from classes_performances import DataHandler as PerformanceDataHandler, ReferenceHandler as PerformanceReferenceHandler, PerformanceAnalysis, DataVisualizer as PerformanceDataVisualizer, InputSelectionDialog as PerformanceInputSelectionDialog, OutputSelectionDialog as PerformanceOutputSelectionDialog
from classes_dynamique import DynamicDataHandler, DynamicReferenceHandler, DynamicAnalysis, DynamicDataVisualizer, DynamicInputSelectionDialog, DynamicOutputSelectionDialog
from classes_analyse import EmissionDataHandler, EmissionReferenceHandler, EmissionAnalysis, EmissionDataVisualizer, EmissionInputSelectionDialog, EmissionOutputSelectionDialog
from classes_comparer import DataHandler as ComparisonDataHandler, ComparisonVisualizer, ParameterSelectionDialog, StatisticalAnalysis

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

class DataLoadingThread(QThread):
    data_loaded = Signal(pd.DataFrame)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        try:
            data = pd.read_csv(self.file_path)
            self.data_loaded.emit(data)
        except Exception as e:
            print(f"Error loading data: {e}")
            self.data_loaded.emit(pd.DataFrame())  # Emit empty DataFrame on error
class MainWindowPreparationThread(QThread):
    preparation_complete = Signal()

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        # Effectue des opérations coûteuses ici
        self.main_window.lazy_initialize_handlers('all')
        self.preparation_complete.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Analyser Pro")

        self.ui.stackedWidget.setCurrentIndex(0)
        #self.ui.icon_onky_widget.setHidden(True)
        self.ui.pushButton_50.clicked.connect(self.change_password)
        self.ui.Log_out_2.clicked.connect(self.logout)

        self.selected_input_column = None
        self.selected_output_columns = []
        self.selected_comparison_parameters = []
        self.chart_layout = QVBoxLayout(self.ui.graphicsView)
        self.comparison_chart_layout = QVBoxLayout(self.ui.graphicsView_2)
        self.anomalies = []
        self.comparison_data = []
        self.data = None

        self.units = {
            'Temps': 's',
            'Couple': 'Nm',
            'Puissance': 'HP',
            'RPM': 'tr/min',
            'Conso Carburant': 'L/100km',
            'Température': '°C',
            'Conso Air': 'g/s',
            'CO': 'g/s',
            'HC': 'g/s',
            'PM': 'g/s',
            'NOx': 'g/s',
            'CO_cum': 'g/km',
            'HC_cum': 'g/km',
            'PM_cum': 'g/km',
            'NOx_cum': 'g/km',
            'Accélération': 'm/s²',
            'Vitesse': 'km/h',
            'Temps Accé': 's',
            'Freinage': 'm/s²',
            'Vibration': 'm/s²',
            'Distance': 'km'
        }

        self.performance_reference_handler = None
        self.emission_reference_handler = None
        self.dynamic_reference_handler = None
        self.real_data_handler = None
        self.virtual_data_handler = None

        self.init_ui_connections()

        # Démarrer l'initialisation en arrière-plan
        self.prepare_main_window()

    
    def change_password(self):
        new_password = self.ui.lineEdit_2.text()

        if not new_password:
            QMessageBox.warning(self, "Erreur", "Le mot de passe ne peut pas être vide.")
            return

        # Logic to change the password (replace this with actual backend logic)
        # For demonstration purposes, we'll just show a success message
        success = self.update_password_in_backend(new_password)

        if success:
            QMessageBox.information(self, "Succès", "Le mot de passe a été changé avec succès.")
        else:
            QMessageBox.critical(self, "Erreur", "Échec du changement de mot de passe.")  


    def update_password_in_backend(self, new_password):
        # Replace this with actual logic to update the password in your backend
        # For now, we'll just return True to simulate a successful update
        return True          

    def prepare_main_window(self):
        self.preparation_thread = MainWindowPreparationThread(self)
        self.preparation_thread.preparation_complete.connect(self.on_preparation_complete)
        self.preparation_thread.start()

    def on_preparation_complete(self):
        print("Initialisation complète")

    def init_ui_connections(self):
        self.ui.Home_1.clicked.connect(self.switch_to_home_page)
        self.ui.Home_2.clicked.connect(self.switch_to_home_page)
        self.ui.Data_Analysis.clicked.connect(self.switch_to_Data_Analysis_page)
        self.ui.Data_Comparisons.clicked.connect(self.switch_to_Data_Comparisons_page)
        self.ui.Help_1.clicked.connect(self.switch_to_Help_page)
        self.ui.Help_2.clicked.connect(self.switch_to_Help_page)
        self.ui.Data_Analysis_2.clicked.connect(self.switch_to_Data_Analysis_2_page)
        self.ui.Data_Comparisons_2.clicked.connect(self.switch_to_Data_Comparisons_2_page)
        self.ui.Setting_1.clicked.connect(self.switch_to_Setting_page)
        self.ui.Setting_2.clicked.connect(self.switch_to_Setting_page)
        self.ui.Browse_Files_8.clicked.connect(self.load_data)
        self.ui.Browse_Files_9.clicked.connect(self.load_data)
        self.ui.Browse_Files_18.clicked.connect(self.select_input_data)
        self.ui.Browse_Files_19.clicked.connect(self.select_output_data)
        self.ui.Start_analysis_button_8.clicked.connect(self.plot_data)
        self.ui.Generate_report_button.clicked.connect(self.show_analysis_table)
        self.ui.performance_moteur.clicked.connect(self.open_dialogue_performances)
        self.ui.emissions.clicked.connect(self.open_dialogue_emission)
        self.ui.resistance_force.clicked.connect(self.open_dialogue_dynamique)
        self.ui.Browse_Files_5.clicked.connect(self.load_real_data)
        self.ui.Browse_Files_11.clicked.connect(self.load_virtual_data)
        self.ui.Start_analysis_button_4.clicked.connect(self.select_comparison_parameters)
        self.ui.Start_analysis_button_5.clicked.connect(self.visualize_comparison)
        self.ui.Generate_report_button_2.clicked.connect(self.show_comparison_table)
        self.ui.Analysis_1.clicked.connect(self.analysis_context_menu)

    def logout(self):
        from login_window import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def switch_to_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_Data_Analysis_page(self):
        self.lazy_initialize_handlers('performance')
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_Data_Comparisons_page(self):
        self.lazy_initialize_handlers('comparison')
        self.ui.stackedWidget.setCurrentIndex(3)

    def switch_to_Help_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def switch_to_Data_Analysis_2_page(self):
        self.lazy_initialize_handlers('emission')
        self.ui.stackedWidget.setCurrentIndex(6)

    def switch_to_Data_Comparisons_2_page(self):
        self.lazy_initialize_handlers('dynamic')
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_Setting_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def analysis_context_menu(self):
        self.show_custom_context_menu(self.ui.Analysis_1, ["Banc à rouleaux", "Banc moteur"])

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()
        if text == "Banc à rouleaux":
            self.switch_to_Data_Analysis_page()
        elif text == "Banc moteur":
            self.switch_to_Data_Comparisons_page()

    def load_data(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Fichiers CSV (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.thread = DataLoadingThread(file_path)
            self.thread.data_loaded.connect(self.on_data_loaded)
            self.thread.start()

    def on_data_loaded(self, data):
        try:
            self.data = data
            if self.data.empty or 'Temps' not in self.data.columns:
                QMessageBox.warning(self, "Erreur", "Données invalides ou manquantes.")
            else:
                QMessageBox.information(self, "Succès", "Données chargées avec succès !")
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors du chargement des données : {str(e)}")
        finally:
            QApplication.processEvents()  # Forcer la mise à jour de l'interface utilisateur

    def select_input_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return
        dialog = EmissionInputSelectionDialog(self)
        dialog.set_column_names(self.data.columns)
        if dialog.exec():
            self.selected_input_column = dialog.get_selected_column()
            QMessageBox.information(self, "Colonne d'entrée sélectionnée", f"Colonne sélectionnée : {self.selected_input_column}")

    def select_output_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return
        dialog = EmissionOutputSelectionDialog(self)
        dialog.set_column_names(self.data.columns)
        if dialog.exec():
            self.selected_output_columns = dialog.get_selected_columns()
            QMessageBox.information(self, "Colonnes de sortie sélectionnées", f"Colonnes sélectionnées : {', '.join(self.selected_output_columns)}")

    def plot_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        input_column = self.selected_input_column
        output_columns = self.selected_output_columns

        if not input_column or not output_columns:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les colonnes d'entrée et de sortie d'abord !")
            return

        graph_type = self.ui.comboBox.currentText()
        if graph_type == "Courbe":
            self.plot_line_graph(input_column, output_columns, self.ui.graphicsView_9)
        elif graph_type == "Histogramme":
            self.plot_bar_graph(input_column, output_columns, self.ui.graphicsView_9)
        elif graph_type == "Diagramme de dispersion":
            self.plot_scatter_graph(input_column, output_columns, self.ui.graphicsView_9)

    def plot_line_graph(self, input_column, output_columns, graphics_view):
        chart = QChart()

        for output_column in output_columns:
            series = QLineSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, self.data[output_column][i])
            series.setName(output_column)
            chart.addSeries(series)
        chart.createDefaultAxes()
        axisX = QValueAxis()
        axisX.setTitleText(f"{input_column} ({self.units.get(input_column, '')})")

        y_labels = ", ".join([f"{col} ({self.units.get(col, '')})" for col in output_columns])
        axisY = QValueAxis()
        axisY.setTitleText(y_labels)

        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY, series)
        chart.setTitle(f"Graphique en ligne ({', '.join(output_columns)} en fonction de {input_column})")
        chart.setTitleFont(QFont("Arial", 13, QFont.Bold))

        graphics_view.setChart(chart)

    def plot_bar_graph(self, input_column, output_columns, graphics_view):
        chart = QChart()
        for output_column in output_columns:
            series = QBarSeries()
            bar_set = QBarSet(output_column)
            for value in self.data[output_column]:
                bar_set.append(value)
            series.append(bar_set)
            chart.addSeries(series)
        chart.createDefaultAxes()
        axisX = QValueAxis()
        axisX.setTitleText(f"{input_column} ({self.units.get(input_column, '')})")

        y_labels = ", ".join([f"{col} ({self.units.get(col, '')})" for col in output_columns])
        axisY = QValueAxis()
        axisY.setTitleText(y_labels)

        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY, series)
        chart.setTitle(f"Graphique en barres ({', '.join(output_columns)} en fonction de {input_column})")
        chart.setTitleFont(QFont("Arial", 13, QFont.Bold))
        graphics_view.setChart(chart)

    def plot_scatter_graph(self, input_column, output_columns, graphics_view):
        chart = QChart()
        for output_column in output_columns:
            series = QScatterSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, value)
            series.setName(output_column)
            chart.addSeries(series)
        chart.createDefaultAxes()
        axisX = QValueAxis()
        axisX.setTitleText(f"{input_column} ({self.units.get(input_column, '')})")

        y_labels = ", ".join([f"{col} ({self.units.get(col, '')})" for col in output_columns])
        axisY = QValueAxis()
        axisY.setTitleText(y_labels)

        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY, series)
        chart.setTitle(f"Nuage de points ({', '.join(output_columns)} en fonction de {input_column})")
        chart.setTitleFont(QFont("Arial", 13, QFont.Bold))
        graphics_view.setChart(chart)

    def open_dialogue_performances(self):
        self.lazy_initialize_handlers('performance')
        dialogue = PerformancesDialog(self, self.data)
        dialogue.accepted.connect(self.analyse_par_performance)
        dialogue.exec_()

    def analyse_par_performance(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        input_column = self.selected_input_column
        output_columns = self.selected_output_columns

        if input_column and output_columns:
            analysis = PerformanceAnalysis(self.data, input_column, output_columns, self.performance_reference_handler)
            results, anomalies = analysis.analyze()
            visualizer = PerformanceDataVisualizer(self.data, self.chart_layout)
            visualizer.plot_with_reference(input_column, results)
            self.anomalies = anomalies
            self.populate_table(anomalies, ["Temps", "Paramètre", "Valeur", "Écart (%)", "Correction"])

    def open_dialogue_emission(self):
        self.lazy_initialize_handlers('emission')
        dialogue = EmissionDialog(self, self.data)
        dialogue.accepted.connect(self.analyse_par_emission)
        dialogue.exec_()

    def analyse_par_emission(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        input_column = self.selected_input_column
        output_columns = self.selected_output_columns

        if input_column and output_columns:
            analysis = EmissionAnalysis(self.data, input_column, output_columns, self.emission_reference_handler)
            results, anomalies = analysis.analyze()
            visualizer = EmissionDataVisualizer(self.data, self.chart_layout)
            visualizer.plot_with_reference(input_column, results)
            self.anomalies = anomalies
            self.populate_table(anomalies, ["Temps", "Paramètre", "Valeur", "Écart (%)", "Correction"])

    def open_dialogue_dynamique(self):
        self.lazy_initialize_handlers('dynamic')
        dialogue = DynamiqueDialog(self, self.data)
        dialogue.accepted.connect(self.analyse_par_dynamique)
        dialogue.exec_()

    def analyse_par_dynamique(self):
        if self.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return

        input_column = self.selected_input_column
        output_columns = self.selected_output_columns

        if input_column and output_columns:
            analysis = DynamicAnalysis(self.data, input_column, output_columns, self.dynamic_reference_handler)
            results, anomalies = analysis.analyze()
            visualizer = DynamicDataVisualizer(self.data, self.chart_layout)
            visualizer.plot_with_reference(input_column, results)
            self.anomalies = anomalies
            self.populate_table(anomalies, ["Temps", "Paramètre", "Valeur", "Écart (%)", "Correction"])

    def load_real_data(self):
        self.real_data_handler.load_data()

    def load_virtual_data(self):
        self.virtual_data_handler.load_data()


    def select_comparison_parameters(self):
        if self.real_data_handler.data is not None and self.virtual_data_handler.data is not None:
            dialog = ParameterSelectionDialog(self)
            dialog.set_column_names(self.real_data_handler.data.columns)
            if dialog.exec():
                self.selected_comparison_parameters = dialog.get_selected_columns()
                QMessageBox.information(self, "Paramètres sélectionnés", f"Paramètres sélectionnés : {', '.join(self.selected_comparison_parameters)}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez charger les données réelles et virtuelles d'abord !")

    def visualize_comparison(self):
        if self.selected_comparison_parameters:
            visualizer = ComparisonVisualizer(self.real_data_handler.data, self.virtual_data_handler.data, self.comparison_chart_layout)
            visualizer.plot_comparison(self.selected_comparison_parameters)

            analysis = StatisticalAnalysis(self.real_data_handler.data, self.virtual_data_handler.data)
            self.comparison_data = self.get_comparison_data(analysis, self.selected_comparison_parameters)
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les paramètres à comparer d'abord !")

    def get_comparison_data(self, analysis, parameters):
        comparison_data = []
        for param in parameters:
            stats = analysis.calculate_statistics(param)
            correlation = analysis.calculate_correlation(param)
            conclusion = self.determine_conclusion(stats['error_rel'])

            unit = analysis.units.get(param, '')
            comparison_data.append({
                'Paramètre': param,
                'Moyenne réelle': f"{stats['mean_real']:.4f} {unit}",
                'Moyenne virtuelle': f"{stats['mean_virtual']:.4f} {unit}",
                'Écart moyen (%)': f"{abs(stats['error_rel']):.4f} %",
                'Corrélation': f"{correlation:.4f}",
                'Conclusion': conclusion
            })
        return comparison_data

    def determine_conclusion(self, error_rel):
        if error_rel <= 5:
            return "Fiable"
        elif 5 < error_rel <= 15:
            return "Modérément fiable"
        else:
            return "Peu fiable"

    def show_analysis_table(self):
        if not self.anomalies:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord effectuer une analyse pour obtenir les anomalies.")
            return
        columns = ["Temps", "Paramètre", "Valeur", "Écart (%)", "Correction"]
        table_window = TableauAnalyseWindow(self.anomalies, columns, self)
        table_window.show()

    def show_comparison_table(self):
        if not self.comparison_data:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord effectuer une comparaison pour obtenir les résultats.")
            return
        columns = ["Paramètre", "Moyenne réelle", "Moyenne virtuelle", "Écart moyen (%)", "Corrélation", "Conclusion"]
        table_window = TableauAnalyseWindow(self.comparison_data, columns, self)
        table_window.show()

    def populate_table(self, anomalies, columns):
        model = QStandardItemModel(len(anomalies), len(columns))
        model.setHorizontalHeaderLabels(columns)

        for row, anomaly in enumerate(anomalies):
            for col, column in enumerate(columns):
                model.setItem(row, col, QStandardItem(str(anomaly.get(column, ''))))

        self.ui.tableView.setModel(model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def lazy_initialize_handlers(self, handler_type):
        if handler_type == 'performance' and self.performance_reference_handler is None:
            self.performance_reference_handler = PerformanceReferenceHandler()
        elif handler_type == 'emission' and self.emission_reference_handler is None:
            self.emission_reference_handler = EmissionReferenceHandler()
        elif handler_type == 'dynamic' and self.dynamic_reference_handler is None:
            self.dynamic_reference_handler = DynamicReferenceHandler()
        elif handler_type == 'comparison' and (self.real_data_handler is None or self.virtual_data_handler is None):
            self.real_data_handler = DynamicDataHandler()
            self.virtual_data_handler = DynamicDataHandler()
        elif handler_type == 'all':
            self.performance_reference_handler = PerformanceReferenceHandler()
            self.emission_reference_handler = EmissionReferenceHandler()
            self.dynamic_reference_handler = DynamicReferenceHandler()
            self.real_data_handler = DynamicDataHandler()
            self.virtual_data_handler = DynamicDataHandler()
