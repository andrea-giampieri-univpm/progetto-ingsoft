from ElementoMenu import ElementoMenu


class Pietanza(ElementoMenu):
    def __init__(self, listaAllergeni, listaIngredienti, prezzoPietanza, nome):
        super().__init__(areaPreparazione="cucina", prezzoElemento=prezzoPietanza, nomeElemento=nome)
        self.allergeni = [] + listaAllergeni
        self.ingredienti = [] + listaIngredienti

    def getInfoPietanza(self):
        info = self.getInfoElementoMenu()
        info['allergeni'] = self.allergeni
        info['ingredienti'] = self.ingredienti
        return info

    def aggiungiAllergene(self, allergene):
        self.allergeni.append(allergene)

    def aggiungiIngrediente(self, ingrediente):
        self.ingredienti.append(ingrediente)

    def eliminaAllergene(self, allergene):
        self.allergeni.remove(allergene)

    def eliminaIngrediente(self, ingrediente):
        self.ingredienti.remove(ingrediente)

    def getAllergeni(self):
        return self.allergeni

    def getIngredienti(self):
        return self.ingredienti
