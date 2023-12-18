from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_LoginForm(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(450, 550)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
                self.widget = QtWidgets.QWidget(Form)
                self.widget.setGeometry(QtCore.QRect(40, 40, 370, 480))
                self.widget.setStyleSheet("QPushButton#btn_login{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98 , 112, 226));\n"
        "    color: rgba(255, 255, 255, 210);\n"
        "    border-radius:5px;\n"
        "}\n"
        "QPushButton#btn_login:hover{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118 , 132, 226));\n"
        "    \n"
        "}\n"
        "QPushButton#btn_login:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(105, 118, 132, 200);\n"
        "}\n"
        ""
        "QPushButton#btn_register_now{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98 , 112, 226));\n"
        "    color: rgba(255, 255, 255, 210);\n"
        "    border-radius:5px;\n"
        "}\n"
        "QPushButton#btn_register_now:hover{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118 , 132, 226));\n"
        "    \n"
        "}\n"
        "QPushButton#btn_register_now:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(105, 118, 132, 200);\n"
        "}\n"
        ""
        )
                self.widget.setObjectName("widget")
                self.label = QtWidgets.QLabel(self.widget)
                self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
                self.label.setStyleSheet("border-image: url(:/image/background.png);\n"
        "border-radius: 20px")
                self.label.setText("")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.widget)
                self.label_2.setGeometry(QtCore.QRect(30, 30, 300, 420))
                self.label_2.setStyleSheet("background-color: qradialgradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
        "border-radius: 20px")
                self.label_2.setText("")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.widget)
                self.label_3.setGeometry(QtCore.QRect(40, 50, 280, 390))
                self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
        "border-radius:15px")
                self.label_3.setText("")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.widget)
                self.label_4.setGeometry(QtCore.QRect(130, 95, 111, 40))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
                self.label_4.setObjectName("label_4")
                self.txt_email = QtWidgets.QLineEdit(self.widget)
                self.txt_email.setGeometry(QtCore.QRect(60, 165, 230, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txt_email.setFont(font)
                self.txt_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;\n"
        "")
                self.txt_email.setObjectName("lineEdit")
                self.txt_password = QtWidgets.QLineEdit(self.widget)
                self.txt_password.setGeometry(QtCore.QRect(60, 230, 230, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txt_password.setFont(font)
                self.txt_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;\n"
        "")
                self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.txt_password.setObjectName("lineEdit_2")
                self.btn_login = QtWidgets.QPushButton(self.widget)
                self.btn_login.setGeometry(QtCore.QRect(80, 310, 200, 40))
                self.btn_register_now = QtWidgets.QPushButton(self.widget)
                self.btn_register_now.setGeometry(QtCore.QRect(90, 380, 180, 20))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.btn_login.setFont(font)
                self.btn_login.setObjectName("btn_login")
                 # Add Register button
                self.btn_register_now.setFont(font)
                self.btn_register_now.setObjectName("btn_register_now")
                self.label_5 = QtWidgets.QLabel(self.widget)
                self.label_5.setGeometry(QtCore.QRect(100, 360, 200, 16))
                self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
                self.label_5.setObjectName("label_5")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label_4.setText(_translate("Form", "Log In"))
                self.txt_email.setPlaceholderText(_translate("Form", "Email"))
                self.txt_password.setPlaceholderText(_translate("Form", "Password"))
                self.btn_login.setText(_translate("Form", "L o g  I n"))
                self.btn_register_now.setText(_translate("Form", "R e g i s t e r"))
                self.label_5.setText(_translate("Form", "if you don't have an account"))
        
        
        