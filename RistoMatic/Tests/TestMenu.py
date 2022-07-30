import unittest

from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAmministrativa.Menu import Menu


class TestMenu(unittest.TestCase):

#   Verifco che raisa se l'elemento non è un ElementoMenu
    def testAggiungiMenu(self):
        menu = Menu('Menu di Prova',1.50)
        self.assertIsNotNone(menu)
        self.assertRaises(Exception,menu.aggiungiElementoMenu)

    def testEliminaMenu(self):
        menu = Menu('Menu di Prova',1.50)
        elementoMenu = ElementoMenu('elemento di prova','CUCINA',12.75)
        menu.aggiungiElementoMenu(elementoMenu)
        menu.eliminaElementoMenu(elementoMenu.nomeElemento)
        self.assertEqual(len(menu.getListaElementi()),0)


