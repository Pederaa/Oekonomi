import numpy as np
import pandas as pd
from datetime import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from lagBetalingsliste import *
from betalingsSorterer import *
from slaaSammen import *
from exceldokument import *
from plotter import *
from tagManager import *

from Betalinger_class import Betalinger

import os

inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger" #PC 
# inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger" #Laptop

print("Program started")

tagmanager = basicTagManager()
betalinger = lagListeAvBetalinger(inputmappe, tagmanager)
utskriftsmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"

betalinger = kunTag(betalinger, ["Handlevarer"], tagmanager)
ukentligeBetalinger = slaaSammenUker(betalinger)
dagligebetalinger = slaaSammenDager(betalinger)

betalinger.tittel = "Vanlige betalinger"
ukentligeBetalinger.tittel = "Ukentlige betalinger"
dagligebetalinger.tittel = "Daglige betalinger"

plot = Plot(3)
plot.plotRekke(0, betalinger)
plot.plotRekke(2, ukentligeBetalinger)
plot.plotRekke(1, dagligebetalinger)

plot.show()

print("Program Complete")