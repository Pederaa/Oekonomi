import matplotlib.pyplot as plt
from betalingsSorterer import *


class Plot:
    def __init__(self, numberOfPlots):
        self.fig, self.ax = plt.subplots(numberOfPlots)
        self.numberOfPlots = numberOfPlots
    
    def checkInInfexOutOuBounds(self, index):
        if(index >= self.numberOfPlots):
            raise IndexError
    
    def show(self): plt.show()
    
    def addTitle(self, betalinger, index=False):
        if index == False:
            self.ax.set_title(betalinger.tittel)
            self.ax.set_xlabel(betalinger.xlabel)
            self.ax.set_ylabel(betalinger.currency)
            return

        self.ax[index].set_title(betalinger.tittel)
        self.ax[index].set_xlabel(betalinger.xlabel)
        self.ax[index].set_ylabel(betalinger.currency)

    def plotLinjeDiagram(self, betalinger, index=False):
        x = []
        y = []
        if index == False:
            for betaling in betalinger:
                x.append(betaling.datestamp)
                y.append(betaling.utFraKonto)

            self.ax[index].plot(x, y)
            self.addTitle(index, betalinger)
            return

        self.checkInInfexOutOuBounds(index)
        for betaling in betalinger:
            x.append(betaling.datestamp)
            y.append(betaling.utFraKonto)
        self.ax[index].plot(x, y)
        self.addTitle(index, betalinger)

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
        self.addTitle(index, betalinger)
