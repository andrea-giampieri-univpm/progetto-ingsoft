import datetime
from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAttivita.Enum import Zone
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class Menu:
    # costo_coperto = 0
    def __init__(self, nome_menu, costo_coperto):
        self.costoCoperto=costo_coperto
        self.dataCreazione = datetime.datetime.now()
        self.nomeMenu=nome_menu
        self.listaElementi = dict()


    def aggiungiElementoMenu(self, elemento):
        if (isinstance(elemento,ElementoMenu)):
            self.listaElementi[elemento.nomeElemento] = elemento
        else:
            raise Exception("Not ElementoMenu")

    def eliminaElementoMenu(self, nome):
        del(self.listaElementi[nome])

    def getCostoCoperto(self):
        return self.costoCoperto

    def getDataCreazione(self):
        return self.dataCreazione

    def getInfoMenu(self):
        return {
            "nomeMenu": self.nomeMenu,
            "costoCoperto": self.costoCoperto,
            "dataCreazione": self.dataCreazione
        }

    def getNomeMenu(self):
        return self.nomeMenu

    def getListaElementi(self):
        return self.listaElementi

    def setCostoCoperto(self, costo):
        self.costoCoperto=costo

    def setDataCreazione(self, data):
        try:
            self.dataCreazione = datetime.datetime.strptime(data, "%d/%m/%Y")
        except:
            raise Exception("Not a date")

    def setNomeMenu(self, nome: str):
        self.nomeMenu = nome
