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
if not os.path.isdir(inputmappe):
    inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger" #Laptop

    if not os.path.isdir(inputmappe):
        raise FileExistsError(f"Ingen mappe funnet: {inputmappe}")

# inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger" #Laptop

print("Program started")

tagmanager = basicTagManager()
betalinger = lagListeAvBetalinger(inputmappe, tagmanager)
utskriftsmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"

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
    print(f"{c}: Exit")

    while True:
        try:
            answer = int(input(""))
            break
        except:
            print("Must input number")
            continue

    c = 0
    for option, funct in options.items():
        if c == answer:
            print(f"Running funtion {option}")
        c += 1
    if c == answer:
        print("Exiting application")
        break

    print()
    print()
    print()

"""
betalinger = fjernTager(betalinger, ["Handlevarer"])
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
"""