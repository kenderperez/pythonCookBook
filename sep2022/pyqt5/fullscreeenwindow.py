#pyqt5 imports
from PyQt5.QtWidgets import *
from PyQt5 import uic

#custon imports
from hashlib import md5
import pyperclip


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("myui.ui", self)
        self.setWindowTitle("md5 encriptador")

    #Codigo custon  
        self.encriptar.clicked.connect(self.clickfunction)

    def clickfunction(self):
        texto = self.texto.text()
        textoEncriptado = md5(texto.encode("utf-8")).hexdigest()
        self.textoencry.setText(textoEncriptado + " " + "copiado al portapapeles!")
        pyperclip.copy(textoEncriptado)
        self.texto.setText(textoEncriptado)







def main():
    app = QApplication([])
    window = MyGUI()
    window.showFullScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
