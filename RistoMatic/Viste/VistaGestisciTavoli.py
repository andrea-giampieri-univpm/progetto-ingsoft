from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QListView, QVBoxLayout
from PySide6 import QtWidgets

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.Viste.VistaAggiungiTavolo import VistaAggiungiTavolo


class VistaGestisciTavoli(QtWidgets.QWidget):
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
    #    testButton = QPushButton("Test button")
    #    testButton.clicked.connect(self.visualizzaAltreInformazioni)

        newButton = QPushButton("Crea nuovo tavolo")
        newButton.clicked.connect(self.nuovoTavolo)

        delButton = QPushButton("Elimina tavolo selezionato")
        delButton.clicked.connect(self.eliminaTavolo)

        buttonsLayout.addWidget(newButton)
    #    buttonsLayout.addWidget(testButton)
        buttonsLayout.addWidget(delButton)

        buttonsLayout.addStretch()
        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(1000, 600)
        self.setWindowTitle("Gestione tavoli")

    def nuovoTavolo(self):
        print('nuovoTavolo')
        self.inserisciTavolo = VistaAggiungiTavolo(callback=self.aggiornaUi())
        tavolo = self.inserisciTavolo.show()



    def eliminaTavolo(self):
        print('eliminaTavolo')
        selected = self.listView.selectedIndexes()[0].data()
        riferimentoTavolo = int(selected.split(', ')[0].strip().split()[2])
        print('num tav',riferimentoTavolo)
   #    numeroPosti = int(selected.split(', ')[1].strip().split()[3])
        tavolo = StatoSala.ricercaTavolo(riferimentoTavolo)
        StatoSala.rimuoviTavolo(tavolo)
        self.aggiornaUi()

    def visualizzaAltreInformazioni(self):
        print('VisualizzaAltreInformazioni')
        self.aggiornaUi()
        for tavolo in StatoSala.Tavoli:
            print(tavolo.getInfoTavolo())


    def aggiornaUi(self):
        listViewModel = QStandardItemModel(self.listView)
        StatoSala.Tavoli.sort(key=lambda x: x.getRiferimentoTavolo())
        for tavolo in StatoSala.Tavoli:  # mostra le infromazioni del tavolo per ogni tavolo nella lista Tavoli di stato sala
            qItem = QStandardItem()
            titolo = f"Numero tavolo: {tavolo.riferimentoTavolo}, Numero posti massimo: {tavolo.numeroPosti}"
            qItem.setText(titolo)
            qItem.setEditable(False)
            font = qItem.font()
            font.setPointSize(20)
            qItem.setFont(font)
            listViewModel.appendRow(qItem)
        self.listView.setModel(listViewModel)

    def getGenericButton(self, titolo, onClick):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(onClick)
        return
