# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connexion.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import im_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1394, 905)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(204, 229, 255);")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(830, 270, 371, 101))
        self.lineEdit.setMaximumSize(QSize(16777215, 101))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46, 82,101,255);\n"
"border-bottom-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);\n"
"padding-bottom: 7px\n"
"")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(830, 470, 411, 61))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 61))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.lineEdit_2.setFont(font1)
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
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(820, 630, 391, 61))
        self.pushButton.setMaximumSize(QSize(16777215, 61))
        self.pushButton.setFont(font)
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
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(950, 110, 231, 81))
        self.label_3.setMaximumSize(QSize(16777215, 81))
        font2 = QFont()
        font2.setPointSize(60)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(Qt.RichText)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 681, 651))
        self.label_2.setStyleSheet(u"image: url(:/im/SII-removebg-preview.png);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.lineEdit_2.raise_()

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_2.setText("")
    # retranslateUi

