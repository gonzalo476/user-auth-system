from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__(parent=None)

        # crear un layout
        self.setWindowTitle("Main Window")
        self.setMinimumSize(400, 300)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # red
        red = QtWidgets.QLabel("Red")
        red.setStyleSheet("background-color: red; padding: 20px;")

        # green
        green = QtWidgets.QLabel("Green")
        green.setStyleSheet("background-color: green; padding: 20px;")

        # blue
        blue = QtWidgets.QLabel("Blue")
        blue.setStyleSheet("background-color: blue; padding: 20px;")

        # add colors to layout
        layout.addWidget(red)
        layout.addWidget(green)
        layout.addWidget(blue)
