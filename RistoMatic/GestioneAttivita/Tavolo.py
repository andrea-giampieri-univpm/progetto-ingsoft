from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Enum import StatoTavolo
import datetime

class Tavolo():
    counter_n_tavolo = 1

    def __init__(self, posti, riferimentoTav = 0):
        super(Tavolo, self).__init__()

        self.numeroPosti=posti
        self.numeroCoperti=0
        self.isLibero = True
        self.riferimentoTavolo = riferimentoTav
        if riferimentoTav == 0:
            self.riferimentoTavolo = Tavolo.counter_n_tavolo
            Tavolo.counter_n_tavolo = Tavolo.counter_n_tavolo + 1
        elif riferimentoTav != 0:
            self.riferimentoTavolo = riferimentoTav
        StatoSala.aggiungiTavolo(self)

    def __eq__(self,obj):
            return self.riferimentoTavolo==obj.riferimentoTavolo

    def getInfoTavolo(self) -> dict:
        return {
            "riferimentoTavolo": self.riferimentoTavolo,
            "posti": self.numeroPosti,
            "coperti": self.numeroCoperti,
            "libero": self.isLibero
        }

    def getIsLibero(self) -> bool:
        return (self.isLibero and not self.getIsPrenotato())

    def getIsPrenotato(self) -> bool:
        prenotazioni=StatoSala.getListaPrenotazioni()
        if (not prenotazioni == None):
            now = datetime.datetime.now()
            for prenotazione in prenotazioni:
                tavoloprenotato=prenotazione.getRiferimentoTavolo()
                dataprenotazione= prenotazione.dataPrenotazione
                diff = ( dataprenotazione-now)
                if tavoloprenotato == self.riferimentoTavolo and (diff.total_seconds()/3600 < 4):
                    return True
        return False

    def getNumeroCoperti(self) -> int:
        return self.numeroCoperti

    def getNumeroPosti(self) -> int:
        return self.numeroPosti

    def getRiferimentoTavolo(self) -> int:
        return self.riferimentoTavolo

    def setIsLibero(self, tavoloLibero : bool):
        self.isLibero=tavoloLibero

    def setNumeroCoperti(self, numeroCoperti: int):
        self.numeroCoperti = numeroCoperti

    def setNumeroPosti(self, numeroPosti : int):
        self.numeroPosti=numeroPosti

    def getStato(self):
        if(not self.isLibero):
            return StatoTavolo.OCCUPATO
        elif(self.getIsPrenotato()):
            return StatoTavolo.PRENOTATO
        return StatoTavolo.UTILIZZABILE
