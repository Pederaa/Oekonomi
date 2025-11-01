import matplotlib.pyplot as plt
import Betalinger_class
from matplotlib.dates import DateFormatter
import datetime

from betalingsSorterer import *


class Plot:
    def __init__(self, numberOfPlots):
        self.fig, self.ax = plt.subplots(numberOfPlots)
        self.numberOfPlots = numberOfPlots
    
    def checkInInfexOutOuBounds(self, index):
        if(index >= self.numberOfPlots):
            raise IndexError
    
    def show(self): plt.show()
    
    def addTitles(self, index, betalinger):
        self.ax[index].set_title(betalinger.tittel)
        self.ax[index].set_xlabel(betalinger.xlabel)
        self.ax[index].set_ylabel(betalinger.currency)

    def plotRekke(self, index, betalinger):
        self.checkInInfexOutOuBounds(index)
        x = []
        y = []
        for betaling in betalinger:
            x.append(betaling.datestamp)
            y.append(betaling.utFraKonto)

        self.ax[index].plot(x, y)
        self.addTitles(index, betalinger)


    def plottEtterÅr(self, index, betalinger):
        self.checkInInfexOutOuBounds(index)
        betalingerSortertTid = sorterEtterAar(betalinger)

        for aar, value in betalingerSortertTid.items():
            x = []
            y = []
            for betaling in value:
                x.append(betaling.datestamp.replace(year=1999))
                y.append(betaling.utFraKonto)

            self.ax[index].plot(x, y, label=str(aar))

        date_form = DateFormatter("%d.%m")
        self.ax[index].xaxis.set_major_formatter(date_form)
        self.ax[index].legend()
        self.addTitles(index, betalinger)

    # Todo: endre på denne
    def plottSector(self, index, betalinger, tagmanager):
        self.checkInInfexOutOuBounds(index)
        betalingerEtterTag = sorterBetalingerEtterTags(betalinger)

        tager = list(tagmanager.getTags())

        tagerAaPlotte = []
        sums = []
        for tag in tager:
            totalUtgift = betalingerEtterTag[tag].sum()[0]
            if (totalUtgift == 0):
                continue

            tagerAaPlotte.append(tag)
            sums.append(betalingerEtterTag[tag].sum()[0])
        
        self.ax[index].pie(sums, labels=tagerAaPlotte)
        self.addTitles(index, betalinger)
