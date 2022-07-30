from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel, QGridLayout, QLineEdit, QMessageBox
from RistoMatic.Viste.Blocks.BlockComandaSala import BlockComandaSala
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class BlockDettaglioTavolo(QtWidgets.QWidget):

    def __init__(self,tavolo):
        super().__init__()
        self.setWindowTitle(f"Tavolo {tavolo.riferimentoTavolo}")

        self.tavolo=tavolo

        self.add=QPushButton("Apri tavolo")
        self.add.clicked.connect(self.aggiungi_comanda)

        self.remove = QPushButton("Chiudi tavolo")
        self.remove.clicked.connect(self.rimuovi_comanda)

        self.coperti = QLineEdit()
        self.coperti.setFixedSize(25, 25)
        self.coperti.setText(str(0))
        self.coperti.textChanged.connect(self.modifica_coperti)
        self.coperti.setAlignment(Qt.AlignLeft)

        self.lbl_coperti = QLabel("Coperti ")
        self.lbl_coperti.setAlignment(Qt.AlignRight)

        self.lbl_prenotazione = QLabel("Prenotazione: ")
        self.lbl_prenotazione.setAlignment(Qt.AlignRight)

        self.prenotazione = QLabel("nessuna")
        prenotazioni = StatoSala.getListaPrenotazioni()
        if not prenotazioni == None:
            for prenotazione in prenotazioni:
                if prenotazione.riferimentoTavolo == self.tavolo.getRiferimentoTavolo():
                    self.prenotazione.setText(str(prenotazione.cliente.nomeCliente))

        self.prenotazione.setAlignment(Qt.AlignLeft)

        self.comanda=StatoSala.ricercaComanda(self.tavolo.riferimentoTavolo)

        self.wcomanda=None

        self.resize(540, 640)
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.add,0,0,1,2)
        self.grid.addWidget(self.remove,0,2,1,2)
        self.grid.addWidget(self.lbl_coperti, 1, 0, 1, 1)
        self.grid.addWidget(self.coperti, 1, 1, 1, 1)
        self.grid.addWidget(self.lbl_prenotazione, 1, 2, 1, 1)
        self.grid.addWidget(self.prenotazione, 1, 3, 1, 1)

        if (not self.comanda == None):
            self.wcomanda = BlockComandaSala(self.comanda)
            self.grid.addWidget(self.wcomanda, 2, 0, 1, 4)

    def aggiungi_comanda(self):
        if self.comanda == None:
            self.comanda = Comanda(self.tavolo)
            self.wcomanda = BlockComandaSala(self.comanda)
            self.grid.addWidget(self.wcomanda, 2, 0, 1, 4)

    def rimuovi_comanda(self):
        if not self.comanda==None and StatoSala.rimuoviComanda(self.comanda):
            self.comanda = None
            self.wcomanda.deleteLater()
        else:
            msgBox = QMessageBox()
            msgBox.setText("Impossibile chiudere tavolo")
            msgBox.exec()

    def modifica_coperti(self):

            if not self.coperti.text() =="":
              if self.coperti.text().isnumeric() is False  :
                  msgBox = QMessageBox()
                  msgBox.setText("Coperto non valido. Puoi inserire solo NUMERI !")
                  msgBox.exec()
                  self.tavolo.setNumeroCoperti(1)
                  self.coperti.setText("1")
                  return
              if int(self.coperti.text()) > int(self.tavolo.getNumeroPosti()) :
                  msgBox = QMessageBox()
                  msgBox.setText("Capienza massima tavolo raggiunta !")
                  msgBox.exec()
                  self.tavolo.setNumeroCoperti(1)
                  self.coperti.setText("1")
                  return
              self.tavolo.setNumeroCoperti(int(self.coperti.text()))
            if not self.wcomanda ==None:
                    self.wcomanda.aggiorna_totale()
                    return


