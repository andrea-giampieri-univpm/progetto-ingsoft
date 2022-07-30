import datetime
import os
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.Viste.Blocks.BlockElementoComandaSala import BlockElementoComandaSala
from RistoMatic.Viste.VistaAggiungiElemento import VistaAggiungiElemento


class BlockComandaSala(QtWidgets.QGroupBox):

    def __init__(self, comanda: Comanda):
        super().__init__()
        self.comanda = comanda

        if (isinstance(comanda.rif, Tavolo)):
            self.setTitle(
                f"Comanda {comanda.numeroComanda} - Tavolo {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
        else:
            self.setTitle(
                f"Comanda {comanda.numeroComanda} - Asporto {comanda.rif.getNumeroOrdine()} - {comanda.rif.getOraConsegna()}")
            self.setStyleSheet("QGroupBox {background-color: yellow;}")

        self.setMinimumWidth(300)

        self.vbox = QVBoxLayout()
        self.addbtn = QPushButton("Aggiungi elemento")
        self.addbtn.clicked.connect(self.aggiungi_elemento)
        self.vbox.addWidget(self.addbtn)
        # self.vbox.addStretch(1)
        self.list = QVBoxLayout()

        for elemento in comanda.elementiComanda:
            block = BlockElementoComandaSala(elemento)
            block.aggiorna_comanda.connect(self.aggiorna_totale)
            block.elimina_elemento.connect(self.elimina_elemento)
            self.list.addLayout(block)

        self.vbox.addLayout(self.list)
        self.totline = QHBoxLayout()
        self.coperto = QLabel("Coperto: " + str(self.comanda.getCostoCoperto()) + " €  ")
        self.tot = QLabel("Totale: " + str(self.comanda.getTotale()) + " €")
        self.tot.setStyleSheet("QLabel {font-size:16px; font-weight: bold}")
        self.totline.addWidget(self.coperto)
        self.totline.addWidget(self.tot)
        self.totline.setAlignment(Qt.AlignRight)
        self.vbox.addLayout(self.totline)
        self.stampa = QPushButton("Stampa preconto")
        self.stampa.clicked.connect(self.stampa_preconto)
        self.vbox.addWidget(self.stampa)
        self.setLayout(self.vbox)

        self.waggiungi = None

    def aggiorna_totale(self):
        self.coperto.setText("Coperto: " + str(self.comanda.getCostoCoperto()) + " €  ")
        self.tot.setText("Totale: " + str(self.comanda.getTotale()) + " €")

    def aggiungi_elemento(self):
        self.waggiungi = VistaAggiungiElemento(self.comanda)
        self.waggiungi.update_ui.connect(self.aggiungi_block)
        self.waggiungi.show()

    def aggiungi_block(self):
        block = BlockElementoComandaSala(self.comanda.elementiComanda[-1])
        block.aggiorna_comanda.connect(self.aggiorna_totale)
        block.elimina_elemento.connect(self.elimina_elemento)
        self.list.addLayout(block)
        self.aggiorna_totale()

    def elimina_elemento(self, elemento):
        self.comanda.rimuoviElementoComanda(elemento)

    def stampa_preconto(self):

        try:
            file_object = open("Dati/ComandaDaStampare.txt", 'w')

            file_object.write(
                '****************************** PIZZERIA AMADEUS ******************************************')
            file_object.write('\n')
            file_object.write('\n')
            file_object.write('Località: Termoli, Molise Cb')
            file_object.write('\n')
            file_object.write('data: ')
            file_object.write(datetime.date.today().strftime('%d %b %Y'))
            file_object.write('\n')
            file_object.write('\n')
            file_object.write('        quant.' + '  prz sing pezz.')
            file_object.write('\n')

            for elemento in self.comanda.elementiComanda:
                file_object.write('*) ' + elemento.getInfoElementoComanda().get('Nome') + '   ')
                file_object.write('x' + str(elemento.getInfoElementoComanda().get('Quantita')) + '  ')
                file_object.write(str(elemento.getInfoElementoComanda().get('Prezzo')) + '  ')
                file_object.write('\n')

            file_object.write('\n')
            file_object.write('\n')
            print(self.comanda.getCostoCoperto())
            if (self.comanda.getCostoCoperto() != 0):
                file_object.write('\n')
                file_object.write('Costo totale coperto:  ' + str(round(self.comanda.getCostoCoperto(), 1)))
            file_object.write('\n')
            file_object.write('Totale:    ' + str(round(self.comanda.getTotale(), 2)) + '€')
            file_object.write('\n')
            file_object.write('\n')
            file_object.write('***************************************************************************************')
            file_object.close()

# TODO LUCA : TROVARE SE POSSIBILE UNA SOLUZIONE PER STAMPARE IL PRECONTO !
        #    os.startfile("./RistoMatic/Dati/ComandaDaStampare.txt", "print")



        except FileNotFoundError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ERRORE !")
            msg.setInformativeText("File: ComandaDaStampare.txt non presente nella dir: 'RistoMatic/Dati'")
            msg.exec()

        # pass #manda i dati alla stampante
