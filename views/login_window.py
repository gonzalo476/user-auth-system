from PySide6 import QtWidgets, QtCore

from controllers.auth_controller import AuthController
from .main_window import MainWindow
from .register_window import RegisterWindow

from config.colors import AppleColors
from components.button import Button


class LoginWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # controller instance
        self.auth_controller = AuthController()

        # create layout
        self.setWindowTitle("Sign In")
        self.setFixedSize(400, 300)

        main_layout = QtWidgets.QVBoxLayout()
        register_layout = QtWidgets.QHBoxLayout()
        self.setLayout(main_layout)

        # signin label
        self.signin_label = QtWidgets.QLabel("Sign in to Account")
        self.signin_label.setStyleSheet(
            f"QLabel {{ font-size: 18px; font-weight: bold; }}"
        )

        # username QLine edit
        self.username_edit = QtWidgets.QLineEdit(placeholderText="Username")
        self.username_edit.setMinimumHeight(30)

        # password QLine edit
        self.password_edit = QtWidgets.QLineEdit(placeholderText="Password")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_edit.setMinimumHeight(30)

        # submit btn
        self.login_btn = Button(text="Sign In")

        # register btn
        self.register_txt = QtWidgets.QLabel("Don't have an account?")
        self.register_txt.setStyleSheet(f"QLabel {{ color: {AppleColors.GRAY}; }}")
        self.register_btn = Button(text="Register", type="text")

        # connects
        self.login_btn.clicked.connect(self.handle_login)
        self.register_btn.clicked.connect(self.handle_register)

        # add widgets to main layout
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(10)

        main_layout.addWidget(
            self.signin_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        main_layout.addSpacing(20)
        main_layout.addWidget(self.username_edit)
        main_layout.addWidget(self.password_edit)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.login_btn)

        register_layout.addStretch()
        register_layout.addWidget(self.register_txt)
        register_layout.addWidget(self.register_btn)
        register_layout.addStretch()

        main_layout.addLayout(register_layout)

    def handle_login(self):
        """open main window"""
        username = self.username_edit.text()
        password = self.password_edit.text()
        auth = AuthController()

        success = auth.login(username=username, password=password)

        if success:
            print("Wellcome {0}!".format(username))
            self.main_window = MainWindow(username)
            self.main_window.show()
            self.close()
        else:
            print("invalid User!")

    def handle_register(self):
        """open register window"""
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.hide()
