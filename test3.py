# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogue_performances.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from principale import plot_data  # Importer la fonction directement


from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QVBoxLayout, QPushButton, QDialog, QMessageBox, QComboBox, QSizePolicy 
from PySide6.QtGui import QColor, QPalette
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PySide6.QtCharts import QChartView
from PySide6 import QtCharts

from PySide6.QtGui import QPainter







from principale import Myprincipale
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)



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





class Ui_Dialog(QDialog):
   
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 353)
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 40, 311, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 271, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton_300 = QPushButton(self)
        self.pushButton_300.clicked.connect(self.plot_data)
        self.pushButton_300.setObjectName(u"pushButton_30")
        self.pushButton_300.setGeometry(QRect(10, 290, 371, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton_300.setFont(font1)
        self.pushButton_300.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_311 = QPushButton(self)
        self.pushButton_311.clicked.connect(self.select_input_data)
        self.pushButton_311.setObjectName(u"pushButton_31")
        self.pushButton_311.setGeometry(QRect(10, 130, 379, 26))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton_311.setFont(font2)
        self.pushButton_311.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"	background-color: rgb(0, 85, 127);\n"
"\n"
"}")
        self.pushButton_322 = QPushButton(self)
        self.pushButton_322.clicked.connect(self.select_output_data)
        self.pushButton_322.setObjectName(u"pushButton_32")
        self.pushButton_322.setGeometry(QRect(10, 70, 379, 26))
        self.pushButton_322.setFont(font2)
        self.pushButton_322.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"	background-color: rgb(0, 85, 127);\n"
"\n"
"}")
        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 190, 381, 71))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_333 = QPushButton(self.layoutWidget_2)
        self.pushButton_333.setObjectName(u"pushButton_33")
        self.pushButton_333.setFont(font2)
        self.pushButton_333.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"	background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_12.addWidget(self.pushButton_333)

        self.comboBox_2 = QComboBox(self.layoutWidget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.comboBox_2.setFont(font3)

        self.verticalLayout_12.addWidget(self.comboBox_2)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

        self.data = None
        self.selected_input_column = None
        self.selected_output_columns = []





    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Performances du Moteur", None))
        self.pushButton_300.setText(QCoreApplication.translate("Dialog", u"Analyser", None))
        self.pushButton_311.setText(QCoreApplication.translate("Dialog", u"Choisir le facteur d'analyser", None))
        self.pushButton_322.setText(QCoreApplication.translate("Dialog", u"Choisir la performance \u00e0 analyser", None))
        self.pushButton_333.setText(QCoreApplication.translate("Dialog", u"Choisir le type de graphe", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Courbe", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Histogramme", None))

    # retranslateUi








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
        graph_type = self.comboBox.currentText()

        if graph_type == "Courbe":
            self.plot_line_graph(input_column, output_columns)
        elif graph_type == "Histogramme":
            self.plot_bar_graph(input_column, output_columns)
        elif graph_type == "Diagramme de dispersion":
            self.plot_scatter_graph(input_column, output_columns)

