import unittest
import datetime
from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione

class TestPrenotazione(unittest.TestCase):

    def testCreazionePrenotazione(self):
        data = datetime.datetime(2022, 6, 14, 19, 30, 0)
        data.now()
        cliente = Cliente("Angelo Rossi", "3334445556")
        prenotazione = Prenotazione(dataPrenotazione=data, numeroPersone=4, cliente=cliente, riferimentoTavolo=2)

        prenotazioni = [prenotazione]


        self.assertEqual(cliente.nomeCliente, prenotazioni[0].cliente.nomeCliente)
        self.assertEqual(cliente.recapitoTelefonico, prenotazioni[0].cliente.recapitoTelefonico)
        self.assertEqual(prenotazione.id, prenotazioni[0].id)
        self.assertEqual(prenotazione.dataPrenotazione, prenotazioni[0].dataPrenotazione)
        self.assertEqual(prenotazione.statoPrenotazione, prenotazioni[0].statoPrenotazione)
        self.assertEqual(prenotazione.numeroPersone, prenotazioni[0].numeroPersone)
        self.assertEqual(prenotazione.riferimentoTavolo, prenotazioni[0].riferimentoTavolo)