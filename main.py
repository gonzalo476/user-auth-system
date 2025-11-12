import sys
from PySide6 import QtWidgets

from views.main_window import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
