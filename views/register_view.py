import re

from PySide6 import QtWidgets, QtCore

from components.button import Button
from components.dialog import InfoMessage, SuccessMessage
from controllers.auth_controller import AuthController

studio_depts = [
    "Production",
    "Layout / Matchmove",
    "Modeling",
    "Texturing / Surfacing",
    "Rigging",
    "Animation",
    "FX / Simulation",
    "Lighting",
    "Rendering",
    "Compositing",
    "Roto / Paint",
    "Pipeline / TD",
    "Editorial",
    "IT / Render Farm",
]


class RegisterWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register")
        self.setFixedSize(400, 500)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # label
        self.register_label = QtWidgets.QLabel("Register account")
        self.register_label.setStyleSheet(
            f"QLabel {{ font-size: 18px; font-weight: bold; }}"
        )

        # username edit
        self.username_edit = QtWidgets.QLineEdit(placeholderText="Username")
        self.username_edit.setMinimumHeight(30)

        # email edit
        self.email_edit = QtWidgets.QLineEdit(placeholderText="Email")
        self.email_edit.setMinimumHeight(30)

        # dept combobox
        self.dept_combo = QtWidgets.QComboBox()
        self.dept_combo.addItems(studio_depts)
        self.dept_combo.setMinimumHeight(30)

        # password edit
        self.password_edit = QtWidgets.QLineEdit(placeholderText="Password")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_edit.setMinimumHeight(30)

        # buttons
        self.register_btn = Button(text="Register")
        self.login_btn = Button(
            text="Return to login", type="text", variant="secondary"
        )

        # add widgets to layout
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(10)

        layout.addStretch()
        layout.addWidget(
            self.register_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        layout.addSpacing(20)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.dept_combo)
        layout.addWidget(self.password_edit)
        layout.addStretch()
        layout.addWidget(self.register_btn)
        layout.addWidget(self.login_btn)

        # connect
        self.login_btn.clicked.connect(self.handle_open_login)
        self.register_btn.clicked.connect(self.handle_register_user)

    def handle_open_login(self):
        from .login_view import LoginWindow

        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def handle_register_user(self):
        from .login_view import LoginWindow

        self.login_window = LoginWindow()

        username = self.username_edit.text()
        email = self.email_edit.text()
        deparment = self.dept_combo.currentText()
        password = self.password_edit.text()

        auth = AuthController()

        register_result = auth.register(username, email, deparment, password)

        if register_result.success:
            SuccessMessage(msg=register_result.message).exec()
            self.login_window.show()
            self.close()
        else:
            InfoMessage(msg=register_result.message).exec()
