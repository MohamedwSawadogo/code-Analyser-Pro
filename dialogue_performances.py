# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogue_performances.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont, QCloseEvent
from PySide6.QtWidgets import QApplication, QDialog, QFrame, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox,QComboBox
from classes_performances import DataVisualizer, PerformanceAnalysis
 
class Ui_Dialog(QDialog):
    def __init__(self, main_window, data, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.main_window = main_window
        self.data = data
       
        self.setupUi(self)
        self.setWindowTitle("Analyse des performances")
       
        self.pushButton_30.clicked.connect(self.analyze_data)
        self.pushButton_31.clicked.connect(self.open_input_selection_dialog)
        self.pushButton_32.clicked.connect(self.open_output_selection_dialog)



    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(395, 266)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 40, 361, 16))
        self.line.setMinimumSize(QSize(311, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 361, 31))
        self.label.setMinimumSize(QSize(331, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton_30 = QPushButton(Dialog)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(10, 210, 381, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton_30.setFont(font1)
        self.pushButton_30.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_31 = QPushButton(Dialog)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(10, 140, 379, 41))
        self.pushButton_31.setMinimumSize(QSize(0, 41))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton_31.setFont(font2)
        self.pushButton_31.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"	background-color: rgb(0, 85, 127);\n"
"\n"
"}")
        self.pushButton_32 = QPushButton(Dialog)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(10, 70, 379, 41))
        self.pushButton_32.setMinimumSize(QSize(0, 41))
        self.pushButton_32.setFont(font2)
        self.pushButton_32.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"	background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Performances du Moteur", None))
        self.pushButton_30.setText(QCoreApplication.translate("Dialog", u"Analyser", None))
        self.pushButton_31.setText(QCoreApplication.translate("Dialog", u"Choisir le facteur d'analyse", None))
        self.pushButton_32.setText(QCoreApplication.translate("Dialog", u"Choisir la performance \u00e0 analyser", None))
    # retranslateUi


     
    def open_input_selection_dialog(self):
        self.main_window.select_input_data()
 
    def open_output_selection_dialog(self):
        self.main_window.select_output_data()
 
    def analyze_data(self):
        if self.main_window.data is None:
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord charger les données !")
            return
 
        input_column = self.main_window.selected_input_column
        output_columns = self.main_window.selected_output_columns
 
        if not input_column or not output_columns:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner les colonnes d'entrée et de sortie d'abord !")
            return
 
        analysis = PerformanceAnalysis(self.main_window.data, input_column, output_columns, self.main_window.performance_reference_handler)
        results, anomalies = analysis.analyze()
        visualizer = DataVisualizer(self.main_window.data, self.main_window.chart_layout)
        visualizer.plot_with_reference(input_column, results)
        self.main_window.populate_table(anomalies, ["Temps", "Paramètre", "Valeur", "Écart (%)", "Correction"])
 
    def closeEvent(self, event: QCloseEvent):
        self.accept()
 
if __name__ == "__main__":
    app = QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec()

