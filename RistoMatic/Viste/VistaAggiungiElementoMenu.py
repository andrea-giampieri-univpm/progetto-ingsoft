from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAttivita.Enum import Zone

class VistaAggiungiElementoMenu(QtWidgets.QWidget):

    def __init__(self,menu,callback):

        super().__init__()

        self.menu=menu
        self.cb=callback

        self.vLayout =QVBoxLayout()
        self.qlines = {}

        self.addInfoText("nomeElemento", "Nome pietanza/bevanda")
        #self.addInfoText("areaPreparazione", "Area di preparazione")
        self.addInfoText("prezzoElemento", "Prezzo pietanza/bevanda")

        self.box = QComboBox()
        self.box.addItem("Cucina")
        self.box.addItem("Bar")
        self.box.addItem("F")
        self.vLayout.addWidget(self.box)

        self.salvaElemento = QPushButton('Aggiungi Elemento al Menù')
        self.salvaElemento.clicked.connect(self.saveElemento)
        self.vLayout.addWidget(self.salvaElemento)

        self.setLayout(self.vLayout)



    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)


    def saveElemento(self):
        text = self.box.currentText()
        zona=Zone.CUCINA
        if(text=="Cucina"):
            zona=Zone.CUCINA
        elif(text=="Bar"):
            zona = Zone.BAR
        elif (text=="Forno"):
            zona = Zone.FORNO

        elemento = ElementoMenu(self.qlines["nomeElemento"].text(),zona,float(self.qlines['prezzoElemento'].text()))
        self.menu.aggiungiElementoMenu(elemento)
        self.cb()
        self.close()
