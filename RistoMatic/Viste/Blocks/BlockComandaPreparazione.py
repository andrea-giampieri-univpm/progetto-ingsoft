from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Slot,Signal
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.Enum import Zone
from RistoMatic.Viste.Blocks.BlockElementoComandaPreparazione import BlockElementoComandaPreparazione
from RistoMatic.GestioneAttivita.Tavolo import Tavolo

class BlockComandaPreparazione(QtWidgets.QGroupBox):

    def __init__(self, comanda: Comanda):
        if(isinstance(comanda.rif,Tavolo)):
            super().__init__(f"Comanda {comanda.numeroComanda} - Tavolo {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
        else:
            super().__init__(f"Comanda {comanda.numeroComanda} - Asporto {comanda.rif.getNumeroOrdine()} - {comanda.rif.getOraConsegna()}")
            self.setStyleSheet("QGroupBox {background-color: yellow;}")
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)

        for elem in comanda.elementiComanda:
               if not elem.getIsPronta() and elem.elemento.getAreaPreparazione()==Zone.CUCINA:
                  btn = BlockElementoComandaPreparazione(elem)
                  self.vbox.addWidget(btn)

        self.setLayout(self.vbox)

