from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QAbstractItemView, QPushButton, QLineEdit
from PySide6.QtWidgets import QLabel, QVBoxLayout, QListWidget
from RistoMatic.GestioneAttivita.Enum import Zone
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.Viste.Blocks.BlockElementoComandaAsporto import BlockElementoComandaAsporto
from RistoMatic.Viste.Blocks.BlockElementoComandaSala import BlockElementoComandaSala
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.Viste.Blocks.BlockMenuItem import BlockMenuItem
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class VistaAggiungiElementoAsporto(QtWidgets.QWidget):

    update_ui = Signal()

    def __init__(self, ordine: OrdineAsporto):
        super().__init__()
        self.ordine = ordine
        self.setWindowTitle(f"Aggiungi elemento da menu a ordine asporto {self.ordine.comanda.getNumeroComanda()}")

        self.resize(540, 640)
        self.list = QListWidget()
        self.list.clicked.connect(self.onclick)
        self.list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.list.setSelectionMode(QAbstractItemView.SingleSelection)

        menu = StatoSala.getMenuAttivo().getListaElementi()
        for elementomenu in menu:
            item = BlockMenuItem(menu[elementomenu])
            self.list.addItem(item)

        self.elementoOrdine=None

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(f"Menu attivo: {StatoSala.getMenuAttivo().getNomeMenu()}"))
        self.layout.addWidget(self.list)


        self.setLayout(self.layout)
        self.button=None
        self.note=None
        self.elemento = None

    def onclick(self):
        selected = self.list.selectedItems()
        for selection in selected:
            self.elementocomanda = ElementoComanda(selection.getData(),"",1)
        self.block=BlockElementoComandaAsporto(self.elementocomanda)
        self.layout.addLayout(self.block)
        self.button = QPushButton("Aggiungi")
        self.note = QLineEdit()
        self.layout.addWidget(self.note)
        self.button.clicked.connect(self.aggiungiElemento)
        self.layout.addWidget(self.button)

    def aggiungiElemento(self):
        self.elementocomanda.setNote(self.note.text())
        self.ordine.comanda.aggiungiElementoComanda(self.elementocomanda)
        self.update_ui.emit()
        self.close()
