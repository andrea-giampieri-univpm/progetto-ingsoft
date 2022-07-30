from RistoMatic.Viste.FlowLayout import FlowLayout
from random import *
from RistoMatic.Viste.Blocks.BlockTavolo import BlockTavolo
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from PySide6 import QtWidgets
from PySide6.QtCore import Signal,Slot, QTimer

class VistaTavoli(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.layout = FlowLayout(self)
        #self.timer = QTimer()
        #self.timer.timeout.connect(self.aggiornaUi)
        #self.timer.start(5000)
        self.aggiornaUi()

    def aggiornaUi(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for tavolo in StatoSala.Tavoli:
            self.layout.addWidget(BlockTavolo(tavolo))


