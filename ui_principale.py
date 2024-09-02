# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principale.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import im_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1416, 908)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 75))
        self.widget_3.setMaximumSize(QSize(16777215, 61))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.pushButton_19 = QPushButton(self.widget_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        font = QFont()
        font.setPointSize(30)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet(u"image: url(:/im/menu1-removebg-preview.png);\n"
"\n"
"border : none;")
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_19)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(558, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(204, 229, 255);")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"\n"
"background-color: rgb(204, 229, 255);")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.widget_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(550, 270, 35, 10))
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_20 = QPushButton(self.page)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 71))
        self.pushButton_20.setMaximumSize(QSize(16777215, 71))
        font2 = QFont()
        font2.setPointSize(44)
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_20, 0, 0, 1, 1)

        self.line_5 = QFrame(self.page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"border-image: url(:/im/photo accueil outil.jpg);\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_15 = QLabel(self.page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 81))
        self.label_15.setMaximumSize(QSize(16777215, 81))
        font3 = QFont()
        font3.setPointSize(16)
        self.label_15.setFont(font3)

        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_9 = QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_21 = QPushButton(self.page_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 71))
        self.pushButton_21.setMaximumSize(QSize(16777215, 71))
        self.pushButton_21.setFont(font2)
        self.pushButton_21.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_9.addWidget(self.pushButton_21, 0, 0, 1, 1)

        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 51))
        self.label_16.setMaximumSize(QSize(16777215, 51))
        font4 = QFont()
        font4.setFamilies([u"Arial Rounded MT Bold"])
        font4.setPointSize(27)
        self.label_16.setFont(font4)

        self.gridLayout_9.addWidget(self.label_16, 1, 0, 1, 1)

        self.line_6 = QFrame(self.page_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_6, 3, 0, 1, 1)

        self.pushButton_22 = QPushButton(self.page_2)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 41))
        self.pushButton_22.setMaximumSize(QSize(16777215, 41))
        font5 = QFont()
        font5.setPointSize(20)
        self.pushButton_22.setFont(font5)
        self.pushButton_22.setStyleSheet(u"\n"
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

        self.gridLayout_9.addWidget(self.pushButton_22, 2, 0, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border-image: url(:/im/banc_rouleaux.jpg);")

        self.gridLayout_9.addWidget(self.label_7, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_10 = QGridLayout(self.page_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_24 = QPushButton(self.page_3)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMaximumSize(QSize(16777215, 71))
        self.pushButton_24.setFont(font2)
        self.pushButton_24.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_24, 0, 0, 1, 1)

        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 51))
        self.label_19.setFont(font4)

        self.gridLayout_10.addWidget(self.label_19, 1, 0, 1, 1)

        self.line_7 = QFrame(self.page_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_7, 3, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.page_3)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMaximumSize(QSize(16777215, 41))
        self.pushButton_25.setFont(font5)
        self.pushButton_25.setStyleSheet(u"\n"
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

        self.gridLayout_10.addWidget(self.pushButton_25, 2, 0, 1, 1)

        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border-image: url(:/im/banc_moteur.jpg);\n"
"")

        self.gridLayout_10.addWidget(self.label_8, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_11 = QGridLayout(self.page_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_28 = QPushButton(self.page_4)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMaximumSize(QSize(16777215, 41))
        self.pushButton_28.setFont(font5)
        self.pushButton_28.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_11.addWidget(self.pushButton_28, 0, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.page_4)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMaximumSize(QSize(16777215, 41))
        self.pushButton_29.setFont(font5)
        self.pushButton_29.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_11.addWidget(self.pushButton_29, 0, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_31 = QPushButton(self.page_4)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMaximumSize(QSize(16777215, 31))
        self.pushButton_31.setFont(font5)
        self.pushButton_31.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_11.addWidget(self.pushButton_31)

        self.comboBox = QComboBox(self.page_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        self.comboBox.setMaximumSize(QSize(16777215, 29))
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.comboBox)


        self.gridLayout_11.addLayout(self.verticalLayout_11, 1, 0, 1, 2)

        self.pushButton_30 = QPushButton(self.page_4)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMaximumSize(QSize(16777215, 41))
        self.pushButton_30.setFont(font5)
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

        self.gridLayout_11.addWidget(self.pushButton_30, 2, 0, 1, 2)

        self.line_2 = QFrame(self.page_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"    border-bottom: 2px solid black;")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_2, 3, 0, 1, 2)

        self.graphicsView = QChartView(self.page_4)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.graphicsView, 4, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_12 = QGridLayout(self.page_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_27 = QPushButton(self.page_5)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMaximumSize(QSize(16777215, 61))
        self.pushButton_27.setFont(font2)
        self.pushButton_27.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_12.addWidget(self.pushButton_27, 0, 0, 1, 3)

        self.pushButton_32 = QPushButton(self.page_5)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMaximumSize(QSize(16777215, 41))
        self.pushButton_32.setFont(font5)
        self.pushButton_32.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"border-radius: 15px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_12.addWidget(self.pushButton_32, 1, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.page_5)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMaximumSize(QSize(16777215, 41))
        self.pushButton_33.setFont(font5)
        self.pushButton_33.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"border-radius: 15px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_12.addWidget(self.pushButton_33, 1, 1, 1, 1)

        self.pushButton_34 = QPushButton(self.page_5)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMaximumSize(QSize(16777215, 41))
        self.pushButton_34.setFont(font5)
        self.pushButton_34.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"border-radius: 15px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_12.addWidget(self.pushButton_34, 1, 2, 1, 1)

        self.line_4 = QFrame(self.page_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"\n"
"    border-bottom: 2px solid black;\n"
"")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line_4, 2, 0, 1, 3)

        self.graphicsView_2 = QChartView(self.page_5)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.graphicsView_2, 3, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_13 = QGridLayout(self.page_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.pushButton_36 = QPushButton(self.page_6)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMaximumSize(QSize(16777215, 61))
        self.pushButton_36.setFont(font2)
        self.pushButton_36.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_13.addWidget(self.pushButton_36, 0, 0, 1, 4)

        self.pushButton_23 = QPushButton(self.page_6)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMaximumSize(QSize(16777215, 31))
        self.pushButton_23.setFont(font5)
        self.pushButton_23.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"}")

        self.gridLayout_13.addWidget(self.pushButton_23, 1, 1, 1, 1)

        self.label_20 = QLabel(self.page_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 51))
        font6 = QFont()
        font6.setPointSize(25)
        font6.setBold(True)
        self.label_20.setFont(font6)

        self.gridLayout_13.addWidget(self.label_20, 1, 2, 1, 1)

        self.label_27 = QLabel(self.page_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 51))
        self.label_27.setFont(font6)

        self.gridLayout_13.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_17 = QLabel(self.page_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 51))
        self.label_17.setFont(font6)

        self.gridLayout_13.addWidget(self.label_17, 1, 0, 1, 1)

        self.pushButton_37 = QPushButton(self.page_6)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMaximumSize(QSize(16777215, 31))
        self.pushButton_37.setFont(font5)
        self.pushButton_37.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_13.addWidget(self.pushButton_37, 1, 3, 1, 1)

        self.pushButton_26 = QPushButton(self.page_6)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMaximumSize(QSize(16777215, 31))
        self.pushButton_26.setFont(font5)
        self.pushButton_26.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_13.addWidget(self.pushButton_26, 2, 1, 1, 1)

        self.label_21 = QLabel(self.page_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 51))
        self.label_21.setFont(font6)

        self.gridLayout_13.addWidget(self.label_21, 2, 2, 1, 1)

        self.pushButton_38 = QPushButton(self.page_6)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMaximumSize(QSize(16777215, 31))
        self.pushButton_38.setFont(font5)
        self.pushButton_38.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_13.addWidget(self.pushButton_38, 2, 3, 1, 1)

        self.pushButton_39 = QPushButton(self.page_6)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMaximumSize(QSize(16777215, 31))
        self.pushButton_39.setFont(font5)
        self.pushButton_39.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
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

        self.gridLayout_13.addWidget(self.pushButton_39, 3, 0, 1, 4)

        self.graphicsView_3 = QChartView(self.page_6)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.graphicsView_3, 5, 0, 1, 4)

        self.line_3 = QFrame(self.page_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"    border-bottom: 2px solid black;")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_13.addWidget(self.line_3, 4, 0, 1, 4)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_14 = QGridLayout(self.page_7)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_41 = QPushButton(self.page_7)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMaximumSize(QSize(16777215, 31))
        self.pushButton_41.setFont(font5)
        self.pushButton_41.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_13.addWidget(self.pushButton_41)

        self.comboBox_3 = QComboBox(self.page_7)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(16777215, 29))
        self.comboBox_3.setFont(font1)

        self.verticalLayout_13.addWidget(self.comboBox_3)


        self.gridLayout_14.addLayout(self.verticalLayout_13, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_42 = QPushButton(self.page_7)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMaximumSize(QSize(16777215, 31))
        self.pushButton_42.setFont(font5)
        self.pushButton_42.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_14.addWidget(self.pushButton_42)

        self.comboBox_4 = QComboBox(self.page_7)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(16777215, 29))
        self.comboBox_4.setFont(font1)

        self.verticalLayout_14.addWidget(self.comboBox_4)


        self.gridLayout_14.addLayout(self.verticalLayout_14, 2, 0, 1, 1)

        self.pushButton_40 = QPushButton(self.page_7)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMaximumSize(QSize(16777215, 61))
        self.pushButton_40.setFont(font2)
        self.pushButton_40.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_14.addWidget(self.pushButton_40, 0, 0, 1, 1)

        self.pushButton_45 = QPushButton(self.page_7)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMaximumSize(QSize(16777215, 51))
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_14.addWidget(self.pushButton_45, 3, 0, 1, 1)

        self.pushButton_43 = QPushButton(self.page_7)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMaximumSize(QSize(16777215, 51))
        self.pushButton_43.setFont(font5)
        self.pushButton_43.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
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

        self.gridLayout_14.addWidget(self.pushButton_43, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_15 = QGridLayout(self.page_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton_46 = QPushButton(self.page_8)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMaximumSize(QSize(16777215, 61))
        self.pushButton_46.setFont(font2)
        self.pushButton_46.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_46, 0, 0, 1, 5)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton_47 = QPushButton(self.page_8)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMaximumSize(QSize(16777215, 31))
        self.pushButton_47.setFont(font5)
        self.pushButton_47.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_15.addWidget(self.pushButton_47)

        self.comboBox_5 = QComboBox(self.page_8)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMaximumSize(QSize(16777215, 29))
        self.comboBox_5.setFont(font1)

        self.verticalLayout_15.addWidget(self.comboBox_5)


        self.gridLayout_15.addLayout(self.verticalLayout_15, 1, 0, 1, 5)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_48 = QPushButton(self.page_8)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMaximumSize(QSize(16777215, 31))
        self.pushButton_48.setFont(font5)
        self.pushButton_48.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.pushButton_48)

        self.comboBox_6 = QComboBox(self.page_8)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMaximumSize(QSize(16777215, 29))
        self.comboBox_6.setFont(font1)

        self.verticalLayout_16.addWidget(self.comboBox_6)


        self.gridLayout_15.addLayout(self.verticalLayout_16, 2, 0, 1, 5)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_49 = QPushButton(self.page_8)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMaximumSize(QSize(16777215, 31))
        self.pushButton_49.setFont(font5)
        self.pushButton_49.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.pushButton_49)

        self.comboBox_7 = QComboBox(self.page_8)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMaximumSize(QSize(16777215, 29))
        self.comboBox_7.setFont(font1)

        self.verticalLayout_17.addWidget(self.comboBox_7)


        self.gridLayout_15.addLayout(self.verticalLayout_17, 3, 0, 1, 5)

        self.pushButton_51 = QPushButton(self.page_8)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMaximumSize(QSize(16777215, 41))
        font7 = QFont()
        font7.setPointSize(30)
        font7.setBold(True)
        self.pushButton_51.setFont(font7)
        self.pushButton_51.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_51, 4, 0, 1, 5)

        self.label_25 = QLabel(self.page_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 31))
        font8 = QFont()
        font8.setFamilies([u"Arial Black"])
        font8.setPointSize(18)
        font8.setBold(True)
        self.label_25.setFont(font8)
        self.label_25.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_15.addWidget(self.label_25, 5, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.page_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 41))
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setStrikeOut(False)
        self.lineEdit_2.setFont(font9)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46, 82,101,255);\n"
"border-bottom-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);\n"
"padding-bottom: 7px\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.gridLayout_15.addWidget(self.lineEdit_2, 5, 2, 1, 2)

        self.pushButton_50 = QPushButton(self.page_8)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMaximumSize(QSize(16777215, 41))
        self.pushButton_50.setFont(font5)
        self.pushButton_50.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
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

        self.gridLayout_15.addWidget(self.pushButton_50, 5, 4, 1, 1)

        self.pushButton_52 = QPushButton(self.page_8)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMaximumSize(QSize(16777215, 41))
        self.pushButton_52.setFont(font7)
        self.pushButton_52.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_52, 6, 0, 1, 1)

        self.label_26 = QLabel(self.page_8)
        self.label_26.setObjectName(u"label_26")
        font10 = QFont()
        font10.setFamilies([u"Arial Rounded MT Bold"])
        font10.setPointSize(20)
        self.label_26.setFont(font10)

        self.gridLayout_15.addWidget(self.label_26, 6, 1, 1, 2)

        self.stackedWidget.addWidget(self.page_8)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_5)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(93, 0))
        self.widget.setMaximumSize(QSize(93, 16777215))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"border:none;\n"
"background-color: rgb(85, 170, 255);\n"
"background-color: rgb(204, 229, 255);\n"
"QPushButtonhover{\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(75, 75))
        self.label.setStyleSheet(u"image: url(:/im/SII-removebg-preview.png);")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(13, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 50, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(70)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(45, 45))
        self.pushButton.setMaximumSize(QSize(45, 45))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"	image: url(:/im/486971-accueil-icon-design-gratuit-vectoriel-removebg-preview.png);\n"
"	background-image: url(:/im/486971-accueil-icon-design-gratuit-vectoriel-removebg-preview.png);\n"
"border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(45, 45))
        self.pushButton_3.setMaximumSize(QSize(45, 45))
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    border: none;\n"
" \n"
"	image: url(:/im/4492900-200.png);\n"
"border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setMaximumSize(QSize(40, 40))
        self.pushButton_4.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"	image: url(:/im/1.png);\n"
"border-radius :3;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
" border: none;\n"
"	image: url(:/im/2.png);\n"
"border-radius:10;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(38, 38))
        self.pushButton_6.setMaximumSize(QSize(38, 38))
        self.pushButton_6.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
" border: none;\n"
"	image: url(:/im/images-removebg-preview.png);\n"
"border-radius:10;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setMaximumSize(QSize(40, 40))
        self.pushButton_8.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
" border: none;\n"
"\n"
"	image: url(:/im/3643771-configuration-configure-gear-set-setting_113449.png);\n"
"border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(38, 38))
        self.pushButton_7.setMaximumSize(QSize(38, 38))
        self.pushButton_7.setStyleSheet(u"\n"
"QPushButton {\n"
" border: none;\n"
"\n"
"	image: url(:/im/3596149.png);\n"
"\n"
"\n"
"border-radius:10;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(226, 0))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet(u"QWidget {\n"
"\n"
"background-color: rgb(255, 255, 255); \n"
"color : black;}\n"
"\n"
"QPushButton { \n"
"height : 30 px;\n"
"border: none;\n"
"\n"
"}")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(52)
        self.gridLayout.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(88, 98))
        self.label_2.setMaximumSize(QSize(88, 98))
        self.label_2.setStyleSheet(u"image: url(:/im/SII-removebg-preview.png);")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(115, 98))
        self.label_3.setMaximumSize(QSize(115, 98))
        font11 = QFont()
        font11.setPointSize(18)
        font11.setBold(True)
        self.label_3.setFont(font11)
        self.label_3.setStyleSheet(u"color: rgb(204, 229, 255);")

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(45)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 45, -1, -1)
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(207, 36))
        font12 = QFont()
        font12.setPointSize(15)
        font12.setBold(True)
        self.pushButton_2.setFont(font12)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"    \n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_2.setIconSize(QSize(100, 60))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoDefault(True)

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        font13 = QFont()
        font13.setKerning(False)
        self.frame_3.setFont(font13)
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_12 = QPushButton(self.frame_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font12)
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.pushButton_12.setIconSize(QSize(100, 60))
        self.pushButton_12.setCheckable(True)

        self.gridLayout_6.addWidget(self.pushButton_12, 0, 0, 1, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        font14 = QFont()
        font14.setPointSize(12)
        self.pushButton_15.setFont(font14)
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_15.setIconSize(QSize(50, 30))
        self.pushButton_15.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font14)
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_16.setIconSize(QSize(50, 30))
        self.pushButton_16.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_16)


        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font12)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_9.setIconSize(QSize(100, 60))
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_9)

        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setFont(font13)
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font12)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_10.setIconSize(QSize(100, 60))
        self.pushButton_10.setCheckable(True)

        self.gridLayout_7.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_17 = QPushButton(self.frame_4)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font14)
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_17.setIconSize(QSize(50, 30))
        self.pushButton_17.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_4)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font14)
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_18.setIconSize(QSize(50, 30))
        self.pushButton_18.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_18)


        self.gridLayout_7.addWidget(self.frame_4, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(39)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font12)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_11.setIconSize(QSize(100, 60))
        self.pushButton_11.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font12)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_13.setIconSize(QSize(100, 60))
        self.pushButton_13.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font12)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_14.setIconSize(QSize(100, 60))
        self.pushButton_14.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_14)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.widget.raise_()
        self.widget_2.raise_()

        self.retranslateUi(MainWindow)
        self.pushButton_10.toggled.connect(self.frame_4.setHidden)
        self.pushButton_19.toggled.connect(self.widget_2.setHidden)
        self.pushButton_12.toggled.connect(self.frame.setHidden)
        self.pushButton_9.toggled.connect(self.pushButton_4.setChecked)
        self.pushButton_13.toggled.connect(self.pushButton_8.setChecked)
        self.pushButton_2.toggled.connect(self.pushButton.setChecked)
        self.pushButton_12.toggled.connect(self.pushButton_3.setChecked)
        self.pushButton_11.toggled.connect(self.pushButton_6.setChecked)
        self.pushButton_19.toggled.connect(self.widget.setVisible)
        self.pushButton_10.toggled.connect(self.pushButton_5.setChecked)
        self.pushButton_14.toggled.connect(self.pushButton_7.setChecked)

        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_2.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bienvenue", None))
        self.label_5.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.label_6.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Analyser Pro est un outil complet pour l'analyse d\u00e9taill\u00e9e des performances des bancs d'essai automobile. </span></p><p align=\"center\"><span style=\" font-size:18pt;\">Il offre aux ing\u00e9nieurs un acc\u00e8s facile \u00e0 toutes les fonctionnalit\u00e9s n\u00e9cessaires pour une analyse pr\u00e9cise des donn\u00e9es.</span></p></body></html>", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Banc \u00e0 rouleaux", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Veuillez charger les donn\u00e9es matlab du banc \u00e0 rouleaux (.csv)</p></body></html>", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.label_7.setText("")
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Banc moteur", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Veuillez charger les donn\u00e9es matlab du banc moteur (.csv)</p></body></html>", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.label_8.setText("")
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Configurer le Param\u00e8tre d'Entr\u00e9e", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Configurer le(s) Param\u00e8tre(s) de Sortie", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Choisir le type de graphique", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Courbe", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Histogramme", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Diagramme de dispersion", None))

        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Visualiser", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Performances Moteur", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"\u00c9missions", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Dynamique du V\u00e9hicule", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Comparer", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u25cf Donn\u00e9es r\u00e9elles du banc moteur</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u25cf Donn\u00e9es matlab du banc \u00e0 rouleaux (.csv)</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u25cf Donn\u00e9es r\u00e9elles du banc \u00e0 rouleaux (.csv)</span></p></body></html>", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u25cf Donn\u00e9es matlab du banc moteur</span></p></body></html>", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Visualiser", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres d'Exportation", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Comparaison", None))

        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"Format d'Exportation", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Exporter en PDF", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Exporter en Excel", None))

        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Exporter", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Exporter", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer un rapport complet", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Langue", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Anglais", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Arabe", None))

        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Th\u00e8me", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Clair", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Sombre", None))

        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Activer", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"D\u00e9sactiver", None))

        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"S\u00e9curit\u00e9 et Confidentialit\u00e9", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u2022Modifier le mot de passe:</span></p></body></html>", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nouveau mot de passe", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Aide et Support", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><span style=\" font-family:'MS Shell Dlg 2'; font-size:22pt;\">\u2022 Documentation : </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:22pt; font-style:italic;\">[Lien_Documentation]</span></p><p><span style=\" font-family:'MS Shell Dlg 2'; font-size:22pt;\">\u2022 Support technique : </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:22pt; font-style:italic;\">[Lien_Support technique]</span></p><p><span style=\" font-family:'MS Shell Dlg 2'; font-size:22pt;\">\u2022 Version de l'outil : </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:22pt; font-style:italic;\">1.1</span></p><p><span style=\" font-size:22pt;\"><br/></span></p></body></html>", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Analyser Pro", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Types de Banc", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Banc \u00e0 rouleaux", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Banc moteur", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Visualisation", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Options d'Analyse", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Analyser", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Comparer", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Exporter", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"D\u00e9connecter", None))
    # retranslateUi

