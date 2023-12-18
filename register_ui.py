from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import res

class Ui_RegisterForm(QtWidgets.QWidget):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(450, 550)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
                font = QtGui.QFont()
                font.setKerning(False)
                Form.setFont(font)
                self.widget = QtWidgets.QWidget(Form)
                self.widget.setGeometry(QtCore.QRect(40, 40, 370, 480))
                self.widget.setStyleSheet("QPushButton#btn_register{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98 , 112, 226));\n"
        "    color: rgba(255, 255, 255, 210);\n"
        "    border-radius:10px;\n"
        "}\n"
        "QPushButton#btn_register:hover{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118 , 132, 226));\n"
        "    \n"
        "}\n"
        "QPushButton#btn_register:pressed{\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(105, 118, 132, 200);\n"
        "}\n"
        ""
        "QPushButton#btn_back_to_login{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98 , 112, 226));\n"
        "    color: rgba(255, 255, 255, 210);\n"
        "    border-radius:10px;\n"
        "}\n"
        "QPushButton#btn_back_to_login:hover{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118 , 132, 226));\n"
        "    \n"
        "}\n"
        "QPushButton#btn_back_to_login:pressed{\n"
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
                self.label_3.setGeometry(QtCore.QRect(40, 40, 280, 400))
                self.label_3.setAutoFillBackground(False)
                self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
        "border-radius:15px")
                self.label_3.setText("")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.widget)
                self.label_4.setGeometry(QtCore.QRect(105, 50, 151, 40))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
                self.label_4.setObjectName("label_4")
                self.txt_email = QtWidgets.QLineEdit(self.widget)
                self.txt_email.setGeometry(QtCore.QRect(60, 200, 230, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txt_email.setFont(font)
                self.txt_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;\n"
        "")
                self.txt_email.setObjectName("txt_email")
                self.txt_pass = QtWidgets.QLineEdit(self.widget)
                self.txt_pass.setGeometry(QtCore.QRect(60, 250, 230, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txt_pass.setFont(font)
                self.txt_pass.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;\n"
        "")
                self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
                self.txt_pass.setObjectName("txt_pass")
                self.btn_register = QtWidgets.QPushButton(self.widget)
                self.btn_register.setGeometry(QtCore.QRect(75, 350, 200, 40))
                self.btn_back_to_login = QtWidgets.QPushButton(self.widget)
                self.btn_back_to_login.setGeometry(QtCore.QRect(75, 400, 200, 20))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                font2 = QtGui.QFont()
                font2.setPointSize(8)
                font2.setBold(True)
                font2.setWeight(75)
                self.btn_register.setFont(font)
                self.btn_register.setObjectName("btn_register")
                self.btn_back_to_login.setFont(font2)
                self.btn_back_to_login.setObjectName("btn_back_to_login")
                self.txt_confirm_pass = QtWidgets.QLineEdit(self.widget)
                self.txt_confirm_pass.setGeometry(QtCore.QRect(60, 300, 230, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txt_confirm_pass.setFont(font)
                self.txt_confirm_pass.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;\n"
        "")
                self.txt_confirm_pass.setEchoMode(QtWidgets.QLineEdit.Password)
                self.txt_confirm_pass.setObjectName("txt_confirm_pass")
                self.txt_Fname = QtWidgets.QLineEdit(self.widget)
                self.txt_Fname.setGeometry(QtCore.QRect(60, 100, 231, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txt_Fname.setFont(font)
                self.txt_Fname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;\n"
        "")
                self.txt_Fname.setObjectName("txt_Fname")
                self.txt_Lname = QtWidgets.QLineEdit(self.widget)
                self.txt_Lname.setGeometry(QtCore.QRect(60, 150, 231, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.txt_Lname.setFont(font)
                self.txt_Lname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;\n"
        "")
                self.txt_Lname.setObjectName("txt_Lname")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label_4.setText(_translate("Form", "Register"))
                self.txt_email.setPlaceholderText(_translate("Form", "Email"))
                self.txt_pass.setPlaceholderText(_translate("Form", "Password"))
                self.btn_register.setText(_translate("Form", "R e g i s t e r"))
                self.btn_back_to_login.setText(_translate("Form", "L o g I n"))
                self.txt_confirm_pass.setPlaceholderText(_translate("Form", "Confirm Password"))
                self.txt_Fname.setPlaceholderText(_translate("Form", "First Name"))
                self.txt_Lname.setPlaceholderText(_translate("Form", "Last Name"))
        def hideForm(self):
                # Eğer hide metodu varsa kullan, yoksa kendi gizle metodunu oluştur
                if hasattr(self, 'hide'):
                        self.hide()
                else:
                        Form.hide()

