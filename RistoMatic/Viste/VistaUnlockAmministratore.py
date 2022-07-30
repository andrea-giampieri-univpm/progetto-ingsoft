import sys
from PySide6.QtWidgets import QTabWidget, QVBoxLayout, QScrollArea , QWidget, QGridLayout, QLabel, QLineEdit,QPushButton, QMessageBox, QListView
from PyQt5 import sip
from RistoMatic.Viste.MainVistaSala import VistaSala
from cryptography.fernet import Fernet


class VistaUnlockAmministratore(QWidget):



    def __init__(self):
        super().__init__()
        self.setWindowTitle('Accesso Amministratore')
        self.resize(500, 120)

        layout = QGridLayout()

        self.label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Inserisci il nome-utente')
        layout.addWidget(self.label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        self.label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Inserisci la tua password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        self.button_login = QPushButton('Accedi')
        self.button_login.clicked.connect(self.check_password)
        layout.addWidget(self.button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

# Nome-utente : a , password: 1234
    def check_password(self):
        check = None
        msg = QMessageBox()
# Idea : creo una password dinamica , che cambia sempre , così non la devo salvare ma è comunque sicura, inutile leggere il nome utente
        key = Fernet.generate_key()
        fernet = Fernet(key)
        psw = fernet.encrypt(self.lineEdit_password.text().encode())

#  Leggo la passowrd in esadecimale , dopodiche la converto e la cripto , contemporaneamente
        try:
          with open('Dati/dati.txt') as file:
               contenuto = file.read().rstrip()
        except:
            msg.setWindowTitle('ERRORE')
            msg.setText('FILE NON PRESENTE O NELLA DIRECTORY SBAGLIATA !(esatta: Dati/dati.txt)')
            msg.exec()
            return
        try:
            n = int(contenuto,16)
            check = True
        except ValueError:
            check = False

        if contenuto == '' or check is False :
            msg.setWindowTitle('ERRORE')
            msg.setText('errore nella lettura del file: Dati/dati.tx !')
            msg.exec()
            return

        pswDaConfrontare = fernet.encrypt(str(int(str(contenuto), 16)).encode())
        if self.lineEdit_username.text()=='a' and fernet.decrypt(psw).decode()==fernet.decrypt(pswDaConfrontare).decode():

            self.button_login.deleteLater()
            self.lineEdit_password.deleteLater()
            self.label_password.deleteLater()
            self.lineEdit_username.deleteLater()
            self.label_name.deleteLater()
            self.label_password.deleteLater()

            msg.setText('Autenticazione effettuata ! Buon lavoro')
            msg.exec()
            from RistoMatic.Viste.VistaAmministratore import VistaAmministratore
            self.vistaAmministratore = VistaAmministratore()
            self.layout().addWidget(self.vistaAmministratore)



            #self.vistaAmministratore.show()


            #self.destroy(True)

        else:
             msg.setText('Ops ! Qualcosa è andato storto , riprova !')
             msg.exec()





