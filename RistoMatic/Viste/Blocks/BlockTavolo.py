from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QTimer
from RistoMatic.Viste.VistaDettaglioTavolo import BlockDettaglioTavolo
from RistoMatic.GestioneAttivita.Enum import StatoTavolo


class BlockTavolo(QtWidgets.QPushButton):

    def __init__(self,tavolo):
        super().__init__()

        self.tavolo = tavolo

        self.detail=None
        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiorna)
        self.timer.start(5000)

        self.status = tavolo.getStato()
        self.filldata()

        self.clicked.connect(self.show_detail)

    def show_detail(self):
        self.detail=BlockDettaglioTavolo(self.tavolo)
        self.detail.show()


    @Slot()
    def aggiorna(self):
        self.filldata()

    def filldata(self):
        self.status = self.tavolo.getStato()
        self.setText(
            f"Tavolo {str(self.tavolo.riferimentoTavolo)} Posti: {str(self.tavolo.getNumeroPosti())} \n Coperti: {str(self.tavolo.getNumeroCoperti())} \n Stato: {str(self.status.value)}")

        if (self.status == StatoTavolo.UTILIZZABILE):
            self.setStyleSheet('QPushButton {background-color: green; font-size: 16px; height: 90; width:150;}')
        elif (self.status == StatoTavolo.PRENOTATO):
            self.setStyleSheet('QPushButton {background-color: orange; font-size: 16px; height: 90; width:150;}')
        elif (self.status == StatoTavolo.OCCUPATO):
            self.setStyleSheet('QPushButton {background-color: red; font-size: 16px; height: 90; width:150;}')