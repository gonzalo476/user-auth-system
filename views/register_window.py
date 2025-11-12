from PySide6 import QtWidgets

from components.button import Button


class RegisterWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register")
        self.setMinimumSize(400, 600)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.login_btn = Button(text="Return to login", type="text")

        layout.addWidget(self.login_btn)

        self.login_btn.clicked.connect(self.handle_open_login)

    def handle_open_login(self):
        from .login_window import LoginWindow

        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
