

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.click_function)

        self.setCentralWidget(button)

    def click_function(self):
        print("The button was clicked")
        self.setWindowTitle("otro titulo")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
