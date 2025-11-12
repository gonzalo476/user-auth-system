from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):

    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setMinimumSize(400, 300)

        self.welcome_label = QtWidgets.QLabel("Bienvenido {0}!".format(username), self)
