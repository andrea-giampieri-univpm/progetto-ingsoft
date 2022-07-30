from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu

class ElementoComanda():
    def __init__(self, elementoMenu : ElementoMenu, note: str, quantita: int):
        self.elemento = elementoMenu
        self.note = note
        self.quantita=quantita
        self.isPronta = False
        self.visibilita = True #se false l'elemento è annullato

    def getInfoElementoComanda(self):
        return {"Nome":self.elemento.nomeElemento,
                "Note":self.note,
                "Quantita":self.quantita,
                "Prezzo": self.elemento.prezzoElemento}

    def getIsPronta(self):
        return self.isPronta

    def getNote(self):
        return self.note

    def getQuantita(self):
        return self.quantita

    def getVisibilita(self):
        return self.visibilita

    def setIsPronta(self,isPronta : bool):
        self.isPronta=isPronta

    def setNote(self,note : str) :
        self.note=note

    def setQuantita(self,quantita : int):
        self.quantita=quantita

    def setVisibilita(self,visibilita) :
        self.visibilita=visibilita