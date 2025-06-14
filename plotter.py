import matplotlib.pyplot as plt
import Betalinger_class
from matplotlib.dates import DateFormatter
import datetime

from betalingsSorterer import sorterEtterAarmanneder, sorterEtterAar, sorterBetalingerEtterKategori
from kategoriidentifiserer import getKategorier


class Plot:
    def __init__(self, numberOfPlots):
        self.fig, self.ax = plt.subplots(numberOfPlots)
        self.numberOfPlots = numberOfPlots
    
    def checkInInfexOutOuBounds(self, index):
        if(index >= self.numberOfPlots):
            raise IndexError
    
    def show(self):
        plt.show()


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



    def plottSector(self, index, betalinger):
        self.checkInInfexOutOuBounds(index)
        betalingerEtterKategori = sorterBetalingerEtterKategori(betalinger)

        kategorier = list(getKategorier())

        sums = []
        for kategori in kategorier:            
            print(str(kategori) + ": " + str(betalingerEtterKategori[kategori].sum()[0]))
            sums.append(betalingerEtterKategori[kategori].sum()[0])
                    
        print(kategorier)
        print(sums)
        self.ax[index].pie(sums, labels=kategorier)
