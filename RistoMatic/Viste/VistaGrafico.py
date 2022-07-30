import matplotlib.pyplot as plt
import numpy as np
from PySide6 import QtWidgets
from numpy import spacing

#from RistoMatic.GestioneAmministrativa import StatisticheEconomiche
import datetime

class VistaGrafico():

#   1 Grafico
    def graficoStatisticheEconomiche(self,datiRaffinati):

        giorni = []

        for sgiorno in datiRaffinati.keys():
           # dataSporca = sgiorno.isoformat()
            dataPulita = datetime.date(sgiorno.year,sgiorno.month,sgiorno.day).strftime('%m-%d')
            giorni.append(dataPulita)


#       len(datiRaffinati.giorni)

        x_pos = np.arange(len(giorni))
        plt.bar(x_pos, datiRaffinati.values(), align='center')
        plt.xticks(x_pos, giorni)
        plt.ylabel('Incasso (€)')
        plt.xlabel('Giorno')
        plt.title('Guadagno totale per giorno')
        plt.xticks(rotation=45)
        plt.show()




#   4 Grafici
    def graficoStatisticheGestionali(self,ordiniAsporto,ordiniTavolo):


#        print('ordiniTavoli.values() = ', ordiniTavolo.values())

#   Plotto il diagramma a blocchi: N°COMANDE TAVOLI AL GIORNO:
        giorni = []
        for sgiorno in ordiniTavolo.keys():  # I giorni vanno bene per tutti e quattro i grafici
            dataPulita = datetime.date(sgiorno.year,sgiorno.month,sgiorno.day).strftime('%m-%d')
            giorni.append(dataPulita)

        numComandeTavolo = []
        for value in ordiniTavolo.values():
            numComandeTavolo.append(len(value))
        numComandeAsporto = []
        for value in ordiniAsporto.values():
            numComandeAsporto.append(len(value))


        elementiOrdineAsporto = {}
        index = 0
        asportoKey = list(ordiniAsporto.keys())
        for listaComande in ordiniAsporto.values():
            numElementi = 0
            for comanda in listaComande:
                  for elemento in comanda.elementiComanda:
                      numElementi = numElementi + 1
        #   OrdiniAsporto.keys()[OrdiniAsporto.values().index(listaComande)]
            elementiOrdineAsporto[asportoKey[index]] = numElementi
            index = index+1


        totTavolo = 0
        elementiOrdineTavolo = {}
        index = 0
        tavoloKey = list(ordiniTavolo.keys())
        for listaComande in ordiniTavolo.values():
            totTavolo = totTavolo + len(listaComande)
            numElementi = 0
            for comanda in listaComande:
                  for elemento in comanda.elementiComanda:
                      numElementi = numElementi + 1
            elementiOrdineTavolo[tavoloKey[index]] = numElementi
            index = index+1


#        print('numComandeTavolo : ', numComandeTavolo)
#        print('elementiOrdineTavolo.values() : ', elementiOrdineTavolo.values())


# Numero di comande al TAVOLO al GIORNO
        plt.subplot(2,2,1)
        x_pos = np.arange(len(giorni))
        plt.bar(x_pos, numComandeTavolo, align='center')
        plt.xticks(x_pos, giorni)
        plt.ylabel('n° com. tavoli')
        plt.xlabel('Giorno')
        plt.title('n°com. tavoli X giorno')
        plt.xticks(rotation=90)

# Numero di comande d'ASPORTO al giorno
        plt.subplot(2,2,2)
        x_pos = np.arange(len(giorni))
        plt.bar(x_pos, numComandeAsporto, align='center')
        plt.xticks(x_pos, giorni)
        plt.ylabel('n° com. asporto')
        plt.xlabel('Giorno')
        plt.title('n°com. asporto X giorno')
        plt.xticks(rotation=90)


#  Numero di ELEMENTI comande TAVOLO al GIORNO
        plt.subplot(2,2,3)
        x_pos = np.arange(len(giorni))
        plt.bar(x_pos, elementiOrdineTavolo.values(), align='center')
        plt.xticks(x_pos, giorni)
        plt.ylabel('n° ele. tavolo')
        plt.xlabel('Giorno')
        plt.title('n°ele. tot com. tavolo X giorno')
        plt.xticks(rotation=90)


#  Numero di ELEMENTI comande d'ASPORTO al GIORNO
        plt.subplot(2,2,4)
        x_pos = np.arange(len(giorni))
        plt.bar(x_pos, elementiOrdineAsporto.values(), align='center')
        plt.xticks(x_pos, giorni)
        plt.ylabel('n° ele. asporto')
        plt.xlabel('Giorno')
        plt.title('n°ele. tot com. asporto X giorno')
        plt.xticks(rotation=90)


        plt.tight_layout(pad=5.0)

        plt.subplot_tool()
        plt.show()











