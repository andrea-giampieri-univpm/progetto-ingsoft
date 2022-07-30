import threading
import time

from PySide6 import QtWidgets
from PySide6.QtCore import QBasicTimer, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QListView
from PySide6.QtWidgets import QVBoxLayout

from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.Viste.VistaAggiungiPrenotazione import VistaAggiungiPrenotazione
from RistoMatic.Viste.VistaInfoPrenotazione import VistaInfoPrenotazione


class VistaPrenotazioni(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        hLayout = QHBoxLayout()

        self.aggiorna = QTimer()
        self.aggiorna.setInterval(5000)
        self.aggiorna.timeout.connect(self.aggiornaUi)
        self.aggiorna.start()

        self.listView = QListView()
        self.aggiornaUi()
        hLayout.addWidget(self.listView)

        buttonsLayout = QVBoxLayout()
        infoButton = QPushButton("Visualizza altro")
        infoButton.clicked.connect(self.visualizzaAltro)

        newButton = QPushButton("Aggiungi Prenotazione")
        newButton.clicked.connect(self.aggiungiPrenotazione)

        delButton = QPushButton("Elimina Prenotazione selezionata")
        delButton.clicked.connect(self.eliminaPrenotazione)

        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)
        buttonsLayout.addWidget(delButton)

        buttonsLayout.addStretch()
        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Prenotazioni")

    def aggiornaUi(self):
        listViewModel = QStandardItemModel(self.listView)

        StatoSala.Prenotazioni.sort(key=lambda x: x.cliente.getNomeCliente())  # mette in ordine alfabetico le prenotazioni riferendosi al nome dei clienti che le hanno effettuate

        for prenotazione in StatoSala.Prenotazioni:  # per ogni prenotazione crea una riga
            item = QStandardItem()
            titolo = f"{prenotazione.cliente.getNomeCliente()},  {prenotazione.dataPrenotazione},  Coperti: {prenotazione.getNumeroPersone()}, Tavolo: {prenotazione.getRiferimentoTavolo()}, Numero telefono: {prenotazione.cliente.getRecapitoTelefonico()}"
            item.setText(titolo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(20)
            item.setFont(font)
            listViewModel.appendRow(item)

        self.listView.setModel(listViewModel)

    def getGenericButton(self, titolo, onClick):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(onClick)
        return

    def visualizzaAltro(self):
        selected = self.listView.selectedIndexes()[0].data()
        nomeCliente = selected.split(', ')[0].strip()
        riferimentoTavolo = selected.split(', ')[3].strip().split()[1]
        recapitoTelefonico = selected.split(', ')[4].strip().split()[2]

        print(nomeCliente)
        print(recapitoTelefonico)
        prenotazione = StatoSala.ricercaNomeRecapitoTavolo(self, nomeCliente=nomeCliente, recapitoTelefonico=recapitoTelefonico, riferimentoTavolo=riferimentoTavolo)

        self.vistaPrenotazione = VistaInfoPrenotazione(prenotazione, eliminaCallback=self.aggiornaUi())
        self.vistaPrenotazione.show()

    def eliminaPrenotazione(self):
        print("eliminaPrenotazione")
        selected = self.listView.selectedIndexes()[0].data()
        nomeCliente = selected.split(', ')[0].strip()
        riferimentoTavolo = selected.split(', ')[3].strip().split()[1]
        dataPrenotazione = selected.split(', ')[1].strip()

        recapitoTelefonico = selected.split(', ')[4].strip().split()[2]
        print(recapitoTelefonico)

        print(nomeCliente)
        print(riferimentoTavolo)
        print(dataPrenotazione)
        index = StatoSala.ricercaNomeDataTavolo(self, nomeCliente, dataPrenotazione, riferimentoTavolo)

        print(index)
        del StatoSala.Prenotazioni[index]
        self.aggiornaUi()

    def aggiungiPrenotazione(self):
        self.inserisciPrenotazione = VistaAggiungiPrenotazione(callback=self.aggiornaUi())
        prenotazione = self.inserisciPrenotazione.show()




