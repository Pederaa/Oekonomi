from lagBetalingsliste import *
from betalingsSorterer import *
from slaaSammen import *
from exceldokument import *
from plotter import *
from tagManager import *

def weekly_b_year(betalinger):
    ukentligeBetalinger = slaaSammenUker(betalinger)
    ukentligeBetalinger.tittel = "Ukentlige betalinger år for år"

    plot = Plot(1)
    plot.plotLinjeDiagram(ukentligeBetalinger)
    plot.show()