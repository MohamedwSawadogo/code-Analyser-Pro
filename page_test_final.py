import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QVBoxLayout, QMenu, QHeaderView
from PySide6.QtCharts import QChart, QLineSeries, QBarSeries, QScatterSeries
from PySide6.QtGui import QStandardItemModel, QStandardItem, QAction, Qt,  QFont
from indexmomo import Ui_MainWindow
from dialogue_performances import Ui_Dialog as PerformancesDialog
from dialogue_émissions import Ui_Dialog as EmissionDialog
from dialogue_dynamique import Ui_Dialog as DynamiqueDialog
from tableau_export import TableauAnalyseWindow, DataExporter
from classes_performances import DataHandler as PerformanceDataHandler, ReferenceHandler as PerformanceReferenceHandler, PerformanceAnalysis, DataVisualizer as PerformanceDataVisualizer, InputSelectionDialog as PerformanceInputSelectionDialog, OutputSelectionDialog as PerformanceOutputSelectionDialog
from classes_dynamique import DynamicDataHandler, DynamicReferenceHandler, DynamicAnalysis, DynamicDataVisualizer, DynamicInputSelectionDialog, DynamicOutputSelectionDialog
from classes_analyse import EmissionDataHandler, EmissionReferenceHandler, EmissionAnalysis, EmissionDataVisualizer, EmissionInputSelectionDialog, EmissionOutputSelectionDialog
from classes_comparer import DataHandler as ComparisonDataHandler, ComparisonVisualizer, ParameterSelectionDialog, StatisticalAnalysis

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        
        # Handlers for different types of analysis
        self.performance_data_handler = PerformanceDataHandler()
        self.performance_reference_handler = PerformanceReferenceHandler()
        self.emission_data_handler = EmissionDataHandler()
        self.emission_reference_handler = EmissionReferenceHandler()
        self.dynamic_data_handler = DynamicDataHandler()
        self.dynamic_reference_handler = DynamicReferenceHandler()
        
        self.real_data_handler = ComparisonDataHandler()
        self.virtual_data_handler = ComparisonDataHandler()

        self.selected_input_column = None
        self.selected_output_columns = []
        self.selected_comparison_parameters = []
        self.chart_layout = QVBoxLayout(self.graphicsView)
        self.comparison_chart_layout = QVBoxLayout(self.graphicsView_2)
        self.anomalies = []
        self.comparison_data = []
        self.data = None

        # Connexion des boutons aux méthodes
        self.Home_1.clicked.connect(self.switch_to_home_page)
        self.Home_2.clicked.connect(self.switch_to_home_page)
        self.Data_Analysis.clicked.connect(self.switch_to_Data_Analysis_page)
        self.Data_Comparisons.clicked.connect(self.switch_to_Data_Comparisons_page)
        self.Help_1.clicked.connect(self.switch_to_Help_page)
        self.Help_2.clicked.connect(self.switch_to_Help_page)
        self.Data_Analysis_2.clicked.connect(self.switch_to_Data_Analysis_2_page)
        self.Data_Comparisons_2.clicked.connect(self.switch_to_Data_Comparisons_2_page)
        self.Setting_1.clicked.connect(self.switch_to_Setting_page)
        self.Setting_2.clicked.connect(self.switch_to_Setting_page)
        self.Browse_Files_8.clicked.connect(self.load_data)
        self.Browse_Files_9.clicked.connect(self.load_data)
        self.Browse_Files_18.clicked.connect(self.select_input_data)
        self.Browse_Files_19.clicked.connect(self.select_output_data)
        self.Start_analysis_button_8.clicked.connect(self.plot_data)

        self.Generate_report_button.clicked.connect(self.show_analysis_table)
      
        self.performance_moteur.clicked.connect(self.open_dialogue_performances)
        self.emissions.clicked.connect(self.open_dialogue_emission)
        self.resistance_force.clicked.connect(self.open_dialogue_dynamique)
        self.Browse_Files_5.clicked.connect(self.load_real_data)
        self.Browse_Files_11.clicked.connect(self.load_virtual_data)
        self.Start_analysis_button_4.clicked.connect(self.select_comparison_parameters)
        self.Start_analysis_button_5.clicked.connect(self.visualize_comparison)
        self.Generate_report_button_2.clicked.connect(self.show_comparison_table)

        self.Analysis_1.clicked.connect(self.analysis_context_menu)

    def switch_to_home_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_Data_Analysis_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_Data_Comparisons_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_Help_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_Data_Analysis_2_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_Data_Comparisons_2_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_Setting_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def analysis_context_menu(self):
        self.show_custom_context_menu(self.Analysis_1, ["Banc à rouleaux", "Banc moteur"])

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
            try:
                self.data = pd.read_csv(file_path)
                if self.data.empty or 'Temps' not in self.data.columns:
                    QMessageBox.warning(self, "Erreur", "Données invalides ou manquantes.")
                else:
                    QMessageBox.information(self, "Succès", "Données chargées avec succès !")
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"Erreur lors du chargement des données : {str(e)}")

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

        graph_type = self.comboBox.currentText()
        if graph_type == "Courbe":
            self.plot_line_graph(input_column, output_columns, self.graphicsView_9)
        elif graph_type == "Histogramme":
            self.plot_bar_graph(input_column, output_columns, self.graphicsView_9)
        elif graph_type == "Diagramme de dispersion":
            self.plot_scatter_graph(input_column, output_columns, self.graphicsView_9)

    def plot_line_graph(self, input_column, output_columns, graphics_view):
        chart = QChart()
        chart.setTitle(f"Graphique en ligne (Ordonné en fonction de {input_column})")
        for output_column in output_columns:
            series = QLineSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, self.data[output_column][i])
            series.setName(output_column)
            chart.addSeries(series)
        chart.createDefaultAxes()
        chart.legend().setAlignment(Qt.AlignBottom)
        graphics_view.setChart(chart)



    def plot_bar_graph(self, input_column, output_columns, graphics_view):
        chart = QChart()
        chart.setTitle(f"Graphique en barres (Ordonné en fonction de {input_column})")
        for output_column in output_columns:
            series = QBarSeries()
            bar_set = series.append(output_column)
            for i, value in enumerate(self.data[output_column]):
                bar_set.append(value)
            chart.addSeries(series)
        chart.createDefaultAxes()
        chart.legend().setAlignment(Qt.AlignBottom)
        graphics_view.setChart(chart)

    def plot_scatter_graph(self, input_column, output_columns, graphics_view):
        chart = QChart()
        chart.setTitle(f"Nuage de points (Ordonné en fonction de {input_column})")
        for output_column in output_columns:
            series = QScatterSeries()
            for i, value in enumerate(self.data[input_column]):
                series.append(i, value)
            series.setName(output_column)
            chart.addSeries(series)
        chart.createDefaultAxes()
        chart.legend().setAlignment(Qt.AlignBottom)
        graphics_view.setChart(chart)

    def open_dialogue_performances(self):
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
            self.populate_table(anomalies, ["Temps", "Paramètre/Polluant", "Valeur", "Écart (%)", "Correction"])

    def open_dialogue_dynamique(self):
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
        self.real_data_handler.load_data("Données réelles")

    def load_virtual_data(self):
        self.virtual_data_handler.load_data("Données virtuelles")

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

            comparison_data.append({
                'Paramètre': param,
                'Moyenne réelle': f"{stats['mean_real']:.2f}",
                'Moyenne virtuelle': f"{stats['mean_virtual']:.2f}",
                'Écart moyen (%)': f"{stats['error_rel']:.2f} %",
                'Corrélation': f"{correlation:.2f}",
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

if __name__ == "__main__":
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()
