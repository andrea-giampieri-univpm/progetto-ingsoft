from PySide6 import QtWidgets
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QVBoxLayout, QPushButton

from RistoMatic.GestioneAttivita import OrdineAsporto
from RistoMatic.Viste.VistaAggiungiOrdineAsporto import VistaAggiungiOrdineAsporto


class BlockNuovoOrdineAsporto(QtWidgets.QGroupBox):

    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.setMinimumSize(300, 227)
        self.vbox = QVBoxLayout()

        self.addbtn = QPushButton("Aggiungi\nnuovo ordine ")
        self.addbtn.clicked.connect(self.aggiungiNuovoOrdine)
        self.addbtn.setMinimumSize(100, 100)
        self.addbtn.setFont(QFont('Times', 20))
    #   self.addbtn.setStyleSheet(
    #        "border: 2px solid black;"
    #        "border-radius: 50px;"
    #        "font-size: 35px;")

        self.addbtn.setStyleSheet("QPushButton {background-color: #98eda7;}")
        self.vbox.addWidget(self.addbtn)
        self.setLayout(self.vbox)

    def aggiungiNuovoOrdine(self):
        #print("aggiungiNuovoOrdine")
        self.nuovoOrdine = VistaAggiungiOrdineAsporto(callback=self.callback)
        ordine = self.nuovoOrdine.show()