import pickle

from PySide6 import QtWidgets
from PySide6.QtWidgets import QListView, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel

from RistoMatic.GestioneAmministrativa.Menu import Menu
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class VistaAggiungiMenu(QtWidgets.QWidget):

    def __init__(self, callback):
        super().__init__()

        self.callback=callback
        self.vLayout =QVBoxLayout()
        self.qlines = {}

        self.addInfoText("nomeMenu", "Nome Menu")
        self.addInfoText("costoCoperto", "Costo coperto")

        self.salvaMenu = QPushButton('Salva menu')
        self.salvaMenu.clicked.connect(self.saveMenu)
        self.vLayout.addWidget(self.salvaMenu)

        self.setLayout(self.vLayout)



    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)

# Li salva su un file .pickle contenuto nella cartella Dati del progetto
    def saveMenu(self):
        menu = Menu(self.qlines["nomeMenu"].text(),self.qlines["costoCoperto"].text())
        StatoSala.aggiungiMenu(menu)
        self.callback()
        self.close()


