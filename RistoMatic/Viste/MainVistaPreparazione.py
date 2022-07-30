from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from RistoMatic.Viste.FlowLayout import FlowLayout
from RistoMatic.Viste.Blocks.BlockComandaPreparazione import BlockComandaPreparazione
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.GestioneAmministrativa.Menu import Menu
from RistoMatic.GestioneAttivita.Enum import StatoComanda
from random import *

class VistaPreparazione(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vista Preparazione")

        StatoSala.start()

        self.layout = FlowLayout(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiorna)
        self.timer.start(5000)

        lista=StatoSala.getListaComande()
        for comanda in lista:
            if not comanda.getStato() == StatoComanda.COMPLETATA:
                self.layout.addWidget(BlockComandaPreparazione(comanda))
        if self.layout.count()==0:
            self.layout.addWidget(QtWidgets.QLabel("Nessuna comanda presente"))

    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        lista=StatoSala.getListaComande()
        for comanda in lista:
            if not comanda.getStato()==StatoComanda.COMPLETATA:
                self.layout.addWidget(BlockComandaPreparazione(comanda))
        if self.layout.count() == 0:
            self.layout.addWidget(QtWidgets.QLabel("Nessuna comanda presente"))
