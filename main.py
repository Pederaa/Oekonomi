import numpy as np
import pandas as pd
from datetime import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from lagBetalingsliste import *
from betalingsSorterer import *
from kategoriManager import *
from slaaSammen import *
from exceldokument import *
from plotter import *
from tagManager import *

from Betalinger_class import Betalinger

# inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger"
inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger"

print("Program started")
betalinger = lagListeAvBetalinger(inputmappe) # Ordner betalingene (egen class) i en egen liste fra exel-dokumentet

utskriftsmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"

betalinger = kunTag(betalinger, ["Handlevarer"])
ukentligeBetalinger = slaaSammenUker(betalinger)

dok = excelDokument(betalinger)
dok.columns = ["År", "Dato", "Forklaring", "Ut", "Inn"]
dok.make("Handlevarer", utskriftsmappe)

plot = Plot(2)
plot.plottEtterÅr(0, ukentligeBetalinger)
plot.plottEtterÅr(1, betalinger)

plot.show()

print("Program Complete")