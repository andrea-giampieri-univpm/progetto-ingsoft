import datetime
import os
import pickle

import RistoMatic.GestioneAttivita.Tavolo
import RistoMatic.GestioneAttivita.OrdineAsporto
from RistoMatic.GestioneAttivita import OrdineAsporto
from RistoMatic.GestioneAttivita.Enum import StatoComanda, StatoPrenotazione


class StatoSala():
    OrdiniAsporto =[]
    Tavoli = []
    Prenotazioni = []
    Comande = []
    Menu = None

    def __init__(self):
        pass

    @staticmethod
    def start():
        if os.path.isfile('Dati/Tavoli.pickle'):
            with open('Dati/Tavoli.pickle', 'rb') as f:
                dati = pickle.load(f)
            StatoSala.Tavoli=dati

        dict=StatoSala.getDictMenu()
        StatoSala.setMenuAttivo("Default")

    @staticmethod
    def getListaTavoli():
        return StatoSala.Tavoli

    @staticmethod
    def aggiungiTavolo(tavolo):
        StatoSala.Tavoli.append(tavolo)

        dati = []
        if os.path.isfile('Dati/Tavoli.pickle'):
            with open('Dati/Comande.pickle', 'rb') as f:
                dati = pickle.load(f)
        dati.append(tavolo)
        with open('Dati/Tavoli.pickle', 'wb') as handle:
            pickle.dump(dati, handle, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def ricercaTavolo(tavolo_ricerca):
        rif=0
        if isinstance(tavolo_ricerca, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
            rif= tavolo_ricerca.riferimentoTavolo
        elif isinstance(tavolo_ricerca, int):
            rif = tavolo_ricerca

        for tavolo in StatoSala.getListaTavoli():
            if tavolo.riferimentoTavolo == rif:
                return tavolo
        return None

    @staticmethod
    def rimuoviTavolo(tavolo):
        if (tavolo.getIsLibero()):
            try:
                StatoSala.Tavoli.remove(tavolo)
                dati = []
                if os.path.isfile('Dati/Tavoli.pickle'):
                    with open('Dati/Tavoli.pickle', 'rb') as f:
                        dati = pickle.load(f)
                dati.remove(tavolo)
                with open('Dati/Tavoli.pickle', 'wb') as handle:
                    pickle.dump(dati, handle, pickle.HIGHEST_PROTOCOL)
            except:
                print("errore eliminazione")


    @staticmethod
    def salvaDati():
        pass

    @staticmethod
    def getListaComande():
        return StatoSala.Comande

    @staticmethod
    def aggiungiComanda(comanda):
        StatoSala.Comande.append(comanda)
        if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
            comanda.rif.setIsLibero(False)

    @staticmethod
    def ricercaComanda(riferimento: int):
        for comanda in StatoSala.getListaComande():
            if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo) and comanda.rif.riferimentoTavolo == riferimento:
                return comanda
            elif isinstance(comanda.rif, RistoMatic.GestioneAttivita.OrdineAsporto.OrdineAsporto) and comanda.rif.numeroOrdine == riferimento:
                return comanda
        return None

    @staticmethod
    def rimuoviComanda(comanda):
        try:
            if (not comanda.getStato()==StatoComanda.IN_PREPARAZIONE):
                dati = []
                if os.path.isfile('Dati/Comande.pickle'):
                    with open('Dati/Comande.pickle', 'rb') as f:
                        dati = pickle.load(f)
                dati.append(comanda)
                with open('Dati/Comande.pickle', 'wb') as handle:
                    pickle.dump(dati, handle, pickle.HIGHEST_PROTOCOL)

                StatoSala.Comande.remove(comanda)
                if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
                    comanda.rif.setIsLibero(True)
                    comanda.rif.setNumeroCoperti(0)
                return True
            else:
                return False

        except:
            return False


    @staticmethod
    def getDictMenu():
        if os.path.isfile('Dati/Menu.pickle'):
            with open('Dati/Menu.pickle', 'rb') as f:
                menus = pickle.load(f)
                return menus

    @staticmethod
    def aggiungiMenu(menu):
        menus = dict()
        if os.path.isfile('Dati/Menu.pickle'):
            with open('Dati/Menu.pickle', 'rb') as f:
                menus = pickle.load(f)
        menus[menu.getNomeMenu()]=(menu)
        with open('Dati/Menu.pickle', 'wb') as handle:
            pickle.dump(menus, handle, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def getMenuAttivo():
        if StatoSala.Menu == None or StatoSala.Menu==False:
            dictMenu=StatoSala.getDictMenu()
            StatoSala.setMenuAttivo(dictMenu["Default"])
        return StatoSala.Menu

    @staticmethod
    def setMenuAttivo(key):
        menu = StatoSala.cercaMenu(key)
        StatoSala.Menu=menu

    @staticmethod
    def rimuoviMenu(key):
        if not key=="Default" and os.path.isfile('Dati/Menu.pickle'):
            with open('Dati/Menu.pickle', 'rb') as f:
                menus = pickle.load(f)
                menus.pop(key)
                with open('Dati/Menu.pickle', 'wb') as handle:
                    pickle.dump(menus, handle, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def cercaMenu(key):
        if os.path.isfile('Dati/Menu.pickle'):
            with open('Dati/Menu.pickle', 'rb') as f:
                menus = pickle.load(f)
                try:
                    return menus[key]
                except:
                    return False


    @staticmethod
    def getListaPrenotazioni():
        return StatoSala.Prenotazioni

    @staticmethod
    def getListaCodaPrenotazione():
        prenotazioni = []
        for prenotazione in StatoSala.getListaPrenotazioni():
            if prenotazione.getStatoPrenotazione() == StatoPrenotazione.NON_CONFERMATA:
                prenotazioni.append(prenotazione)

        return prenotazioni

    @staticmethod
    def ricercaPrenotazione(nomeCliente: str, dataPrenotazione: datetime):
        prenotazioni = []
        for prenotazione in StatoSala.getListaPrenotazioni():
            info = prenotazione.getInfoPrenotazione()
            if info["NomeCliente"] == nomeCliente and dataPrenotazione==prenotazione.getDataPrenotazione():
                prenotazioni.append(prenotazione)

        return prenotazioni

    @staticmethod
    def rimuoviPrenotazione(prenotazione):
        dati = []
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                dati = pickle.load(f)
        dati.append(prenotazione)
        with open('Dati/Prenotazioni.pickle', 'wb') as handle:
            pickle.dump(dati, handle, pickle.HIGHEST_PROTOCOL)

        StatoSala.Prenotazioni.remove(prenotazione)


    @staticmethod
    def inviaRisposta():
        pass

    @staticmethod
    def notificaDisponibilita(numeroCellulareCliente : str, nomeCliente : str):
        pass

    @staticmethod
    def rimuoviPrenotazioniNonConfermate():
        nc= StatoSala.getListaCodaPrenotazione()
        for prenotazione in nc:
            StatoSala.rimuoviPrenotazione(prenotazione)


    @staticmethod
    def aggiungiOrdineAsporto(ordineasporto):
        StatoSala.OrdiniAsporto.append(ordineasporto)

    @staticmethod
    def getListaAsporto():
        return StatoSala.OrdiniAsporto

    @staticmethod
    def ricercaOrdineAsporto(nomeCliente : str):
        for asporto in StatoSala.getListaAsporto():
            if asporto.cliente.nomeCliente == nomeCliente:
                return asporto
        return None

    @staticmethod
    def rimuoviOrdineAsporto(ordine):
        dati = []
        if os.path.isfile('Dati/Comande.pickle'):
            with open('Dati/Comande.pickle', 'rb') as f:
                dati = pickle.load(f)
        dati.append(ordine.getComanda())
        with open('Dati/Comande.pickle', 'wb') as handle:
            pickle.dump(dati, handle, pickle.HIGHEST_PROTOCOL)

        StatoSala.rimuoviComanda(ordine.getComanda())
        StatoSala.OrdiniAsporto.remove(ordine)


    @staticmethod
    def ricercaNomeRecapitoTavolo(self, nomeCliente, recapitoTelefonico, riferimentoTavolo):
       for i in StatoSala.Prenotazioni:
            if i.cliente.nomeCliente == nomeCliente and i.riferimentoTavolo == int(riferimentoTavolo):
                prenotazione = i
       return prenotazione


    @staticmethod
    def eliminaTavoloPerRiferimento(riferimentoTavolo):
        index = 0
        for i in StatoSala.Tavoli:
            rif = i.getRiferimentoTavolo()
            if rif == riferimentoTavolo:
                print('RIFERIMENTO UGUALE')
                index = StatoSala.Tavoli.index(i)
        del StatoSala.Tavoli[index]



    @staticmethod
    def ricercaNomeDataTavolo(self, nomeCliente, dataPrenotazione, riferimentoTavolo):
        for i in StatoSala.Prenotazioni:
            if i.cliente.nomeCliente == nomeCliente and i.riferimentoTavolo == int(riferimentoTavolo):
                prenotazione = i
        return StatoSala.Prenotazioni.index(prenotazione)



#   Prende i dati dal file pickle
    @staticmethod
    def getDati(self):
        with (open("Dati/Comande.pickle", "rb")) as openfile:
           while True:
             try:
                storicoComande = pickle.load(openfile)
                return storicoComande
#   Se il file non esiste lo controllo direttamente dal Main
             except EOFError:
                 break


