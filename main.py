import numpy as np
import pandas as pd
from datetime import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from lagBetalingsliste import lagListeAvBetalinger
from betalingsSorterer import sorterEtterAarmanneder, sorterBetalingerEtterKategori
from kategoriManager import fjernKategori, kunKategori
from slaaSammen import slaaSammenDager, slaaSammenUker
from exceldokument import excelDokument
from plotter import Plot

from Betalinger_class import Betalinger

# inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger"
inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger"

print("Program started")
betalinger = lagListeAvBetalinger(inputmappe) # Ordner betalingene (egen class) i en egen liste fra exel-dokumentet

utskriftsmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"

betalinger = fjernKategori(betalinger, ["Ikke relevant", "Annet"])
ukentligeBetalinger = slaaSammenUker(betalinger)

dok = excelDokument(ukentligeBetalinger)
dok.columns = ["År", "Dato", "Forklaring", "Ut", "Inn"]
dok.make("Handlevarer per uke.xlsx", utskriftsmappe)

plot = Plot(3)
plot.plottEtterÅr(0, ukentligeBetalinger)
plot.plottEtterÅr(1, betalinger)
plot.plottSector(2, betalinger)

plot.show()

print("Program Completes")