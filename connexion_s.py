# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connexion_s.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1394, 915)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(204, 229, 255);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(400, 400))
        self.label_2.setStyleSheet(u"image: url(:/im/SII-removebg-preview.png);")

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(35)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(251, 121))
        self.label_3.setMaximumSize(QSize(16777215, 121))
        font = QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(Qt.PlainText)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 78, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(371, 50))
        self.lineEdit.setMaximumSize(QSize(550, 50))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46, 82,101,255);\n"
"border-bottom-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);\n"
"padding-bottom: 7px\n"
"")

        self.verticalLayout.addWidget(self.lineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 38, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(371, 50))
        self.lineEdit_2.setMaximumSize(QSize(550, 50))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46, 82,101,255);\n"
"border-bottom-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);\n"
"padding-bottom: 7px\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(391, 61))
        self.pushButton.setMaximumSize(QSize(16777215, 61))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"    \n"
"   background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    color: black; /* Couleur du texte */\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilsateur", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SE CONNECTER", None))
    # retranslateUi

