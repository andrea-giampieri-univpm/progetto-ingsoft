from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout,QListWidget,QListWidgetItem, QHBoxLayout, QLabel,QLineEdit
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.Viste.Blocks.LineSeparator import QHSeperationLine


class BlockElementoComandaAsporto(QtWidgets.QVBoxLayout):

    aggiornaComanda = Signal()
    eliminaElemento = Signal(object,object)

    def __init__(self, elemento: ElementoComanda):
        super().__init__()
        self.elemento = elemento

        info = self.elemento.getInfoElementoComanda()

        self.col1 = QVBoxLayout()
        self.elem = QLabel(info["Nome"])
        self.elem.setStyleSheet("QLabel {font-size: 16px;}")
        self.col1.addWidget(self.elem)
        self.col1.addWidget(QLabel(info["Note"]))

        self.col2 = QVBoxLayout()
        self.col2.addWidget(QLabel(f"Qty"))
        self.qty = QLabel()
        self.qty.setStyleSheet("QLabel {color: red;}")
        self.qty.setText(str(info["Quantita"]))
        self.col2.addWidget(self.qty)

        self.col3 = QVBoxLayout()
        self.btnp =QPushButton("+")
        self.btnp.clicked.connect(self.aumenta)
        self.btnp.setFixedSize(25,25)
        self.col3.addWidget(self.btnp)
        self.btnm = QPushButton("-")
        self.btnm.clicked.connect(self.riduci)
        self.btnm.setFixedSize(25,25)
        self.col3.addWidget(self.btnm)

        self.col4 = QVBoxLayout()
        self.col4.addWidget(QLabel(str(info["Prezzo"]) +" €/unita"))
        self.prezzo= QLabel(str(info["Prezzo"]*info["Quantita"]) + " €")
        self.prezzo.setStyleSheet("QLabel {font-weight: bold}")
        self.col4.addWidget(self.prezzo)
        self.col4.setAlignment(Qt.AlignRight)

        self.col5 = QVBoxLayout()
        self.btnd = QPushButton("X")
        self.btnd.clicked.connect(self.rimuovi)
        self.btnd.setFixedSize(25, 25)
        self.col5.addWidget(self.btnd)

        self.row = QHBoxLayout()
        self.row.setAlignment(Qt.AlignTop)
        self.row.addLayout(self.col1)
        self.row.addLayout(self.col2)
        self.row.addLayout(self.col3)
        self.row.addLayout(self.col4)
        self.row.addLayout(self.col5)

        self.line = QVBoxLayout()
        self.line.setAlignment(Qt.AlignTop)
        self.line.addLayout(self.row)
        self.line.addWidget(QHSeperationLine())

        self.addLayout(self.line)

    def aumenta(self):
        self.elemento.setQuantita(self.elemento.getQuantita() +1)
        self.qty.setText(str(self.elemento.getQuantita()))
        info = self.elemento.getInfoElementoComanda()
        self.prezzo.setText(str(info["Prezzo"]*info["Quantita"]) + " €")
        self.aggiornaComanda.emit()

    def riduci(self):
        val = (self.elemento.getQuantita() -1)
        if val >0:
            self.elemento.setQuantita(val)
            self.qty.setText(str(self.elemento.getQuantita()))
            info = self.elemento.getInfoElementoComanda()
            self.prezzo.setText(str(info["Prezzo"] * info["Quantita"]) + " €")
            self.aggiornaComanda.emit()

    def rimuovi(self):
        self.eliminaElemento.emit(self.elemento,self)
        self.aggiornaComanda.emit()
        for i in reversed(range(self.col1.count())):
            self.col1.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.col2.count())):
            self.col2.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.col3.count())):
            self.col3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.col4.count())):
            self.col4.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.col5.count())):
            self.col5.itemAt(i).widget().setParent(None)
            self.line.itemAt(1).widget().setParent(None)
        self.deleteLater()
