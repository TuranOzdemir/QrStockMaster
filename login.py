from database_service import * 
from login_ui import *
from main_window_ui import Ui_MainWindow

class LoginLogic:
    def __init__(self, db):
        self.db = db
        
    def authenticate(self, email, password):
        # Query Firestore to find a user with the given email
        query = self.db.collection('users').where(filter = FieldFilter("email", "==", email))
        found_user = next(query.stream(), None)

        if found_user:
            user_data = found_user.to_dict()
            stored_password = user_data.get('password')

            # Check if the entered password matches the stored password
            if stored_password and stored_password == password:
                logging.info("Login successful for email: %s", email)
                return True
            else:
                logging.warning("Incorrect password for email: %s", email)
                return False
        else:
            logging.info("No user found with email: %s", email)
            return False
from PyQt5.QtWidgets import QMessageBox

class ButtonFunctions:
    def __init__(self, db, login_logic, register_logic, login_ui, register_ui, login_form, register_form, main_window):
        self.db = db
        self.login_logic = login_logic
        self.register_logic = register_logic
        self.login_ui = login_ui
        self.register_ui = register_ui
        self.login_form = login_form
        self.register_form = register_form
        self.main_window = main_window

    def on_btn_login_clicked(self):
        email = self.login_ui.txt_email.text()
        password = self.login_ui.txt_password.text()

        if self.login_logic.authenticate(email, password):
            query = self.db.collection('users').where(filter = FieldFilter("email", "==", email))
            found_user = next(query.stream(), None)
            
            if found_user:
                user_data = found_user.to_dict()
                QMessageBox.information(self.login_form, 'Login Successful', 'Welcome, {}'.format(user_data.get('first_name')))
                self.show_main_window()
        else:
            QMessageBox.warning(self.login_form, 'Login Failed', 'Invalid email or password')

    def on_btn_register_clicked(self):
        user = User(
            first_name = self.register_ui.txt_Fname.text(),
            last_name = self.register_ui.txt_Lname.text(),
            email = self.register_ui.txt_email.text(),
            password = self.register_ui.txt_pass.text(),
            date_created = datetime.now()
            )
        # Call the register function from RegisterLogic
        if self.register_logic.register(user):
            QMessageBox.information(self.register_form, 'Registration Successful', 'User registered successfully')
            # Optionally, you can switch back to the login form after successful registration
            self.show_login_form()

        else:
            QMessageBox.warning(self.register_form, 'Registration Failed', 'User registration failed')

    def show_login_form(self):
        # Hide the registration form and show the login form
        self.register_form.hide()
        self.login_form.show()

    def show_register_form(self):
        # Hide the login form and show the registration form
        self.login_form.hide()
        self.register_form.show()
    
    def show_main_window(self):
        self.main_window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.main_window)
        self.login_form.hide()
        self.main_window.show()

