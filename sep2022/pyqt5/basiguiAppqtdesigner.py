#pyqt5 imports
from PyQt5.QtWidgets import *
from PyQt5 import uic

#custon imports

#Clase principal
class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("myui.ui", self) #aca llamanos al archivo .ui generado por qtdesigner
        self.show()

    #Codigo custon  








def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()
