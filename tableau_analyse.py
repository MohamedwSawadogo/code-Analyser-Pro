# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tableau_analyse.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(18, 39, 72);\n"
"")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 85, 127);\n"
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

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tableau d'\u00c9valuation", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exporter le tableau", None))
    # retranslateUi

