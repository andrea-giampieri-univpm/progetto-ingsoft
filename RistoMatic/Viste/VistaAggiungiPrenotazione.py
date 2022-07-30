import datetime
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, \
    QCalendarWidget, QComboBox

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione

class VistaAggiungiPrenotazione(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiPrenotazione, self).__init__()
        self.callback = callback
        self.vLayout = QVBoxLayout()
        self.qlines = {}
        self.addInfoText("nome", "Nome")
        #self.addInfoText("dataPrenotazione", "Data")
        self.addInfoText("numeroPersone", "Numero Persone")
        self.addInfoText("riferimentoTavolo", "Riferimento Tavolo")
        self.addInfoText("recapitoTelefonico", "Recapito Telefonico")

        self.data = QCalendarWidget()
        self.data.clicked.connect(self.selezionaData)
        self.dataSelezionata = None

        self.menuOra = QComboBox()
        orari = ['11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30']
   #     self.menuOra.clicked.connect(self.selezionaOra)
        self.menuOra.addItems(orari)
   #    self.menuOra.clicked.connect(self)
        self.dataString = QLabel("Giorno prenotazione:")
        self.oraString = QLabel("Orario prenotazione:")
        self.box = QCheckBox("Prenotazione da confermare?", self)
  #      self.box.stateChanged.connect(self.clickBox)
        self.vLayout.addWidget(self.dataString)
        self.vLayout.addWidget(self.data)
        self.vLayout.addWidget(self.oraString)
        self.vLayout.addWidget(self.menuOra)

        self.vLayout.addWidget(self.box)

        self.statoPrenotazione = "Confermata"

        okButton = QPushButton("OK")
        prenotazione = okButton.clicked.connect(self.aggiungiPrenotazione)
        self.qlines["okButton"] = okButton
        self.vLayout.addWidget(okButton)
        self.setLayout(self.vLayout)

    def selezionaData(self):
        self.dataSelezionata = self.data.selectedDate()


        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()

        #self.pyDate = datetime.date(int(self.year), int(self.month), int(self.day))
#        self.pyDate.day(self.dataSelezionata.day())
#        self.pyDate.month(self.dataSelezionata.month())
#        self.pyDate.year(self.dataSelezionata.year())
        #print(self.pyDate)


    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)

    def giaPrenotato(self, riferimentoTavolo):
        tavoli = StatoSala.getListaTavoli()
        prenotato = False
        for i in StatoSala.Prenotazioni:
            if i.riferimentoTavolo == riferimentoTavolo:
                diff = i.dataPrenotazione - self.pyDate
                for i in tavoli:
                    if i.riferimentoTavolo == riferimentoTavolo:
                        prenotato = i.getIsPrenotato
        return prenotato


    def aggiungiPrenotazione(self):

        riferimentoTavolo = int(self.qlines["riferimentoTavolo"].text())

        cliente = Cliente("", "")
        self.prenotazione = Prenotazione('', -1, cliente, -1)

        nome = self.qlines["nome"].text()
        recapitoTelefonico = self.qlines["recapitoTelefonico"].text()

        selected = self.menuOra.currentText()
        ora = int(selected.split(':')[0].strip())
        minuti = int(selected.split(':')[1].strip())
#        print(ora)
#        print(minuti)
        numeroPersone = int(self.qlines["numeroPersone"].text())
        check = self.box.checkState()

        if check == 2:      #se c'è la spunta imposta da confermare
            print('2')
            self.prenotazione.setStatoPrenotazione('Da Confermare')

        self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day), ora, minuti, 0)
        for i in StatoSala.Prenotazioni:
            if self.giaPrenotato(riferimentoTavolo):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Il tavolo scelto ha già una prenotazione per quell'ora")
                msg.exec_()
                return

        self.prenotazione.setDataPrenotazione(self.pyDate)
        self.prenotazione.setRiferimentoTavolo(riferimentoTavolo)
        self.prenotazione.setNumeroPersone(numeroPersone)
        #self.prenotazione.setStatoPrenotazione(statoPrenotazione)
        self.prenotazione.cliente.setNomeCliente(nome)
        self.prenotazione.cliente.setRecapitoTelefonico(recapitoTelefonico)

        StatoSala.Prenotazioni.append(self.prenotazione)
        self.close()
