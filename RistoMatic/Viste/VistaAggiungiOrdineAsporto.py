from typing import re

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione

class VistaAggiungiOrdineAsporto(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiOrdineAsporto, self).__init__()
        self.setWindowTitle('Nuova Prenotazione')
        self.callback = callback

        self.vLayout = QVBoxLayout()
        self.qlines = {}
        self.addInfoText("nome", "Nome")
        self.addInfoText("recapitoTelefonico", "Recapito Telefonico")
    #    self.addInfoText("oraConsegna", "Ora consegna")

        self.menuOra = QComboBox()
        orari = ['18:30', '18:45', '19:00','19:15', '19:30','19:45', '20:00','20:15', '20:30','20:45',
                 '21:00','21:15', '21:30','21:45', '22:00']
        self.menuOra.addItems(orari)
   #     self.addInfoText("oraOrdine", "oraOrdine")

        self.vLayout.addWidget(self.menuOra)
        okButton = QPushButton("OK")
        ordine = okButton.clicked.connect(self.aggiungiOrdine)
        self.qlines["okButton"] = okButton
        self.vLayout.addWidget(okButton)
        self.setLayout(self.vLayout)
        #self.callback()

    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)


    def aggiungiOrdine(self):
        self.cliente = Cliente("", "")
        self.ordine = OrdineAsporto(None, None, self.cliente)

# VEDERE SE METTERE WHILE O IF
        self.nome = self.qlines["nome"].text()
        self.recapitoTelefonico = self.qlines["recapitoTelefonico"].text()

        if (any(map(str.isdigit, self.nome)) is True  and any(map(str.isdigit, self.recapitoTelefonico)) is False) or (len(self.nome)==0 or len(self.recapitoTelefonico)==0):
            msg = QMessageBox()
            msg.setWindowTitle('ATTENZIONE!')
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ERRORE!")
            msg.setInformativeText("Compilazione ordine asporto ERRATA. Prestare attenzione !")
            msg.exec()
            return

        elif any(map(str.isdigit, self.nome)) is True:
            msg = QMessageBox()
            msg.setWindowTitle('ATTENZIONE!')
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ERRORE!")
            msg.setInformativeText("Il nome NON PUO contenere NUMERI")
            msg.exec()
            return

        elif any(map(str.isdigit, self.recapitoTelefonico)) is False:
            msg = QMessageBox()
            msg.setWindowTitle('ATTENZIONE!')
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ERRORE!")
            msg.setInformativeText("Il recapito-telefonico NON PUO contenere LETTERE")
            msg.exec()
            return

  #     self.oraConsegna = self.qlines["oraConsegna"].text()
        self.oraConsegna = self.menuOra.currentText()
        nOrdini = 0
        for i in StatoSala.OrdiniAsporto:
            if i.oraConsegna == self.oraConsegna:
                nOrdini += 1

            if nOrdini >= 4:
                msg = QMessageBox()
                msg.setWindowTitle('ATTENZIONE!')
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Ci sono già troppi ordini per quell'ora")
                msg.exec_()
                return


        self.ordine.setOraConsegna(self.oraConsegna)
        self.ordine.cliente.setNomeCliente(self.nome)
        self.ordine.cliente.setRecapitoTelefonico(self.recapitoTelefonico)

        StatoSala.aggiungiOrdineAsporto(self.ordine)
        self.callback()
        self.close()
