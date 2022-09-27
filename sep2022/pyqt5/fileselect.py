#pyqt5 imports
from PyQt5.QtWidgets import *
from PyQt5 import uic

#custon imports
from cryptography.fernet import Fernet



#Clase principal
class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("selectfile.ui", self) #aca llamanos al archivo .ui generado por qtdesigner
        self.show()

    #Codigo custon  
        self.seleccionar.clicked.connect(self.getfile)
        self.encryptButton.clicked.connect(self.encrypt)
    


    def getfile(self):
        #print('click')
        filename = QFileDialog.getOpenFileName(self, 'Open file',)
        #print(filename[0])
        self.seleccion.setText(filename[0])


    def encrypt(self):
        file_path = self.seleccion.text()
        key = Fernet.generate_key()
        print(key)
        f = Fernet(key)
        #read the file to be encrypted
        myfile = open(file_path, "rb")
        file_data = myfile.read()
        encrypted_data = f.encrypt(file_data)
        
        #write the filedata to a crypted file
        myfile_two = open(file_path, "wb")
        myfile_two.write(encrypted_data)
        myfile_two.close()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()
