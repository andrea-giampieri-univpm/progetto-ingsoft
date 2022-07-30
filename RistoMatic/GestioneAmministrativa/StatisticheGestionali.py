import datetime
import itertools
import pickle

import pandas
from RistoMatic.GestioneAmministrativa.Statistiche import Statistiche
from RistoMatic.GestioneAttivita.StatoSala import StatoSala


class StatisticheGestionali(Statistiche):

    def __init__(self, dataInizio, dataFine):
        super().__init__(dataInizio, dataFine)

    # Media ORDINI ASPORTO , ORDINI TAVOLI
    # Totale ORDINI ASPORTO , ORDINI TAVOLI

    # Restituisce due dizionari con la seguente sintassi: dict = { data : lista_comande , ... }
    def calcolaStatistiche(self):

        self.setFiltro()


        storicoComande = StatoSala.getDati(self)

        inizio = datetime.date(self.dataInizio.year, self.dataInizio.month, self.dataInizio.day)
        fine = datetime.date(self.dataFine.year, self.dataFine.month, self.dataFine.day)
        date_list = pandas.date_range(start=inizio, end=fine)
        # per ogni giorno controllo controllo l'incasso
        OrdiniAsporto = {}
        OrdiniTavolo = {}
        for data in date_list:
            comandeAsporto = []
            comandeTavolo = []
            for comanda in storicoComande:
                # print('INFO COMANDA : ' , comanda.getInfoOrdineAsporto())
                dataComanda = datetime.date(comanda.dataCreazione.year, comanda.dataCreazione.month,
                                            comanda.dataCreazione.day)
                if dataComanda == datetime.date(data.year, data.month, data.day):
                    if comanda.isAsporto() is True:
                        comandeAsporto.append(comanda)
                    elif comanda.isTavolo() is True:
                        comandeTavolo.append(comanda)
            OrdiniAsporto[datetime.date(data.year, data.month, data.day)] = comandeAsporto
            OrdiniTavolo[datetime.date(data.year, data.month, data.day)] = comandeTavolo

        return (OrdiniAsporto, OrdiniTavolo)

    #   Posso avere statistiche come segue: giorno con piu ordini , giorno con meno ordini , media ordini nel periodo di tempo
    #   Quante bevande / pietanze si sono presi in quei giorni'
    #   OrdiniAsporto = {'giornoMaxComande':'n_comande' , 'giornoMinComande':'n_comande' , 'MedieComandePeriodoTempo':'n_medioCom', 'Giorno con il maggior numero di elementi':'num_elementi' , 'Giorno con il minor numero di elementi':'num_elementi' , 'mediae elementi':'numMediaElementi'}
    #   OrdiniComande = ////
    # OSSERVAZIONE: le statistiche sul numero di elementi delle comande , non tengono conto della quantità, poichè servono solo per far
    #               vedere quante tipologie di pietanze sono state ordinate , senza vederne la quantità specifica
    def generaStatistiche(self):
        OrdiniAsporto, OrdiniTavolo = self.calcolaStatistiche()

        numComandeAsporto = {}
        #    asportoKey = OrdiniAsporto.keys()
        asportoKey = list(OrdiniAsporto.keys())
        index = 0;
        for value in OrdiniAsporto.values():
            numComandeAsporto[asportoKey[index]] = len(value)
            index = index + 1

        numComandeTavolo = {}
        tavoloKey = list(OrdiniTavolo.keys())
        index = 0;
        for value in OrdiniTavolo.values():
            numComandeTavolo[tavoloKey[index]] = len(value)
            index = index + 1

        giornoMaxComandeAsporto = max(numComandeAsporto, key=numComandeAsporto.get)
        giornoMinComandeAsporto = min(numComandeAsporto, key=numComandeAsporto.get)

        giornoMaxComandeTavolo = max(numComandeTavolo, key=numComandeTavolo.get)
        giornoMinComandeTavolo = min(numComandeTavolo, key=numComandeTavolo.get)

        #   OrdineAsporto e OrdineComande hanno la stessa lunghezza(stesso numero di keys), ciò che cambia sono i values al loro interno !

        totAsporto = 0
        elementiOrdineAsporto = {}
        index = 0
        for listaComande in OrdiniAsporto.values():
            totAsporto = totAsporto + len(listaComande)
            numElementi = 0
            for comanda in listaComande:
                for elemento in comanda.elementiComanda:
                    numElementi = numElementi + 1
            #   OrdiniAsporto.keys()[OrdiniAsporto.values().index(listaComande)]
            elementiOrdineAsporto[asportoKey[index]] = numElementi
            index = index + 1

        mediaComandeAsporto = round(totAsporto / len(OrdiniAsporto), 2)

        giornoNumOrdiniAsportoMax = max(elementiOrdineAsporto, key=elementiOrdineAsporto.get)
        giornoNumOrdiniAsportoMin = min(elementiOrdineAsporto, key=elementiOrdineAsporto.get)
        mediaOrdiniComandeAsporto = round(sum(elementiOrdineAsporto.values()) / len(elementiOrdineAsporto), 1)

        AsportoPuliti = {}
        AsportoPuliti['TIPOLOGIA :'] = 'STATISTICHE GESTIONALI ASPORTO'
        AsportoPuliti['MAX : ', giornoMaxComandeAsporto] = elementiOrdineAsporto.get(giornoMaxComandeAsporto)
        AsportoPuliti['MIN : ', giornoMinComandeAsporto] = elementiOrdineAsporto.get(giornoMinComandeAsporto)
        AsportoPuliti['Media comande nel periodo di tempo : '] = mediaComandeAsporto
        AsportoPuliti['MAX NUM ELEMENTI COMANDE : ', giornoNumOrdiniAsportoMax] = elementiOrdineAsporto.get(
            giornoNumOrdiniAsportoMax)
        AsportoPuliti['MIN NUM ELEMENTI COMANDE : ', giornoNumOrdiniAsportoMin] = elementiOrdineAsporto.get(
            giornoNumOrdiniAsportoMin)
        AsportoPuliti['MEDIA NUM ELEMENTI COMANDE : '] = mediaOrdiniComandeAsporto

        ######### TAVOLO ##########

        #   OrdineAsporto e OrdineComande hanno la stessa lunghezza(stesso numero di keys), ciò che cambia sono i values al loro interno !

        totTavolo = 0
        elementiOrdineTavolo = {}
        index = 0
        for listaComande in OrdiniTavolo.values():
            totTavolo = totTavolo + len(listaComande)
            numElementi = 0
            for comanda in listaComande:
                for eftlemento in comanda.elementiComanda:
                    numElementi = numElementi + 1
            #   OrdiniTavolo.keys()[OrdiniTavolo.values().index(listaComande)]
            elementiOrdineTavolo[tavoloKey[index]] = numElementi
            index = index + 1

        mediaComandeTavolo = round(totAsporto / len(OrdiniTavolo), 2)

        giornoNumOrdiniTavoloMax = max(elementiOrdineTavolo, key=elementiOrdineTavolo.get)
        giornoNumOrdiniTavoloMin = min(elementiOrdineTavolo, key=elementiOrdineTavolo.get)
        mediaOrdiniComandeTavolo = round(sum(elementiOrdineTavolo.values()) / len(elementiOrdineTavolo), 1)

        TavoloPuliti = {}
        TavoloPuliti['TIPOLOGIA :'] = 'STATISTICHE GESTIONALI TAVOLI'
        TavoloPuliti['MAX : ', giornoMaxComandeTavolo] = elementiOrdineTavolo.get(giornoMaxComandeTavolo)
        TavoloPuliti['MIN : ', giornoMinComandeTavolo] = elementiOrdineTavolo.get(giornoMinComandeTavolo)
        TavoloPuliti['Media comande nel periodo di tempo : '] = mediaComandeTavolo
        TavoloPuliti['MAX NUM ELEMENTI COMANDE : ', giornoNumOrdiniTavoloMax] = elementiOrdineTavolo.get(
            giornoNumOrdiniTavoloMax)
        TavoloPuliti['MIN NUM ELEMENTI COMANDE : ', giornoNumOrdiniTavoloMin] = elementiOrdineTavolo.get(
            giornoNumOrdiniTavoloMin)
        TavoloPuliti['MEDIA NUM ELEMENTI COMANDE : '] = mediaOrdiniComandeTavolo

        return AsportoPuliti, TavoloPuliti

    def getMediaOrdininiAsporto(self):
        asporto, tavolo = self.generaStatistiche()
        return round(asporto.get('Media comande nel periodo di tempo : '), 2)

    def getMediaOrdiniTavolo(self):
        asporto, tavolo = self.generaStatistiche()
        return round(tavolo.get('Media comande nel periodo di tempo : '), 2)

    def getTotaleOrdiniAsporto(self):
        OrdiniAsporto, OrdiniTavolo = self.calcolaStatistiche()
        numComandeAsporto = {}
        asportoKey = list(OrdiniAsporto.keys())
        index = 0;
        for value in OrdiniAsporto.values():
            numComandeAsporto[asportoKey[index]] = len(value)
            index = index + 1

        return sum(numComandeAsporto.values())

    def getTotaleOrdiniTavolo(self):
        OrdiniAsporto, OrdiniTavolo = self.calcolaStatistiche()
        numComandeTavolo = {}
        tavoloKey = list(OrdiniTavolo.keys())
        index = 0;
        for value in OrdiniTavolo.values():
            numComandeTavolo[tavoloKey[index]] = len(value)
            index = index + 1





