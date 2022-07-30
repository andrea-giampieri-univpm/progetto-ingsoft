import os
import sys
import unittest

from PySide6 import QtWidgets
from Viste.MainVistaMobile import VistaMobile
from Viste.MainVistaPreparazione import VistaPreparazione
from Viste.MainVistaSala import VistaSala
from Tests.TestComanda import *
from Tests.TestPrenotazione import *
from Tests.TestStatistiche import *
from Tests.TestMenu import *


# Settare testmode=True per poter avviare correttamente i test (VEDERE DIRECTORY TEST)
testmode=False
# main
if __name__ == "__main__":
    if (testmode):
        unittest.main()
    else:
        app = QtWidgets.QApplication([])
        app.setStyle('Fusion')

        widgetPreparazione = VistaPreparazione()
        widgetPreparazione.resize(1280, 720)
        widgetPreparazione.show()

        widgetSala = VistaSala()
        widgetSala.resize(1280, 720)
        widgetSala.show()

       # widgetUnlockAmministratore = VistaUnlockAmministratore()
       # widgetUnlockAmministratore.show()

        widgetMobile = VistaMobile()
        widgetMobile.resize(540, 640)
        widgetMobile.show()


        sys.exit(app.exec())
