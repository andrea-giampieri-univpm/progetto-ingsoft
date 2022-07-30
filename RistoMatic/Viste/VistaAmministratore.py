import datetime
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView, QMessageBox,QApplication, QDialog
# TODO LUCA : Risolvere problema import VistaGrafico
from RistoMatic.Viste.VistaCalendario import VistaCalendario
from RistoMatic.Viste.VistaGestisciMenu import VistaGestisciMenu
from RistoMatic.Viste.VistaGestisciTavoli import VistaGestisciTavoli
from RistoMatic.Viste.VistaGrafico import VistaGrafico
from RistoMatic.GestioneAmministrativa.StatisticheEconomiche import StatisticheEconomiche
from RistoMatic.GestioneAmministrativa.StatisticheGestionali import StatisticheGestionali
from RistoMatic.GestioneAmministrativa.StatisticheGestionali import Statistiche
import datetime

from PySide6.QtWidgets import QApplication, QWidget, QCalendarWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QDateTimeEdit, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QTextCharFormat, QIcon

import pandas as pd

from RistoMatic.Viste.VistaUnlockAmministratore import VistaUnlockAmministratore
class VistaAmministratore(QtWidgets.QWidget):


    def __init__(self):

        super().__init__()

        hLayout = QHBoxLayout()
        buttonsLayout = QVBoxLayout()

        global newButton1
        self.statistiche = None
        newButton1 = QPushButton("Salva statistiche")
        newButton1.setEnabled(False)
        newButton1.clicked.connect(self.salvaStatistiche)
        newButton1.setStyleSheet('background-color: red')

        global infoButton
        infoButton = QPushButton("Genera Statistiche Economiche")
        infoButton.clicked.connect(self.statisticheEconomiche)
        infoButton.setStyleSheet('background-color: blue')

        global newButton
        newButton = QPushButton("Genera Statistiche Gestionali")
        newButton.clicked.connect(self.statisticheGestionali)
        newButton.setStyleSheet('background-color: blue')


        annullaButton = QPushButton('Reset')
        annullaButton.clicked.connect(self.reset)
        annullaButton.setStyleSheet('background-color: green')

        menuButton = QPushButton('Gestisci Menu')
        menuButton.clicked.connect(self.showMenu)
        menuButton.setStyleSheet('background-color: red')

        tavoloButton = QPushButton('Gestisci Tavoli')
        tavoloButton.clicked.connect(self.tavoli)
        tavoloButton.setStyleSheet('background-color: red')


        buttonsLayout.addWidget(newButton1)
        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)
        buttonsLayout.addWidget(annullaButton)
        buttonsLayout.addWidget(menuButton)
        buttonsLayout.addWidget(tavoloButton)

        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Amministrazione")




        ###      AGGIUNTA vistaCalendario CON SCELTA MULTIPLA   ###

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.calendar = VistaCalendario()  # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.layout.addWidget(self.calendar)
        hLayout.addLayout(self.layout)

        #btn = QPushButton('Conferma filtro')

       # btn.clicked.connect(self.calendar.acquisizioneGiorni)
        #self.layout.addWidget(btn)


    def salvaStatistiche(self):
        if(self.statistiche is None) : return
        self.statistiche.esportaStatistiche()
        msg = QMessageBox()
        msg.setWindowTitle('Statistiche RistoMatic')
        msg.setText("SUCCESSO !")
        msg.setInformativeText("Statistica salvata corretamente, prego controlla nella cartella ./Dati")
        msg.exec_()
        newButton1.setEnabled(False)
        infoButton.setEnabled(True)
        newButton.setEnabled(True)




    def statisticheEconomiche(self):
        vistaGrafico = VistaGrafico()

        if self.calendar.acquisizioneGiorni() is None :
          # Non ho inserito , nulla, avro i campi del costruttore di genera statistiche economiche vuoto
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Attenzione!")
          msg.setInformativeText("Non hai inserito nessun range di date, per convenzione verranno prese le ultime 24 ore !")
          msg.exec_()
          self.statistiche = StatisticheEconomiche(None,None)
          newButton1.setEnabled(True)
          newButton.setEnabled(False)
          vistaGrafico.graficoStatisticheEconomiche(self.statistiche.calcolaStatistiche())
        else:
            start,end=self.calendar.acquisizioneGiorni()

            if(datetime.date(end.year,end.month,end.day)>datetime.date.today() or datetime.date(start.year,start.month,start.day)==datetime.date(end.year,end.month,end.day)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Attenzione al range di date selezionate !")
                msg.exec_()
                return
            # Range di dati validi:
            else:
                self.statistiche = StatisticheEconomiche(start,end)
                newButton1.setEnabled(True)
                newButton.setEnabled(False)
                vistaGrafico.graficoStatisticheEconomiche(self.statistiche.calcolaStatistiche())
                #newButton1.clicked.connect(self.salvaStatistiche(statistiche))
                #print('Tipo oggetto: vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche) : ' ,type(vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche)))
                #print('Tipo oggetto statistiche.calcolaStatistiche()' , type(statistiche.calcolaStatistiche()))
                #vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
                #print(statistiche.generaStatistiche())






    def statisticheGestionali(self):

        vistaGrafico = VistaGrafico()

        if self.calendar.acquisizioneGiorni() is None :
          # Non ho inserito , nulla, avro i campi del costruttore di genera statistiche economiche vuoto
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Attenzione!")
          msg.setInformativeText("Non hai inserito nessun range di date, per convenzione verranno prese le ultime 24 ore !")
          msg.exec_()
          self.statistiche = StatisticheGestionali(None,None)
          ordiniAsporto,ordiniTavolo = self.statistiche.calcolaStatistiche()
          vistaGrafico.graficoStatisticheGestionali(ordiniAsporto,ordiniTavolo)
          newButton1.setEnabled(True)
          infoButton.setEnabled(False)
          #print(statistiche.generaStatistiche())
         # vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
        else:
            start,end=self.calendar.acquisizioneGiorni()

            if(datetime.date(end.year,end.month,end.day)>datetime.date.today() or datetime.date(start.year,start.month,start.day)==datetime.date(end.year,end.month,end.day)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Attenzione al range di date selezionate !")
                msg.exec_()
                return
            # Range di dati validi:
            else:
                self.statistiche = StatisticheGestionali(start,end)
                ordiniAsporto,ordiniTavolo = self.statistiche.calcolaStatistiche()
                vistaGrafico.graficoStatisticheGestionali(ordiniAsporto,ordiniTavolo)
                newButton1.setEnabled(True)
                infoButton.setEnabled(False)
                #print('ORDINI ASPORTO: ', a)
                #print('ORDINI TAVOLO: ', b)
                #print('Tipo oggetto: vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche) : ' ,type(vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche)))
                #print('Tipo oggetto statistiche.calcolaStatistiche()' , type(statistiche.calcolaStatistiche()))
                #vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
                #print(statistiche.generaStatistiche())




    def reset(self):
        newButton1.setEnabled(False)
        infoButton.setEnabled(True)
        newButton.setEnabled(True)



    def showMenu(self):
        self.menu = VistaGestisciMenu()
        self.menu.show()

    def tavoli(self):
        self.vistaTavoli = VistaGestisciTavoli()
        self.vistaTavoli.setWindowTitle('Gestione dei tavoli')
        self.vistaTavoli.show()

