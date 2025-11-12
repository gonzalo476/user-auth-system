from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__(parent=None)

        # create layout
        self.setWindowTitle("Main Window")
        self.setMinimumSize(400, 300)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # sign in label
        signin_label = QtWidgets.QLabel("Sign In")

        # username QLine edit
        username_edit = QtWidgets.QLineEdit(placeholderText="Username")

        # password QLine edit
        password_edit = QtWidgets.QLineEdit(placeholderText="Password")

        # submit btn
        login_btn = QtWidgets.QPushButton("LogIn")
        login_btn.setMaximumWidth(75)

        # add widgets to layout
        layout.setContentsMargins(50, 50, 50, 50)
        layout.addWidget(signin_label)
        layout.addWidget(username_edit)
        layout.addWidget(password_edit)
        layout.addWidget(login_btn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
