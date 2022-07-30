from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QAbstractItemView, QPushButton, QLineEdit
from PySide6.QtWidgets import QLabel, QVBoxLayout, QListWidget
from RistoMatic.GestioneAttivita.Enum import Zone
from RistoMatic.Viste.Blocks.BlockElementoComandaSala import BlockElementoComandaSala
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.Viste.Blocks.BlockMenuItem import BlockMenuItem
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class VistaAggiungiElemento(QtWidgets.QWidget):

    update_ui = Signal()

    def __init__(self, comanda: Comanda):
        super().__init__()
        self.comanda = comanda
        self.setWindowTitle(f"Aggiungi elemento da menu a comanda {self.comanda.getNumeroComanda()}")

        self.resize(540, 640)
        self.list = QListWidget()
        self.list.clicked.connect(self.onclick)
        self.list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.list.setSelectionMode(QAbstractItemView.SingleSelection)

        menu = StatoSala.getMenuAttivo().getListaElementi()
        for elementomenu in menu:
            item = BlockMenuItem(menu[elementomenu])
            self.list.addItem(item)

        self.elementocomanda=None

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(f"Menu attivo: {StatoSala.getMenuAttivo().getNomeMenu()}"))
        self.layout.addWidget(self.list)


        self.setLayout(self.layout)
        self.btn=None
        self.note=None
        self.elemento = None

    def onclick(self):
        selected = self.list.selectedItems()
        for selection in selected:
            self.elementocomanda = ElementoComanda(selection.getData(),"",1)
        self.block=BlockElementoComandaSala(self.elementocomanda)
        self.layout.addLayout(self.block)
        self.btn=QPushButton("aggiungi")
        self.note = QLineEdit()
        self.layout.addWidget(self.note)
        self.btn.clicked.connect(self.aggiungi)
        self.layout.addWidget(self.btn)

    def aggiungi(self):
        self.elementocomanda.setNote(self.note.text())
        self.comanda.aggiungiElementoComanda(self.elementocomanda)
        self.update_ui.emit()
        self.close()
