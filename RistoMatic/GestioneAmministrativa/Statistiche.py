import datetime
from abc import abstractmethod

class Statistiche():


    def __init__(self,inizioCampionamento,fineCampionamento):
        self.dataInizio = inizioCampionamento
        self.dataFine = fineCampionamento


    def getDataFine(self):
        return self.dataFine

    def getDataInizio(self):
        return self.dataInizio

    def setDataInizio(self , setInizio):
        self.dataInizio = setInizio

    def setDataFine(self , setFine) :
        self.dataFine = setFine

    @abstractmethod
    def calcolaStatistiche(self):
        return


    @abstractmethod
    def generaStatistiche(self)->dict:
        return





    def esportaStatistiche(self):

#   Controllo se prima ci sono gia statistiche a quella data, senno inutile sovrascrivere:
        fileCheck = open('Dati/Statistiche.txt', 'r')
        righe = fileCheck.readlines()
        for riga in righe:
#            if(riga.find(str(self.generaStatistiche(True))) != -1) : return
            if(riga.find(str(self.generaStatistiche)) != -1) : return
        fileCheck.close()

        file_object = open("Dati/Statistiche.txt", 'a')
        file_object.write('GIORNO GENERAZIONE STATISTICA : ')
        file_object.write(datetime.date.today().strftime('%d %b %Y '))
        file_object.write(str(self.generaStatistiche))
        file_object.write('\n')
        file_object.write('\n')
        file_object.close()




    def setFiltro(self):
         if ( self.dataInizio is None) or (self.dataFine is None) :
              self.dataFine = datetime.date.today()
              self.dataInizio = datetime.datetime.today() - datetime.timedelta(days=1)















