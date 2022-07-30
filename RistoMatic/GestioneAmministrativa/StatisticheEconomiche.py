
# Statistiche su MASSIMO INCASSO , MINIMO INCASSO , TOTALE INCASSO NEL FILTRO CORRENTE
# Se non presente nessun fitro verra utilizzato uno di default

import datetime
import pickle

import pandas

from RistoMatic.GestioneAmministrativa.Statistiche import Statistiche
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class StatisticheEconomiche(Statistiche):




    def __init__(self,dataInizio , dataFine):
        super().__init__(dataInizio,dataFine)


    # Dati "rozzi" , da lavorare
    def calcolaStatistiche(self):

        self.setFiltro()


      #  print('data inizio: ', self.dataInizio)
      #  print('data fine: ',self.dataFine)
        storicoComande = StatoSala.getDati(self)


        inizio = datetime.date(self.dataInizio.year,self.dataInizio.month,self.dataInizio.day)
        fine = datetime.date(self.dataFine.year,self.dataFine.month,self.dataFine.day)
        date_list = pandas.date_range(start=inizio,end=fine)
        # per ogni giorno controllo controllo l'incasso
        incasso = {}
        for data in date_list:
            tot = 0.0
            for comanda in storicoComande:
                dataComanda = datetime.date(comanda.dataCreazione.year,comanda.dataCreazione.month,comanda.dataCreazione.day)
                if dataComanda == datetime.date(data.year,data.month,data.day):
                    tot = tot + comanda.getTotale()

            incasso[data] = tot

        return incasso





#   dict = {"incasso massimo":"val"   ,   "incasso minimo":"val"   ,   "incasso medio":"val"}
    def generaStatistiche(self):

        datiRaffinati = {}
        datiGrezzi = self.calcolaStatistiche()

        giornoMaxIncasso  = max(datiGrezzi, key=datiGrezzi.get)
        giornoMinIncasso = min(datiGrezzi , key=datiGrezzi.get)

        totIncasso = 0.0
        for singoloIncasso in datiGrezzi.values():
            totIncasso += singoloIncasso

        datiRaffinati['TIPOLOGIA: '] = 'STATISTICHE ECONOMICHE'
        datiRaffinati[giornoMaxIncasso] = datiGrezzi.get(giornoMaxIncasso)
        datiRaffinati[giornoMinIncasso] = datiGrezzi.get(giornoMinIncasso)
        datiRaffinati["media incassi: "] = round(totIncasso/len(datiGrezzi),2)

        return datiRaffinati




    def getMassimoIncasso(self):
        return round(self.generaStatistiche().get(list(self.generaStatistiche()[1])),2)

    def getMinimoIncasso(self):
        return round(self.generaStatistiche().get(list(self.generaStatistiche()[2])),2)

    def getMediaIncasso(self):
        return round(self.generaStatistiche().get(list(self.generaStatistiche()[3])),2)


    def getTotaleIncasso(self):
        return round(sum(self.calcolaStatistiche().values()),2)




































