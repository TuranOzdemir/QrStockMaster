from database_service import *
from login_ui import *
from login import *
from register_ui import *
from register import *
from main_window_ui import *
import res
import icons_rc

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if not firebase_admin._apps:
        cred = credentials.Certificate('serviceAccountKey.json')
        firebase_admin.initialize_app(cred)

    db = firestore.client()

    login_logic = LoginLogic(db)
    register_logic = RegisterLogic(db)

    # Create instances of the forms
    login_form = QtWidgets.QWidget()
    login_ui = Ui_LoginForm()
    login_ui.setupUi(login_form)

    register_form = QtWidgets.QWidget()
    register_ui = Ui_RegisterForm()
    register_ui.setupUi(register_form)

    main_form = QtWidgets.QMainWindow()    
    main_window_ui = Ui_MainWindow()
    main_window_ui.setupUi(main_form)
    
    # Create instances of the ButtonFunctions class with forms
    btn_functions = ButtonFunctions(db, login_logic, register_logic, login_ui, register_ui, login_form, register_form, main_window_ui)

    # Connect the signals to the slots without calling the functions
    login_ui.btn_login.clicked.connect(btn_functions.on_btn_login_clicked)
    login_ui.btn_register_now.clicked.connect(btn_functions.show_register_form)

    register_ui.btn_register.clicked.connect(btn_functions.on_btn_register_clicked)
    register_ui.btn_back_to_login.clicked.connect(btn_functions.show_login_form)
    # main_window_ui.btn_max_2.clicked.connect(lambda: main_window_ui.exit())

    # Show the login form
    login_form.show()

    # Run the application
    sys.exit(app.exec_())
