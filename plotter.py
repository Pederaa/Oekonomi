import matplotlib.pyplot as plt
import Betalinger_class
from matplotlib.dates import DateFormatter
import datetime

from betalingsSorterer import sorterEtterAarmanneder, sorterEtterAar

def plottEtterÅr(betalinger):
    betalingerSortertTid = sorterEtterAar(betalinger)

    fig, ax = plt.subplots()
    for aar, value in betalingerSortertTid.items():
        x = []
        y = []
        for betaling in value:
            x.append(betaling.datestamp.replace(year=1999))
            y.append(betaling.utFraKonto)

        ax.plot(x, y, label=str(aar))

    date_form = DateFormatter("%d.%m")
    ax.xaxis.set_major_formatter(date_form)

    plt.legend()
    plt.show()