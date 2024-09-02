# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexmomo.ui'
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
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc
import momo_resources_rc
import resources_rc
import momo_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1230, 849)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.icon_onky_widget = QWidget(self.centralwidget)
        self.icon_onky_widget.setObjectName(u"icon_onky_widget")
        self.icon_onky_widget.setMinimumSize(QSize(132, 0))
        self.icon_onky_widget.setMaximumSize(QSize(132, 16777215))
        self.icon_onky_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(204, 229, 255);\n"
"}\n"
"QPushButton:checked{\n"
" background-color:white;\n"
"border-radius:3px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.icon_onky_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(13, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.logo_1 = QLabel(self.icon_onky_widget)
        self.logo_1.setObjectName(u"logo_1")
        self.logo_1.setMaximumSize(QSize(80, 60))
        self.logo_1.setPixmap(QPixmap(u":/<newPrefix>/icon_2/SII-removebg-preview.png"))
        self.logo_1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_1)

        self.horizontalSpacer_9 = QSpacerItem(13, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(35)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 40, -1, -1)
        self.Home_1 = QPushButton(self.icon_onky_widget)
        self.Home_1.setObjectName(u"Home_1")
        self.Home_1.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius:16;\n"
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
        icon = QIcon()
        icon.addFile(u":/<newPrefix>/icon_2/486971-accueil-icon-design-gratuit-vectoriel-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_1.setIcon(icon)
        self.Home_1.setIconSize(QSize(100, 40))
        self.Home_1.setCheckable(True)
        self.Home_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.Home_1)

        self.Analysis_1 = QPushButton(self.icon_onky_widget)
        self.Analysis_1.setObjectName(u"Analysis_1")
        self.Analysis_1.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/<newPrefix>/icon_2/4492900-200.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Analysis_1.setIcon(icon1)
        self.Analysis_1.setIconSize(QSize(100, 40))
        self.Analysis_1.setCheckable(True)
        self.Analysis_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.Analysis_1)

        self.Help_1 = QPushButton(self.icon_onky_widget)
        self.Help_1.setObjectName(u"Help_1")
        self.Help_1.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/<newPrefix>/icon_2/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Help_1.setIcon(icon2)
        self.Help_1.setIconSize(QSize(100, 38))
        self.Help_1.setCheckable(True)
        self.Help_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.Help_1)

        self.About_1 = QPushButton(self.icon_onky_widget)
        self.About_1.setObjectName(u"About_1")
        self.About_1.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/<newPrefix>/icon_2/2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.About_1.setIcon(icon3)
        self.About_1.setIconSize(QSize(100, 38))
        self.About_1.setCheckable(True)
        self.About_1.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.About_1)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 388, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Setting_1 = QPushButton(self.icon_onky_widget)
        self.Setting_1.setObjectName(u"Setting_1")
        self.Setting_1.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/<newPrefix>/icon_2/3643771-configuration-configure-gear-set-setting_113449.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Setting_1.setIcon(icon4)
        self.Setting_1.setIconSize(QSize(100, 38))
        self.Setting_1.setCheckable(True)
        self.Setting_1.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Setting_1)

        self.Log_out_1 = QPushButton(self.icon_onky_widget)
        self.Log_out_1.setObjectName(u"Log_out_1")
        self.Log_out_1.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius:16;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/<newPrefix>/icon_2/3596149.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Log_out_1.setIcon(icon5)
        self.Log_out_1.setIconSize(QSize(100, 38))
        self.Log_out_1.setCheckable(True)
        self.Log_out_1.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Log_out_1)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.gridLayout_6.addWidget(self.icon_onky_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(226, 0))
        font = QFont()
        font.setPointSize(27)
        self.icon_text_widget.setFont(font)
        self.icon_text_widget.setStyleSheet(u"QWidget {\n"
"\n"
"background-color: rgb(255, 255, 255); \n"
"color : black;}\n"
"\n"
"QPushButton { \n"
"height : 30 px;\n"
"border: none;\n"
"\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_12.setSpacing(30)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 28, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_2 = QLabel(self.icon_text_widget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setMinimumSize(QSize(80, 60))
        self.logo_2.setMaximumSize(QSize(80, 60))
        self.logo_2.setPixmap(QPixmap(u":/<newPrefix>/icon_2/SII-removebg-preview.png"))
        self.logo_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_2)

        self.EMIZER = QLabel(self.icon_text_widget)
        self.EMIZER.setObjectName(u"EMIZER")
        self.EMIZER.setMinimumSize(QSize(120, 60))
        self.EMIZER.setMaximumSize(QSize(120, 60))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.EMIZER.setFont(font1)
        self.EMIZER.setStyleSheet(u"color: rgb(204, 229, 255);")

        self.horizontalLayout.addWidget(self.EMIZER)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(40)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 21, -1, -1)
        self.Home_2 = QPushButton(self.icon_text_widget)
        self.Home_2.setObjectName(u"Home_2")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.Home_2.setFont(font2)
        self.Home_2.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.Home_2.setIconSize(QSize(200, 50))
        self.Home_2.setCheckable(True)
        self.Home_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Home_2)

        self.Analysis = QFrame(self.icon_text_widget)
        self.Analysis.setObjectName(u"Analysis")
        self.Analysis.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.Analysis)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Analysis_2 = QPushButton(self.Analysis)
        self.Analysis_2.setObjectName(u"Analysis_2")
        self.Analysis_2.setFont(font2)
        self.Analysis_2.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Analysis_2.setIconSize(QSize(200, 50))
        self.Analysis_2.setCheckable(True)
        self.Analysis_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Analysis_2)

        self.Analysis_dropdown = QFrame(self.Analysis)
        self.Analysis_dropdown.setObjectName(u"Analysis_dropdown")
        self.Analysis_dropdown.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.Analysis_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Data_Analysis = QPushButton(self.Analysis_dropdown)
        self.Data_Analysis.setObjectName(u"Data_Analysis")
        font3 = QFont()
        font3.setPointSize(12)
        self.Data_Analysis.setFont(font3)
        self.Data_Analysis.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Data_Analysis.setCheckable(True)
        self.Data_Analysis.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.Data_Analysis)

        self.Data_Comparisons = QPushButton(self.Analysis_dropdown)
        self.Data_Comparisons.setObjectName(u"Data_Comparisons")
        self.Data_Comparisons.setFont(font3)
        self.Data_Comparisons.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Data_Comparisons.setCheckable(True)
        self.Data_Comparisons.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.Data_Comparisons)


        self.verticalLayout_2.addWidget(self.Analysis_dropdown)


        self.verticalLayout_11.addWidget(self.Analysis)

        self.Help_2 = QPushButton(self.icon_text_widget)
        self.Help_2.setObjectName(u"Help_2")
        self.Help_2.setFont(font2)
        self.Help_2.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
"    border: 1px solid black; \n"
"}\n"
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
        self.Help_2.setIconSize(QSize(200, 50))
        self.Help_2.setCheckable(True)
        self.Help_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.Help_2)

        self.Analysis_3 = QFrame(self.icon_text_widget)
        self.Analysis_3.setObjectName(u"Analysis_3")
        self.Analysis_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.Analysis_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Analysis_4 = QPushButton(self.Analysis_3)
        self.Analysis_4.setObjectName(u"Analysis_4")
        self.Analysis_4.setFont(font2)
        self.Analysis_4.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Analysis_4.setIconSize(QSize(200, 50))
        self.Analysis_4.setCheckable(True)
        self.Analysis_4.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.Analysis_4)

        self.Analysis_dropdown_2 = QFrame(self.Analysis_3)
        self.Analysis_dropdown_2.setObjectName(u"Analysis_dropdown_2")
        self.Analysis_dropdown_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.Analysis_dropdown_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Data_Analysis_2 = QPushButton(self.Analysis_dropdown_2)
        self.Data_Analysis_2.setObjectName(u"Data_Analysis_2")
        self.Data_Analysis_2.setFont(font3)
        self.Data_Analysis_2.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Data_Analysis_2.setCheckable(True)
        self.Data_Analysis_2.setAutoExclusive(False)

        self.verticalLayout_7.addWidget(self.Data_Analysis_2)

        self.Data_Comparisons_2 = QPushButton(self.Analysis_dropdown_2)
        self.Data_Comparisons_2.setObjectName(u"Data_Comparisons_2")
        self.Data_Comparisons_2.setFont(font3)
        self.Data_Comparisons_2.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Data_Comparisons_2.setCheckable(True)
        self.Data_Comparisons_2.setAutoExclusive(False)

        self.verticalLayout_7.addWidget(self.Data_Comparisons_2)


        self.verticalLayout_3.addWidget(self.Analysis_dropdown_2)


        self.verticalLayout_11.addWidget(self.Analysis_3)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 408, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(45)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Setting_2 = QPushButton(self.icon_text_widget)
        self.Setting_2.setObjectName(u"Setting_2")
        self.Setting_2.setFont(font2)
        self.Setting_2.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Setting_2.setIconSize(QSize(200, 50))
        self.Setting_2.setCheckable(True)
        self.Setting_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.Setting_2)

        self.Log_out_2 = QPushButton(self.icon_text_widget)
        self.Log_out_2.setObjectName(u"Log_out_2")
        self.Log_out_2.setFont(font2)
        self.Log_out_2.setStyleSheet(u"QPushButton{\n"
" padding-left: 0px;\n"
"}\n"
"QPushButton {\n"
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
        self.Log_out_2.setIconSize(QSize(200, 50))
        self.Log_out_2.setCheckable(True)
        self.Log_out_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.Log_out_2)


        self.verticalLayout_12.addLayout(self.verticalLayout_4)


        self.gridLayout_6.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(34)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 29, -1, -1)
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(1, 63))
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/<no prefix>/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Lucida Bright"])
        font4.setPointSize(15)
        font4.setBold(True)
        self.label.setFont(font4)

        self.verticalLayout_9.addWidget(self.label)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer = QSpacerItem(313, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
" padding-left:20px;\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(590, 250))
        self.main_screen_widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.main_screen_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font5 = QFont()
        font5.setPointSize(30)
        self.stackedWidget.setFont(font5)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_5 = QGridLayout(self.page_1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 60))
        self.label_10.setMaximumSize(QSize(16777215, 60))
        font6 = QFont()
        font6.setFamilies([u"Lucida Bright"])
        font6.setPointSize(30)
        font6.setBold(True)
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.page_1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 97))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
" padding-left:20px;\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
" background-color: #000000;\n"
" color:white;\n"
"}")

        self.gridLayout_5.addWidget(self.textEdit, 1, 0, 1, 1)

        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/<newPrefix>/icon_2/photo accueil outil.jpg"))

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_3 = QGridLayout(self.page_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 60))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.page_6)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 35))
        self.widget_3.setMaximumSize(QSize(16777215, 35))
        self.widget_3.setStyleSheet(u"\n"
"background-color: rgb(148, 148, 148);")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/<newPrefix>/icon_2/icons8-upload-to-cloud-24.png"))

        self.horizontalLayout_9.addWidget(self.label_7)

        self.label_20 = QLabel(self.widget_3)
        self.label_20.setObjectName(u"label_20")
        font7 = QFont()
        font7.setFamilies([u"Lucida Bright"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.label_20.setFont(font7)

        self.horizontalLayout_9.addWidget(self.label_20)

        self.horizontalSpacer_5 = QSpacerItem(501, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.Browse_Files_5 = QPushButton(self.widget_3)
        self.Browse_Files_5.setObjectName(u"Browse_Files_5")
        self.Browse_Files_5.setMinimumSize(QSize(100, 20))
        self.Browse_Files_5.setMaximumSize(QSize(16777215, 20))
        self.Browse_Files_5.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);\n"
" color: rgb(255, 255, 255);\n"
" border: none;\n"
" border-radius: 15px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"\n"
"")
        self.Browse_Files_5.setCheckable(True)
        self.Browse_Files_5.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.Browse_Files_5)


        self.gridLayout_3.addWidget(self.widget_3, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.page_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 35))
        self.widget_8.setMaximumSize(QSize(16777215, 35))
        self.widget_8.setStyleSheet(u"\n"
"background-color: rgb(148, 148, 148);")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.widget_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/<newPrefix>/icon_2/icons8-upload-to-cloud-24.png"))

        self.horizontalLayout_11.addWidget(self.label_16)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_22 = QLabel(self.widget_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_22)


        self.horizontalLayout_11.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_8 = QSpacerItem(501, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.Browse_Files_11 = QPushButton(self.widget_8)
        self.Browse_Files_11.setObjectName(u"Browse_Files_11")
        self.Browse_Files_11.setMinimumSize(QSize(100, 20))
        self.Browse_Files_11.setMaximumSize(QSize(16777215, 20))
        self.Browse_Files_11.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);\n"
" color: rgb(255, 255, 255);\n"
" border: none;\n"
" border-radius: 15px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}")
        self.Browse_Files_11.setCheckable(True)
        self.Browse_Files_11.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.Browse_Files_11)


        self.gridLayout_3.addWidget(self.widget_8, 2, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Start_analysis_button_4 = QPushButton(self.page_6)
        self.Start_analysis_button_4.setObjectName(u"Start_analysis_button_4")
        self.Start_analysis_button_4.setMinimumSize(QSize(300, 30))
        font8 = QFont()
        font8.setPointSize(10)
        self.Start_analysis_button_4.setFont(font8)
        self.Start_analysis_button_4.setStyleSheet(u"QPushButton {\n"
"border-radius: 15px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")
        self.Start_analysis_button_4.setIconSize(QSize(28, 26))
        self.Start_analysis_button_4.setCheckable(True)
        self.Start_analysis_button_4.setAutoExclusive(True)

        self.horizontalLayout_12.addWidget(self.Start_analysis_button_4)

        self.Start_analysis_button_5 = QPushButton(self.page_6)
        self.Start_analysis_button_5.setObjectName(u"Start_analysis_button_5")
        self.Start_analysis_button_5.setMinimumSize(QSize(185, 30))
        self.Start_analysis_button_5.setFont(font8)
        self.Start_analysis_button_5.setStyleSheet(u"QPushButton {\n"
"border-radius: 15px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")
        self.Start_analysis_button_5.setIconSize(QSize(28, 26))
        self.Start_analysis_button_5.setCheckable(True)
        self.Start_analysis_button_5.setAutoExclusive(True)

        self.horizontalLayout_12.addWidget(self.Start_analysis_button_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)

        self.graphicsView_2 = QChartView(self.page_6)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.graphicsView_2, 4, 0, 1, 1)

        self.Generate_report_button_2 = QPushButton(self.page_6)
        self.Generate_report_button_2.setObjectName(u"Generate_report_button_2")
        self.Generate_report_button_2.setMinimumSize(QSize(260, 40))
        self.Generate_report_button_2.setMaximumSize(QSize(260, 40))
        self.Generate_report_button_2.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);;\n"
" color: white;\n"
" border: none;\n"
" border-radius: 8px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"")
        self.Generate_report_button_2.setCheckable(True)
        self.Generate_report_button_2.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.Generate_report_button_2, 5, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 75))
        self.widget_5.setStyleSheet(u"\n"
"background-color: rgb(148, 148, 148);")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/<no prefix>/icons/icons8-t\u00e9l\u00e9charger-vers-le-cloud-50.png"))

        self.horizontalLayout_20.addWidget(self.label_12)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_31 = QLabel(self.widget_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font7)

        self.verticalLayout_20.addWidget(self.label_31)

        self.label_32 = QLabel(self.widget_5)
        self.label_32.setObjectName(u"label_32")
        font9 = QFont()
        font9.setFamilies([u"Lucida Bright"])
        font9.setPointSize(8)
        font9.setBold(False)
        font9.setItalic(True)
        self.label_32.setFont(font9)

        self.verticalLayout_20.addWidget(self.label_32)


        self.horizontalLayout_20.addLayout(self.verticalLayout_20)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)

        self.horizontalSpacer_14 = QSpacerItem(501, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)

        self.Browse_Files_8 = QPushButton(self.widget_5)
        self.Browse_Files_8.setObjectName(u"Browse_Files_8")
        self.Browse_Files_8.setMinimumSize(QSize(274, 45))
        self.Browse_Files_8.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);\n"
" color: rgb(255, 255, 255);\n"
" border: none;\n"
" border-radius: 15px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"\n"
"")
        self.Browse_Files_8.setCheckable(True)
        self.Browse_Files_8.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.Browse_Files_8)


        self.gridLayout_4.addWidget(self.widget_5, 1, 0, 1, 1)

        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 60))
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/<newPrefix>/icon_2/4.png"))

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_6 = QWidget(self.page_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 75))
        self.widget_6.setStyleSheet(u"\n"
"background-color: rgb(148, 148, 148);")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_15 = QLabel(self.widget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/<no prefix>/icons/icons8-t\u00e9l\u00e9charger-vers-le-cloud-50.png"))

        self.horizontalLayout_22.addWidget(self.label_15)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_33 = QLabel(self.widget_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)

        self.verticalLayout_21.addWidget(self.label_33)

        self.label_34 = QLabel(self.widget_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font9)

        self.verticalLayout_21.addWidget(self.label_34)


        self.horizontalLayout_22.addLayout(self.verticalLayout_21)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_22)

        self.horizontalSpacer_2 = QSpacerItem(470, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.Browse_Files_9 = QPushButton(self.widget_6)
        self.Browse_Files_9.setObjectName(u"Browse_Files_9")
        self.Browse_Files_9.setMinimumSize(QSize(290, 45))
        self.Browse_Files_9.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);\n"
" color: rgb(255, 255, 255);\n"
" border: none;\n"
" border-radius: 15px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"\n"
"")
        self.Browse_Files_9.setCheckable(True)
        self.Browse_Files_9.setAutoExclusive(True)

        self.horizontalLayout_8.addWidget(self.Browse_Files_9)


        self.gridLayout_7.addWidget(self.widget_6, 1, 0, 1, 1)

        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 60))
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/<newPrefix>/icon_2/249.jpg"))

        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_15 = QGridLayout(self.page_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(22)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.Browse_Files_18 = QPushButton(self.page_4)
        self.Browse_Files_18.setObjectName(u"Browse_Files_18")
        self.Browse_Files_18.setMinimumSize(QSize(100, 45))
        self.Browse_Files_18.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);\n"
" color: rgb(255, 255, 255);\n"
" border: none;\n"
" border-radius: 15px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}")
        self.Browse_Files_18.setCheckable(True)
        self.Browse_Files_18.setAutoExclusive(True)

        self.horizontalLayout_41.addWidget(self.Browse_Files_18)

        self.Browse_Files_19 = QPushButton(self.page_4)
        self.Browse_Files_19.setObjectName(u"Browse_Files_19")
        self.Browse_Files_19.setMinimumSize(QSize(100, 45))
        self.Browse_Files_19.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);\n"
" color: rgb(255, 255, 255);\n"
" border: none;\n"
" border-radius: 15px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}")
        self.Browse_Files_19.setCheckable(True)
        self.Browse_Files_19.setAutoExclusive(True)

        self.horizontalLayout_41.addWidget(self.Browse_Files_19)


        self.gridLayout_15.addLayout(self.horizontalLayout_41, 0, 0, 1, 1)

        self.Browse_Files_27 = QPushButton(self.page_4)
        self.Browse_Files_27.setObjectName(u"Browse_Files_27")
        self.Browse_Files_27.setMinimumSize(QSize(100, 45))
        self.Browse_Files_27.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);\n"
" color: rgb(255, 255, 255);\n"
" border: none;\n"
" border-radius: 15px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}")
        self.Browse_Files_27.setCheckable(True)
        self.Browse_Files_27.setAutoExclusive(True)

        self.gridLayout_15.addWidget(self.Browse_Files_27, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.page_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 35))
        self.comboBox.setMaximumSize(QSize(16777215, 35))
        self.comboBox.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_15.addWidget(self.comboBox, 2, 0, 1, 1)

        self.Start_analysis_button_8 = QPushButton(self.page_4)
        self.Start_analysis_button_8.setObjectName(u"Start_analysis_button_8")
        self.Start_analysis_button_8.setMinimumSize(QSize(185, 45))
        font10 = QFont()
        font10.setPointSize(20)
        self.Start_analysis_button_8.setFont(font10)
        self.Start_analysis_button_8.setStyleSheet(u"QPushButton {\n"
"border-radius: 15px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/<no prefix>/icons/icons8-analysis-50 (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start_analysis_button_8.setIcon(icon7)
        self.Start_analysis_button_8.setIconSize(QSize(28, 26))
        self.Start_analysis_button_8.setCheckable(True)
        self.Start_analysis_button_8.setAutoExclusive(True)

        self.gridLayout_15.addWidget(self.Start_analysis_button_8, 3, 0, 1, 1)

        self.graphicsView_9 = QChartView(self.page_4)
        self.graphicsView_9.setObjectName(u"graphicsView_9")
        self.graphicsView_9.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.graphicsView_9, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_17 = QLabel(self.page_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 60))
        self.label_17.setMaximumSize(QSize(16777215, 60))
        self.label_17.setFont(font6)
        self.label_17.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.label_17)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_47 = QPushButton(self.page_7)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(0, 31))
        self.pushButton_47.setMaximumSize(QSize(16777215, 31))
        font11 = QFont()
        font11.setFamilies([u"Lucida Bright"])
        font11.setPointSize(15)
        self.pushButton_47.setFont(font11)
        self.pushButton_47.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_15.addWidget(self.pushButton_47)

        self.comboBox_5 = QComboBox(self.page_7)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(0, 29))
        self.comboBox_5.setMaximumSize(QSize(16777215, 29))
        self.comboBox_5.setFont(font4)

        self.verticalLayout_15.addWidget(self.comboBox_5)


        self.verticalLayout_17.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_48 = QPushButton(self.page_7)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(0, 31))
        self.pushButton_48.setMaximumSize(QSize(16777215, 31))
        self.pushButton_48.setFont(font11)
        self.pushButton_48.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.pushButton_48)

        self.comboBox_6 = QComboBox(self.page_7)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(0, 29))
        self.comboBox_6.setMaximumSize(QSize(16777215, 29))
        self.comboBox_6.setFont(font4)

        self.verticalLayout_16.addWidget(self.comboBox_6)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.verticalSpacer_3 = QSpacerItem(20, 158, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(25)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(30)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 30, -1, -1)
        self.label_18 = QLabel(self.page_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 60))
        self.label_18.setMaximumSize(QSize(16777215, 60))
        font12 = QFont()
        font12.setFamilies([u"Lucida Bright"])
        font12.setPointSize(25)
        font12.setBold(True)
        self.label_18.setFont(font12)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.verticalLayout_13.addWidget(self.label_18)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_2 = QLineEdit(self.page_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(250, 41))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 41))
        font13 = QFont()
        font13.setPointSize(15)
        font13.setBold(True)
        font13.setStrikeOut(False)
        self.lineEdit_2.setFont(font13)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46, 82,101,255);\n"
"border-bottom-color: rgb(112, 112, 112);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 7px\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.lineEdit_2)

        self.horizontalSpacer_3 = QSpacerItem(548, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.pushButton_50 = QPushButton(self.page_7)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(211, 35))
        self.pushButton_50.setMaximumSize(QSize(16777215, 35))
        self.pushButton_50.setFont(font11)
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

        self.horizontalLayout_7.addWidget(self.pushButton_50)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.label_5 = QLabel(self.page_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(780, 90))
        self.label_5.setMaximumSize(QSize(16777215, 90))
        font14 = QFont()
        font14.setFamilies([u"Lucida Bright"])
        font14.setPointSize(13)
        font14.setBold(True)
        self.label_5.setFont(font14)

        self.verticalLayout_14.addWidget(self.label_5)


        self.verticalLayout_17.addLayout(self.verticalLayout_14)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.page_7)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout = QGridLayout(self.page_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Generate_report_button = QPushButton(self.page_5)
        self.Generate_report_button.setObjectName(u"Generate_report_button")
        self.Generate_report_button.setMinimumSize(QSize(240, 51))
        self.Generate_report_button.setMaximumSize(QSize(240, 51))
        self.Generate_report_button.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);;\n"
" color: white;\n"
" border: none;\n"
" border-radius: 8px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"")
        self.Generate_report_button.setCheckable(True)
        self.Generate_report_button.setAutoExclusive(True)

        self.gridLayout.addWidget(self.Generate_report_button, 3, 0, 1, 1)

        self.graphicsView = QChartView(self.page_5)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.graphicsView, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.performance_moteur = QPushButton(self.page_5)
        self.performance_moteur.setObjectName(u"performance_moteur")
        self.performance_moteur.setMinimumSize(QSize(195, 45))
        self.performance_moteur.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);;\n"
" color: white;\n"
" border: none;\n"
" border-radius: 8px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/<no prefix>/icons/icons8-lightning-bolt-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.performance_moteur.setIcon(icon8)
        self.performance_moteur.setIconSize(QSize(32, 29))
        self.performance_moteur.setCheckable(True)
        self.performance_moteur.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.performance_moteur)

        self.emissions = QPushButton(self.page_5)
        self.emissions.setObjectName(u"emissions")
        self.emissions.setMinimumSize(QSize(195, 45))
        self.emissions.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);;\n"
" color: white;\n"
" border: none;\n"
" border-radius: 8px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/<no prefix>/icons/icons8-car-emissions-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.emissions.setIcon(icon9)
        self.emissions.setIconSize(QSize(57, 41))
        self.emissions.setCheckable(True)
        self.emissions.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.emissions)

        self.resistance_force = QPushButton(self.page_5)
        self.resistance_force.setObjectName(u"resistance_force")
        self.resistance_force.setMinimumSize(QSize(210, 45))
        self.resistance_force.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(0, 85, 127);;\n"
" color: white;\n"
" border: none;\n"
" border-radius: 8px;\n"
" font-weight: bold;\n"
" font-size:15px\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/<no prefix>/icons/icons8-wheel-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resistance_force.setIcon(icon10)
        self.resistance_force.setIconSize(QSize(28, 26))
        self.resistance_force.setCheckable(True)
        self.resistance_force.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.resistance_force)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 60))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    border-radius: 10px; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 39, 72);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.main_screen_widget)


        self.gridLayout_6.addLayout(self.verticalLayout_10, 0, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Analysis_2.toggled.connect(self.Analysis_dropdown.setHidden)
        self.Analysis_4.toggled.connect(self.Analysis_dropdown_2.setHidden)
        self.Home_1.toggled.connect(self.Home_2.setChecked)
        self.Analysis_1.toggled.connect(self.Analysis_2.setChecked)
        self.Help_1.toggled.connect(self.Help_2.setChecked)
        self.About_1.toggled.connect(self.Analysis_4.setChecked)
        self.Setting_1.toggled.connect(self.Setting_2.setChecked)
        self.Log_out_1.toggled.connect(self.Log_out_2.setChecked)
        self.Log_out_1.toggled.connect(MainWindow.close)
        self.Log_out_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_onky_widget.setVisible)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_1.setText("")
        self.Home_1.setText("")
        self.Analysis_1.setText("")
        self.Help_1.setText("")
        self.About_1.setText("")
        self.Setting_1.setText("")
        self.Log_out_1.setText("")
        self.logo_2.setText("")
        self.EMIZER.setText(QCoreApplication.translate("MainWindow", u"ANALYSER PRO", None))
        self.Home_2.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.Analysis_2.setText(QCoreApplication.translate("MainWindow", u"Importation", None))
        self.Data_Analysis.setText(QCoreApplication.translate("MainWindow", u"Banc \u00e0 rouleaux", None))
        self.Data_Comparisons.setText(QCoreApplication.translate("MainWindow", u"Banc moteur", None))
        self.Help_2.setText(QCoreApplication.translate("MainWindow", u"Visualisation", None))
        self.Analysis_4.setText(QCoreApplication.translate("MainWindow", u"Options d'Analyse", None))
        self.Data_Analysis_2.setText(QCoreApplication.translate("MainWindow", u"Analyse des param\u00e8tres", None))
        self.Data_Comparisons_2.setText(QCoreApplication.translate("MainWindow", u"Comparaison", None))
        self.Setting_2.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.Log_out_2.setText(QCoreApplication.translate("MainWindow", u"D\u00e9connecter", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenue", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher ici...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:5.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt;\">Analyser Pro est un outil complet pour l'analyse d\u00e9taill\u00e9e des performances des bancs d'essai automobile. Il offre aux ing\u00e9nieurs un acc\u00e8s facile \u00e0 toutes les fonctionnalit\u00e9s n\u00e9cessaires pour une analyse pr\u00e9cise des donn\u00e9es.</span></p></body></html>", None))
        self.label_4.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Comparaison R\u00e9elle vs Simul\u00e9e", None))
        self.label_7.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Importez les donn\u00e9es r\u00e9elles", None))
        self.Browse_Files_5.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.label_16.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Importez les donn\u00e9es Matlab", None))
        self.Browse_Files_11.setText(QCoreApplication.translate("MainWindow", u"Charger", None))
        self.Start_analysis_button_4.setText(QCoreApplication.translate("MainWindow", u"S\u00e9lectionner les param\u00e8tres \u00e0 comparer", None))
        self.Start_analysis_button_5.setText(QCoreApplication.translate("MainWindow", u"Visualiser", None))
        self.Generate_report_button_2.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer le tableau de comparaison", None))
        self.label_12.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Importez les donn\u00e9es ", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Limite 200MB par fichier.CSV", None))
        self.Browse_Files_8.setText(QCoreApplication.translate("MainWindow", u"Charger les donn\u00e9es", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Banc \u00e0 rouleaux", None))
        self.label_2.setText("")
        self.label_15.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Importez les donn\u00e9es ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Limite 200MB par fichier.CSV", None))
        self.Browse_Files_9.setText(QCoreApplication.translate("MainWindow", u"Charger les donn\u00e9es", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Banc Moteur", None))
        self.label_3.setText("")
        self.Browse_Files_18.setText(QCoreApplication.translate("MainWindow", u"Configurer le Param\u00e8tre d'Entr\u00e9e", None))
        self.Browse_Files_19.setText(QCoreApplication.translate("MainWindow", u"Configurer le(s) Param\u00e8tre(s) de  Sortie", None))
        self.Browse_Files_27.setText(QCoreApplication.translate("MainWindow", u"Choisir le type de graphique", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Courbe", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Histogramme", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Diagramme de dispersion", None))

        self.Start_analysis_button_8.setText(QCoreApplication.translate("MainWindow", u"Visualiser", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"  Param\u00e8tres", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Langue", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Anglais", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Arabe", None))

        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Th\u00e8me", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Clair", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Sombre", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"  Modifier le mot de passe", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nouveau mot de passe", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Besoin d'aide ? Contactez-nous \u00e0 support@sii-maroc.com ou appelez-nous au 05 22 43 83 90", None))
        self.Generate_report_button.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer le tableau d'analyse ", None))
        self.performance_moteur.setText(QCoreApplication.translate("MainWindow", u"Performances Moteur", None))
        self.emissions.setText(QCoreApplication.translate("MainWindow", u"\u00c9missions", None))
        self.resistance_force.setText(QCoreApplication.translate("MainWindow", u"Dynamique du V\u00e9hicule", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"     Analyse des param\u00e8tres", None))
    # retranslateUi

