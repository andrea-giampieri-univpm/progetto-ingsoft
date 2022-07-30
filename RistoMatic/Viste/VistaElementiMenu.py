from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QListView
from RistoMatic.Viste.VistaAggiungiElementoMenu import VistaAggiungiElementoMenu


class VistaElementiMenu(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.aggiorna()

        self.buttonsLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.aggiungiElemento = QPushButton('Aggiungi elemento')
        self.aggiungiElemento.clicked.connect(self.addElemento)

        self.eliminaElemento = QPushButton('Rimuovi Elemento')
        self.eliminaElemento.clicked.connect(self.deleteElemento)


        self.buttonsLayout.addWidget(self.aggiungiElemento)
        self.buttonsLayout.addWidget(self.eliminaElemento)
        self.vLayout.addLayout(self.buttonsLayout)

        self.listView = QListView()
        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)



    def addElemento(self):
        self.vistaElemento = VistaAggiungiElementoMenu()
        self.vistaElemento.setWindowTitle('Elemento menù')
        self.vistaElemento.show()

    def deleteElemento(self):
        pass


    def aggiorna(self):
        pass


