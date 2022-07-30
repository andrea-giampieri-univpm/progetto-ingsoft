from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione


class VistaInfoPrenotazione(QWidget):
    def __init__(self, prenotazione, eliminaCallback):
        super(VistaInfoPrenotazione, self).__init__()
        self.eliminaCallback = eliminaCallback

        vLayout = QVBoxLayout()
        titolo = ""
        info = {}
        if isinstance(prenotazione, Prenotazione):
            titolo = "Info prenotazione:"
            info = prenotazione.getInfoPrenotazione()

        labelTitolo = QLabel(titolo)
        fontTitolo = labelTitolo.font()
        fontTitolo.setPointSize(16)
        labelTitolo.setFont(fontTitolo)
        vLayout.addWidget(labelTitolo)

       # vLayout.addItem(QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding))

        vLayout.addWidget(QLabel(f"Nome: {info.get('nomeCliente')}"))
        vLayout.addWidget(QLabel(f"Recapito telefonico: {info.get('recapitoTelefonico')}"))
        vLayout.addWidget(QLabel(f"Numero persone: {info.get('numeroPersone')}"))
        vLayout.addWidget(QLabel(f"Numero tavolo: {info.get('riferimentoTavolo')}"))
        vLayout.addWidget(QLabel(f"Data e ora: {info.get('dataPrenotazione')}"))
        vLayout.addWidget(QLabel(f"Stato: {info.get('statoPrenotazione')}"))
        vLayout.addWidget(QLabel(f"Id: {info.get('idPrenotazione')}"))

        self.setLayout(vLayout)
        self.setWindowTitle("Prenotazione")