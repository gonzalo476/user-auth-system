from PySide6 import QtWidgets, QtCore

from controllers.auth_controller import AuthController
from .main_window import MainWindow

from config.colors import AppleColors


class LoginWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # controller instance
        self.auth_controller = AuthController()

        # create layout
        self.setWindowTitle("Sign In")
        self.setMinimumSize(400, 300)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # signin label
        self.signin_label = QtWidgets.QLabel("Sign In")

        # username QLine edit
        self.username_edit = QtWidgets.QLineEdit(placeholderText="Username")
        self.username_edit.setMinimumHeight(30)

        # password QLine edit
        self.password_edit = QtWidgets.QLineEdit(placeholderText="Password")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_edit.setMinimumHeight(30)

        # submit btn
        self.login_btn = QtWidgets.QPushButton("LogIn")
        self.login_btn.setStyleSheet(
            f"""
                QPushButton {{
                    background-color: {AppleColors.BLUE};
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 10px 20px;
                    font-size: 14px;
                }}
                QPushButton:hover {{
                    background-color: #0051D5;
                }}
                QPushButton:pressed {{
                    background-color: #004BB8;
                }}
            """
        )

        # connects
        self.login_btn.clicked.connect(self.handle_login)

        # add widgets to layout
        layout.setContentsMargins(50, 50, 50, 50)
        layout.addWidget(self.signin_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_edit)
        layout.addSpacing(30)
        layout.addWidget(self.login_btn)

    def handle_login(self):
        """User auth on clicked"""
        username = self.username_edit.text()
        password = self.password_edit.text()

        success = self.auth_controller.login(username, password)

        if success:
            print("Wellcome {0}!".format(username))
            self.main_window = MainWindow(username)
            self.main_window.show()
            self.close()
        else:
            print("invalid User!".format(username))
