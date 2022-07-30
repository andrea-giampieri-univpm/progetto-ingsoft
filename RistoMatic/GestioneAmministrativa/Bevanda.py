import ElementoMenu


class Bevanda(ElementoMenu):
    def __init__(self, listaContenitori, temperaturaBevanda, prezzoBevanda, nomeBevanda):
        super().__init__(areaPreparazione="bar", prezzoElemento=prezzoBevanda, nomeElemento=nomeBevanda)
        self.contenitoreBevanda = [] + listaContenitori
        self.temperaturaBevanda = temperaturaBevanda

    def getInfoBevanda(self):
        info = self.getInfoElementoMenu()
        info['contenitoreBevanda'] = self.contenitoreBevanda
        info['temperaturaBevanda'] = self.temperaturaBevanda
        return info

    def aggiungiContenitoreBevanda(self, contenitoreDaAggiungere):
        self.contenitoreBevanda.append(contenitoreDaAggiungere)

    def eliminaContenitoreBevanda(self, contenitoreDaEliminare):
        self.contenitoreBevanda.remove(contenitoreDaEliminare)

    def getContenitoreBevanda(self):
        return self.contenitoreBevanda

    def getTemperaturaBevanda(self):
        return self.temperaturaBevanda

    def setTemperaturaBevanda(self, temp):
        self.temperaturaBevanda = temp
