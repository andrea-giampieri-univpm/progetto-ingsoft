from PySide6.QtCore import Slot, Signal, QTimer
from PySide6 import QtWidgets
from random import *
from RistoMatic.Viste.FlowLayout import FlowLayout
from RistoMatic.Viste.Blocks.BlockTavolo import BlockTavolo
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Tavolo import Tavolo

class VistaMobile(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vista Mobile")

        self.layout = FlowLayout(self)
        #self.timer = QTimer()
        #self.timer.timeout.connect(self.aggiorna)
        #self.timer.start(5000)

        self.crea()

    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
        self.crea()

    def crea(self):
        for tavolo in StatoSala.getListaTavoli():
            btn = BlockTavolo(tavolo)
            self.layout.addWidget(btn)

