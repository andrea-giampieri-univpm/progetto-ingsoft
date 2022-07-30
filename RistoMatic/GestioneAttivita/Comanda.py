from RistoMatic.GestioneAttivita import ElementoComanda
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.GestioneAttivita.Enum import StatoComanda
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
import datetime

class Comanda:

    counter_n_comanda=1

    def __init__(self, rif):
        self.dataCreazione = datetime.datetime.now()
        self.elementiComanda= []
        self.rif=rif
        self.comandaSincronizzata=False
        self.numeroComanda = Comanda.counter_n_comanda

        Comanda.counter_n_comanda += 1

        StatoSala.aggiungiComanda(self)

    def aggiungiElementoComanda(self, elementoDaAggiungere : ElementoComanda):
        self.elementiComanda.append(elementoDaAggiungere)

    def getComandaSincronizzata(self):
        return self.comandaSincronizzata

    def getInfoComanda(self) -> dict:
        rif=""
        if isinstance(self.rif, Tavolo):
            rif = "Tavolo "+ str(self.rif.getRiferimentoTavolo())
        elif isinstance(self.rif, OrdineAsporto):
            rif = "Asporto " + str(self.rif.getNumeroOrdine())
        return {
            "rif": rif,
            "dataCreazione": self.dataCreazione,
            "numeroComanda": self.numeroComanda,
            "sincronizzata": self.comandaSincronizzata
        }

    def getNumeroComanda(self) -> int:
        return self.numeroComanda

    def getStato(self):
        count=0
        for elemento in self.elementiComanda:
            if elemento.getIsPronta():
                count=count+1

        if count==len(self.elementiComanda):
            return StatoComanda.COMPLETATA
        elif count > 0:
            return StatoComanda.IN_PREPARAZIONE
        else:
            return StatoComanda.CREATA

    def inviaNotificaBar(self):
        pass

    def rimuoviElementoComanda(self, daEliminare : ElementoComanda):
        self.elementiComanda.remove(daEliminare)

    def setComandaSincronizzata(self, comandaSincronizzata : bool):
        self.comandaSincronizzata=comandaSincronizzata

    #forzo lo stato della comanda e quindi dei suoi elementi su uno stato
    def setStatoPreparazione(self, stato : StatoComanda):
        for elemento in self.elementiComanda:
            if stato==StatoComanda.COMPLETATA:
                elemento.setIsPronta(True)
            elif stato==StatoComanda.CREATA:
                elemento.setIsPronta(False)
            elif stato==StatoComanda.ANNULLATA:
                elemento.setIsPronta(False)
                elemento.setVisibilita(False)

    def stampaPreconto(self):
        pass

    def getCostoCoperto(self):
        if isinstance(self.rif, Tavolo):
            tot=self.rif.getNumeroCoperti()*StatoSala.getMenuAttivo().getCostoCoperto()
            return tot
        return 0

    def getTotale(self):
        tot=0
        for elemento in self.elementiComanda:
            info = elemento.getInfoElementoComanda()
            tot = tot+ (info['Quantita']*info["Prezzo"])

        tot = tot+ self.getCostoCoperto()
        return tot


    # Aggiunti due nuovi metodi ausiliari , integrare con il progetto

    def isAsporto(self):
        if isinstance(self.rif,OrdineAsporto):
            return True
        else:
            return False

    def isTavolo(self):
        if isinstance(self.rif,Tavolo):
            return True
        else:
            return False
