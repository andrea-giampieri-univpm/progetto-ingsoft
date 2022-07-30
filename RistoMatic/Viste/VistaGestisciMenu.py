import pickle

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QListView, QVBoxLayout, QLabel
from PySide6 import QtWidgets


from RistoMatic.Viste.VistaAggiungiMenu import VistaAggiungiMenu
from RistoMatic.Viste.VistaModificaMenu import VistaMenu
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class VistaGestisciMenu(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gestione dei menù')
        self.resize(1000, 600)
        self.listView = QListView()



        self.buttonsLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.aggiungiMenu = QPushButton('Aggiungi menù')
        self.aggiungiMenu.clicked.connect(self.addMenu)

        self.eliminaMenu = QPushButton('Elimina menù')
        self.eliminaMenu.clicked.connect(self.deleteMenu)

        self.scegliMenu = QPushButton('Imposta come attivo')
        self.scegliMenu.clicked.connect(self.selectMenu)

        self.modificaMenu = QPushButton('Modifica menu')
        self.modificaMenu.clicked.connect(self.updateMenu)

        self.buttonsLayout.addWidget(self.aggiungiMenu)
        self.buttonsLayout.addWidget(self.eliminaMenu)
        self.buttonsLayout.addWidget(self.scegliMenu)
        self.buttonsLayout.addWidget(self.modificaMenu)
        self.vLayout.addLayout(self.buttonsLayout)

        self.attivo = QLabel(f"Attivo: {StatoSala.getMenuAttivo().getNomeMenu()}")
        self.vLayout.addWidget(self.attivo)
        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)

        self.update_ui()

    def update_ui(self):
        listViewModel = QStandardItemModel(self.listView)
        dictMenu = StatoSala.getDictMenu()
        if len(dictMenu) > 0:
            for key in dictMenu.keys():
                qItem = QStandardItem()
                titolo = f"{key}, costo coperto: {dictMenu[key].getCostoCoperto()}"
                qItem.setText(titolo)
                qItem.setEditable(False)
                font = qItem.font()
                font.setPointSize(20)
                qItem.setFont(font)
                listViewModel.appendRow(qItem)
            self.listView.setModel(listViewModel)

    def addMenu(self):
        cb = self.update_ui
        self.vistaAggiungiMenu = VistaAggiungiMenu(cb)
        self.vistaAggiungiMenu.setWindowTitle('Menù')
        self.vistaAggiungiMenu.show()

    def deleteMenu(self):
        selected = self.listView.selectedIndexes()[0].data()
        key = selected.split(', ')[0].strip()
        if not key == "Default":
            StatoSala.rimuoviMenu(key)
        self.update_ui()

    def selectMenu(self):
        selected = self.listView.selectedIndexes()[0].data()
        key = selected.split(', ')[0].strip()
        StatoSala.setMenuAttivo(key)
        self.attivo.setText(f"Attivo: {StatoSala.getMenuAttivo().getNomeMenu()}")


# Clicco sul menù con il mouse e dopo premendo il pulsante AGGIORNA , lo vado a modificare
    def updateMenu(self):
        selected = self.listView.selectedIndexes()[0].data()
        key = selected.split(', ')[0].strip()
        self.modificaMenu = VistaMenu(key)
        self.modificaMenu.setWindowTitle('Menù')
        self.modificaMenu.show()

