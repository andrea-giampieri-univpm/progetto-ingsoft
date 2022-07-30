from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView, QLineEdit, QLabel
from PySide6.QtGui import QStandardItemModel, QStandardItem, QCloseEvent

from RistoMatic.GestioneAttivita.Enum import Zone
from RistoMatic.Viste.VistaAggiungiElementoMenu import VistaAggiungiElementoMenu
from RistoMatic.GestioneAttivita.StatoSala import StatoSala


class VistaMenu(QtWidgets.QWidget):

    def __init__(self, key):
        super().__init__()

        self.key = key

        self.resize(600, 600)

        self.menu = StatoSala.cercaMenu(self.key)
        self.vLayout = QVBoxLayout()
        self.listView = QListView()
        self.qlines = {}
        self.addInfoText("nomeMenu", "Nome menù: ")

        self.aggiungiElemento = QPushButton('Nuova pietanza')
        self.aggiungiElemento.clicked.connect(self.addElementoMenu)
        self.vLayout.addWidget(self.aggiungiElemento)

        self.eliminaElemento = QPushButton('Elimina pietanza')
        self.eliminaElemento.clicked.connect(self.deleteElementoMenu)
        self.vLayout.addWidget(self.eliminaElemento)

        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)

        self.update_ui()

    def update_ui(self):
        listViewModel = QStandardItemModel(self.listView)
        listaelementi = self.menu.getListaElementi()
        if len(listaelementi) > 0:
            for key in listaelementi:
                qItem = QStandardItem()

                zona = listaelementi[key].getAreaPreparazione()
                text=""
                if (zona == Zone.CUCINA):
                    text = "Cucina"
                elif (zona == Zone.BAR):
                    text = "Bar"
                elif (zona == Zone.FORNO):
                    text = "Forno"
                titolo = f"{listaelementi[key].getNomeElemento()}, prezzo: {listaelementi[key].getPrezzoElemento()}, Zona: {text}"
                qItem.setText(titolo)
                qItem.setEditable(False)
                font = qItem.font()
                font.setPointSize(20)
                qItem.setFont(font)
                listViewModel.appendRow(qItem)
            self.listView.setModel(listViewModel)


    def addElementoMenu(self):
        cb=self.update_ui
        self.vistaAggiungiElementoMenu = VistaAggiungiElementoMenu(self.menu,cb)
        self.vistaAggiungiElementoMenu.setWindowTitle('Aggiungi pietanza / bevanda')
        self.vistaAggiungiElementoMenu.show()

    def deleteElementoMenu(self):
        selected = self.listView.selectedIndexes()[0].data()
        key = selected.split(', ')[0].strip()
        self.menu.getListaElementi().pop(key)
        self.update_ui()

    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))

    def closeEvent(self, event: QCloseEvent) -> None:
        StatoSala.rimuoviMenu(self.key)
        StatoSala.aggiungiMenu(self.menu)