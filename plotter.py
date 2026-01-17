import matplotlib.pyplot as plt
from betalingsSorterer import *
import datetime as dt
from Betalinger_class import Betaling

from operator import attrgetter

class Plot:
    def __init__(self, numberOfPlots=1):
        self.fig, self.ax = plt.subplots(numberOfPlots)
        self.numberOfPlots = numberOfPlots
    
    def checkInInfexOutOuBounds(self, index):
        if(index >= self.numberOfPlots):
            raise IndexError
    
    def show(self): plt.show()

    def plotlinefortoday(self, now, ymax : int):
        plt.vlines(x=now, ymin=0, ymax=ymax, linestyles="dotted", color="Black")
    
    def addTitle(self, betalinger, index=None):
        if index == None:
            self.ax.set_title(betalinger.tittel)
            self.ax.set_xlabel(betalinger.xlabel)
            self.ax.set_ylabel(betalinger.currency)
            return

        self.ax[index].set_title(betalinger.tittel)
        self.ax[index].set_xlabel(betalinger.xlabel)
        self.ax[index].set_ylabel(betalinger.currency)

    def plotLinjeDiagram(self, betalinger, index=None):
        x = []
        y = []
        if index == None:
            for bet in betalinger:
                x.append(bet.datestamp)
                y.append(bet.utFraKonto)

            self.ax.plot(x, y)
            self.addTitle(betalinger, index=index)
            self.plotlinefortoday(dt.datetime.now(), max(betalinger, key=attrgetter('utFraKonto')).utFraKonto)
            return

        self.checkInInfexOutOuBounds(index)
        for bet in betalinger:
            x.append(bet.datestamp)
            y.append(bet.utFraKonto)
        self.ax[index].plot(x, y)
        self.addTitle(betalinger, index=index)

    # Todo: endre på denne
    """
    def plottSector(self, index, betalinger, tagmanager):
        self.checkInInfexOutOuBounds(index)
        tagmanager = basicTagManager()
        betalingerEtterTag = sorterBetalingerEtterTags(betalinger, tagmanager)

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
        self.addTitle(betalinger, index=index)
        """
