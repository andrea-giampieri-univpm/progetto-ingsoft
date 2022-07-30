import unittest
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class TestComanda(unittest.TestCase):

    def test_creazione_tavolo(self):
        tavolo= Tavolo(1)
        comanda=Comanda(tavolo)
        assert(comanda.getNumeroComanda()==1 and isinstance(comanda.rif,Tavolo))

    def test_rimozione_comanda(self):
        tavolo = Tavolo(1)
        comanda = Comanda(tavolo)
        StatoSala.aggiungiComanda(comanda)
        assert(StatoSala.rimuoviComanda(comanda))