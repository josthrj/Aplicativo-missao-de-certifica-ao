# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela-login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_LOGIN(object):
    def setupUi(self, LOGIN):
        if not LOGIN.objectName():
            LOGIN.setObjectName(u"LOGIN")
        LOGIN.resize(480, 640)
        LOGIN.setStyleSheet(u"background-color: rgb(42, 134, 255);")
        self.frame = QFrame(LOGIN)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 150, 321, 401))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Usuario = QLineEdit(self.frame)
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setGeometry(QRect(50, 50, 221, 41))
        font = QFont()
        font.setPointSize(12)
        self.Usuario.setFont(font)
        self.Usuario.setStyleSheet(u"background-color: rgb(182, 182, 182);")
        self.Usuario.setEchoMode(QLineEdit.Normal)
        self.Usuario.setAlignment(Qt.AlignCenter)
        self.Senha = QLineEdit(self.frame)
        self.Senha.setObjectName(u"Senha")
        self.Senha.setGeometry(QRect(50, 150, 221, 41))
        self.Senha.setFont(font)
        self.Senha.setStyleSheet(u"background-color: rgb(182, 182, 182);")
        self.Senha.setEchoMode(QLineEdit.Password)
        self.Senha.setAlignment(Qt.AlignCenter)
        self.Login = QPushButton(self.frame)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(100, 300, 111, 24))
        self.Login.setFont(font)
        self.Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.Login.setMouseTracking(True)
        self.Login.setStyleSheet(u"QPushButton{\n"
"\n"
"  background-color: rgb(18, 18, 18); \n"
"  color: rgb(240, 240, 240);\n"
"  border-radius: 10px \n"
"\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"	background-color: rgb(255, 255, 255);\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}")
        self.label = QLabel(LOGIN)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 19, 191, 121))
        self.label.setPixmap(QPixmap(u"Login.png"))
        self.label.setScaledContents(True)
        QWidget.setTabOrder(self.Usuario, self.Senha)
        QWidget.setTabOrder(self.Senha, self.Login)

        self.retranslateUi(LOGIN)

        QMetaObject.connectSlotsByName(LOGIN)
    # setupUi

    def retranslateUi(self, LOGIN):
        LOGIN.setWindowTitle(QCoreApplication.translate("LOGIN", u"Form", None))
        self.Usuario.setPlaceholderText(QCoreApplication.translate("LOGIN", u"Usuario", None))
        self.Senha.setPlaceholderText(QCoreApplication.translate("LOGIN", u"Senha", None))
        self.Login.setText(QCoreApplication.translate("LOGIN", u"LOGIN", None))
        self.label.setText("")
    # retranslateUi

