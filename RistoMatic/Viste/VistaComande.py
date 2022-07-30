from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

from RistoMatic.Viste.Blocks.BlockComandaSala import BlockComandaSala
from RistoMatic.Viste.FlowLayout import FlowLayout

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from random import *

class VistaComande(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.layout = FlowLayout(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiorna)
        self.timer.start(5000)

        for comanda in StatoSala.getListaComande():
            self.layout.addWidget(BlockComandaSala(comanda))

    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for comanda in StatoSala.getListaComande():
            self.layout.addWidget(BlockComandaSala(comanda))
