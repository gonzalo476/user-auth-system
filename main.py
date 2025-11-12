import sys
from PySide6 import QtWidgets

from views.login_window import LoginWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    app.exec()
