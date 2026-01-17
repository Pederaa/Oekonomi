from lagBetalingsliste import *
from betalingsSorterer import *
from slaaSammen import *
from exceldokument import *
from plotter import *
from tagManager import *

def weekly(betalinger):
    ukentligeBetalinger = slaaSammenUker(betalinger)
    ukentligeBetalinger.tittel = "Ukentlige betalinger år for år"

    plot = Plot(1)
    plot.plotLinjeDiagram(ukentligeBetalinger)
    plot.show()

def ingentag(betalinger):
    tagmanager = basicTagManager()

    annet_betalinger = kunTag(betalinger, ["Annet"], tagmanager)
    annet_betalinger.tittel = "Ukjente betalinger"

    plot = Plot()
    plot.plotLinjeDiagram(annet_betalinger)
    plot.show()

def handlevarer(betalinger):
    tagmanager = basicTagManager()

    handlevare_betalinger = kunTag(betalinger, ["Handlevarer"], tagmanager)
    handlevare_betalinger.tittel = "Alle handlevarer"

    plot = Plot()
    plot.plotLinjeDiagram(handlevare_betalinger)
    plot.show()

def reise(betalinger):
    tagmanager = basicTagManager()

    reise_betalinger = kunTag(betalinger, ["Reise"], tagmanager)
    reise_betalinger.tittel = "Penger brukt på reise"

    plot = Plot()
    plot.plotLinjeDiagram(reise_betalinger)
    plot.show()