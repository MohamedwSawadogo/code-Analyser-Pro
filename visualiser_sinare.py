import sys
import pandas as pd
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFileDialog, QListWidget, QDialog, QDialogButtonBox, QLabel, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Dictionnaire des unités pour chaque colonne
UNITS = {
    'date': 'Date et heure',
    'time': 's',
    'trip': 'Identifiant du trajet',
    'driver': 'Numéro du conducteur',
    'route': 'Numéro de la route',
    'load': 'kg',
    'coldStart': 'Indicateur',
    'gps_lat': 'degrés décimaux',
    'gps_lon': 'degrés décimaux',
    'gps_alt': 'm',
    'gps_speed': 'km/h',
    'humidity': '%HR',
    'pressure': 'mbar',
    'temp': '°C',
    'rpm': 'rpm',
    'speed_vehicle': 'km/h',
    'throttle': '%',
    'manifold_pressure': 'kPa',
    'manifold_temp': '°C',
    'coolant_temp': '°C',
    'fuel_flow': 'g/s',
    'fuel_rate': 'gal/s',
    'air_fuel_ratio': 'Ratio',
    'exh_humidity': '%',
    'exh_mass_flow': 'kg/h',
    'exh_flow_scfm': 'SCFM',
    'exh_flow_ls': 'L/s',
    'exh_temp': '°C',
    'CO2_amb_conc': '%',
    'CO_amb_conc': '%',
    'NO_amb_conc': 'ppm',
    'NO2_amb_conc': 'ppm',
    'O2_amb_conc': '%',
    'CO2_wet_conc': '%',
    'CO_wet_conc': '%',
    'NO_wet_conc': 'ppm',
    'NO2_wet_conc': 'ppm',
    'NOx_wet_conc': 'ppm',
    'O2_wet_conc': '%',
    'CO2_mass': 'g/s',
    'CO_mass': 'g/s',
    'NO_mass': 'g/s',
    'NO2_mass': 'g/s',
    'NOx_mass': 'g/s',
    'O2_mass': 'g/s',
    'NO_mass_cor': 'g/s',
    'NO2_mass_cor': 'g/s',
    'NOx_mass_cor': 'g/s'
}

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def get_unit(self, column):
        return UNITS.get(column, '')

    def plot_data(self, x_axis, y_axes):
        fig, ax = plt.subplots()
        for y_axis in y_axes:
            ax.plot(self.data[x_axis], self.data[y_axis], label=y_axis)
        x_unit = self.get_unit(x_axis)
        y_units = [self.get_unit(y_axis) for y_axis in y_axes]
        ax.set_xlabel(f'{x_axis} ({x_unit})')
        ax.set_ylabel(', '.join([f'{y_axis} ({unit})' for y_axis, unit in zip(y_axes, y_units)]))
        ax.set_title(f'Visualisation des Données : {", ".join(y_axes)} en fonction de {x_axis}', fontweight='bold')
        ax.legend()
        canvas = FigureCanvas(fig)
        return canvas

class VisualizationWindow(QMainWindow):
    def __init__(self):
        super(VisualizationWindow, self).__init__()

        self.setWindowTitle("Visualisation des Données")

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

        self.visualize_button = QPushButton("Visualiser")
        self.visualize_button.clicked.connect(self.visualize_data)

        button_layout.addWidget(self.import_button)
        button_layout.addWidget(self.x_axis_button)
        button_layout.addWidget(self.y_axis_button)
        button_layout.addWidget(self.visualize_button)
        button_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Right panel for graphs
        self.graph_widget = QWidget()
        self.graph_layout = QVBoxLayout()
        self.graph_widget.setLayout(self.graph_layout)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.graph_widget, stretch=2)

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

    def visualize_data(self):
        if not self.file_path or not self.x_axis or not self.y_axes:
            QMessageBox.warning(self, "Attention", "Veuillez importer un fichier et sélectionner les axes X et Y.")
            return

        # Nettoyer l'ancien graphique
        self.clear_layout(self.graph_layout)

        # Générer la visualisation
        data = pd.read_csv(self.file_path)
        visualizer = DataVisualizer(data)
        canvas = visualizer.plot_data(self.x_axis, self.y_axes)
        self.graph_layout.addWidget(canvas)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = VisualizationWindow()
    window.show()

    sys.exit(app.exec())
