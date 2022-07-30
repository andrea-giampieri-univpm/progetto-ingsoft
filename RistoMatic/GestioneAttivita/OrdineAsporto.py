import datetime

import RistoMatic.GestioneAttivita.Comanda

class OrdineAsporto():
    id = 1000

    def __init__(self, oraConsegna, oraOrdine, cliente):
        self.numeroOrdine = self.id
        OrdineAsporto.id += 1
        self.oraConsegna = oraConsegna
        self.oraOrdine = datetime.datetime.now()
        self.cliente = cliente

        self.comanda = RistoMatic.GestioneAttivita.Comanda.Comanda(self)

    def getInfoOrdineAsporto(self):
        return {
            "numeroOrdine": self.numeroOrdine,
            "oraOrdine": self.oraOrdine,
            "oraConsegna": self.oraConsegna,

            "nomeCliente": self.cliente.getNomeCliente(),
            "recapitoTelefonico": self.cliente.getRecapitoTelefonico(),
            "idCliente": self.cliente.getIdCliente()
        }

    def getTotale(self):
        tot = 0
        for elemento in self.comanda.elementiComanda:
            info = elemento.getInfoElementoComanda()
            tot = tot + (info['Quantita'] * info["Prezzo"])
        return tot

    def getNumeroOrdine(self):
        return self.numeroOrdine

    def getOraConsegna(self):
        return self.oraConsegna

    def getoraOrdine(self):
        return self.oraOrdine

    def setOraConsegna(self, oraConsegna):
        self.oraConsegna = oraConsegna

    def setoraOrdine(self, oraOrdine):
        self.oraOrdine = oraOrdine

    def aggiungiElementoAporto(self, elementoComanda):
        self.comanda.elementiComanda.append(elementoComanda)

    def rimuoviElementoAporto(self, index):
        self.comanda.elementiComanda.remove(index)


    def getComanda(self):
        return self.comanda


