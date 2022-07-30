from PySide6 import QtWidgets
from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu

class BlockMenuItem(QtWidgets.QListWidgetItem):

    def __init__(self, elementomenu:ElementoMenu):
        super().__init__()
        self.elementomenu = elementomenu

        self.setText(f"{self.elementomenu.getNomeElemento()} - {self.elementomenu.getPrezzoElemento()}")

    def getData(self):
        return self.elementomenu
