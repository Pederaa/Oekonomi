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

# inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger"
inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger"

print("Program started")
betalinger = lagListeAvBetalinger(inputmappe) # Ordner betalingene (egen class) i en egen liste fra exel-dokumentet

utskriftsmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"

def func():
    pass

def funct2():
    pass

options = {
    "Delete all": func(),
    "Not delete all": funct2()
}

while True:
    c = 0
    for option in options.keys():
        print(f"{c}: {option}")
        c += 1
    
    while True:
        try:
            answer = int(input(""))
            break
        except:
            print("Must input number")
            continue

    c = 0
    for option, funct in options:
        if c == answer:
            print(f"Running funtion {option}")
            break

betalinger = fjernTager(betalinger, ["Handlevarer"])
ukentligeBetalinger = slaaSammenUker(betalinger)

dok = excelDokument(betalinger)
dok.columns = ["År", "Dato", "Forklaring", "Ut", "Inn"]
dok.make("Handlevarer", utskriftsmappe)

plot = Plot(2)
plot.plottEtterÅr(0, ukentligeBetalinger)
plot.plottEtterÅr(1, betalinger)

plot.show()

print("Program Complete")