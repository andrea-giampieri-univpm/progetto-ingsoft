from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.Viste.Blocks.BlockElementoComandaAsporto import BlockElementoComandaAsporto
from RistoMatic.Viste.Blocks.BlockElementoComandaSala import BlockElementoComandaSala
from RistoMatic.Viste.VistaAggiungiElemento import VistaAggiungiElemento

class BlockComandaAsporto(QtWidgets.QGroupBox):

    def __init__(self, ordine: OrdineAsporto, callback):
        super().__init__()
        self.callback = callback
        self.ordine = ordine
        self.comanda = ordine.comanda

        self.setMinimumWidth(300)
        self.setTitle(f"Nome ordine: {ordine.cliente.nomeCliente}, Ora consegna: {ordine.oraConsegna}, cell: {ordine.cliente.recapitoTelefonico}, ID: {ordine.id}")
        self.vbox = QVBoxLayout()

        self.addbtn = QPushButton("Aggiungi elemento")
        self.addbtn.clicked.connect(self.aggiungi_elemento)
        self.vbox.addWidget(self.addbtn)

        self.list = QVBoxLayout()

        for elemento in self.comanda.elementiComanda:
            block = BlockElementoComandaAsporto(elemento)
#             block.aggiorna_comanda.connect(self.aggiorna_totale)
            block.aggiornaComanda.connect(self.aggiorna_totale)
            block.aggiornaComanda.connect(self.aggiorna_totale)
#            block.elimina_elemento.connect(self.elimina_elemento)
            block.eliminaElemento.connect(self.elimina_elemento)
            self.list.addLayout(block)

        self.vbox.addLayout(self.list)
        self.totline = QHBoxLayout()

        self.tot = QLabel("Totale: "+ str(self.ordine.getTotale()) +" €")
        self.tot.setStyleSheet("QLabel {font-size:16px; font-weight: bold}")


        self.totline.addWidget(self.tot)
        self.totline.setAlignment(Qt.AlignRight)
        self.vbox.addLayout(self.totline)

        self.stampa = QPushButton("Stampa Conto")
        self.stampa.clicked.connect(self.stampa_preconto)
        self.vbox.addWidget(self.stampa)

        self.delbutton = QPushButton("Elimina Ordine")

        self.delbutton.setStyleSheet("QPushButton {background-color: #f76f6f;}")
        self.delbutton.clicked.connect(self.elimina_ordine)
        self.vbox.addWidget(self.delbutton)
        self.setLayout(self.vbox)

        self.waggiungi=None

    def aggiorna_totale(self):
        self.tot.setText("Totale: "+ str(self.ordine.getTotale()) +" €")

    def aggiungi_elemento(self):
        self.waggiungi=VistaAggiungiElemento(self.comanda)
        self.waggiungi.update_ui.connect(self.aggiungi_block)
        self.waggiungi.show()

    def aggiungi_block(self):
        block = BlockElementoComandaAsporto(self.comanda.elementiComanda[-1])
        block.aggiornaComanda.connect(self.aggiorna_totale)
        block.eliminaElemento.connect(self.elimina_elemento)
        self.list.addLayout(block)
        self.aggiorna_totale()


    def elimina_elemento(self,elemento):
        self.comanda.rimuoviElementoComanda(elemento)


    def elimina_ordine(self):
        StatoSala.rimuoviOrdineAsporto(self.ordine)
        self.callback()

    def stampa_preconto(self):
        pass #manda i dati alla stampante

