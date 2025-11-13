from PySide6 import QtWidgets

from models.user import User


class MainWindow(QtWidgets.QWidget):

    def __init__(self, user: User):
        super().__init__()
        self.user = user
        self.setWindowTitle("Account")
        self.setMinimumSize(400, 300)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.welcome_label = QtWidgets.QLabel(f"Hello {self.user.username}!", self)
        self.dept_label = QtWidgets.QLabel(f"{self.user.department}", self)
        self.email_label = QtWidgets.QLabel(f"{self.user.email}", self)

        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(10)
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.dept_label)
        layout.addWidget(self.email_label)
