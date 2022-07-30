from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QListView
from PySide6.examples.widgets.layouts.flowlayout.flowlayout import FlowLayout

from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.Viste.Blocks.BlockNuovoOrdineAsporto import BlockNuovoOrdineAsporto
from RistoMatic.Viste.Blocks.BlockComandaAsporto import BlockComandaAsporto
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

from RistoMatic.Viste.Blocks.BlockComandaSala import BlockComandaSala
from RistoMatic.Viste.FlowLayout import FlowLayout

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from random import *

class VistaAsporto(QWidget):
    def __init__(self):
        super().__init__()


        self.layout = FlowLayout(self)
        self.aggiorna()

       # self.refresh = QTimer()
       # self.refresh.setInterval(5000)
       # self.refresh.timeout.connect(self.aggiorna)
       # self.refresh.start()

        self.hBox = QHBoxLayout()
        self.tasti = QVBoxLayout()
        self.vBox = QVBoxLayout()

        for ordine in StatoSala.getListaAsporto():
            self.layout.addWidget(BlockComandaAsporto(ordine, self.aggiorna()))
        self.aggiorna()


    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
        for ordine in StatoSala.getListaAsporto():
            self.layout.addWidget(BlockComandaAsporto(ordine, self.aggiorna))
        self.layout.addWidget(BlockNuovoOrdineAsporto(self.aggiorna))

