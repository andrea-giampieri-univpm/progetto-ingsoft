import unittest

import unittest
import datetime


from RistoMatic.GestioneAmministrativa.Statistiche import Statistiche


class TestStatistiche(unittest.TestCase):


    def testStatisticaNone(self):

        statistica = Statistiche(None,None)

        statistica.setFiltro()
        self.assertIsNotNone(statistica)

        dataFine = datetime.date.today()
        dataInizio = datetime.datetime.today() - datetime.timedelta(days=1)

        self.assertEqual(statistica.getDataInizio(),dataInizio)
        self.assertEqual(statistica.getDataFine(),dataFine)


