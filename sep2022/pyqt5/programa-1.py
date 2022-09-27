from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

#necesario para acceder a los argumentos de linea de comando
import sys

app = QApplication(sys.argv)

#creamos el widget que sera nuestra ventana principal
window = QMainWindow()
window.show()


app.exec_()
