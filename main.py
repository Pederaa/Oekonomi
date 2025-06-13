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
from plotter import plottEtterÅr, plottSector

from Betalinger_class import Betalinger

# inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger"
inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger"

print("Program started")
betalinger = lagListeAvBetalinger(inputmappe) # Ordner betalingene (egen class) i en egen liste fra exel-dokumentet

utskriftsmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"

nye_betalinger = kunKategori(betalinger, ["Lønn"])
#nye_betalinger = slaaSammenUker(nye_betalinger)


dok = excelDokument(nye_betalinger)
dok.columns = ["År", "Dato", "Forklaring", "Ut", "Inn"]
dok.make("Handlevarer per uke.xlsx", utskriftsmappe)

plottEtterÅr(nye_betalinger)

#plottSector(betalinger)
print("Program Completes")