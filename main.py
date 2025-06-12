import numpy as np
import pandas as pd
from datetime import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from lagBetalingsliste import lagListeAvBetalinger
from betalingsSorterer import sorterEtterAarmanneder, sorterBetalingerEtterKategori
from kategoriManager import fjernKategori
from slaaSammen import slaaSammenDager, slaaSammenUker
from exceldokument import excelDokument
from plotter import plottEtterÅr

from Betalinger_class import Betalinger

# inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger"
inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger"

print("Program started")
# Ordner betalingene (egen class) i en egen liste fra exel-dokumentet
betalinger = lagListeAvBetalinger(inputmappe)

#for betaling in betalinger:
    #print(betaling.datestamp)

# Fjerner kategorier jeg ikke vil ha med
#betalinger = fjernKategori(betalinger, ["Ikke relevant", "Lønn", "Leie"])

# Slå sammen uker i en betaling 
#betalinger_per_uke = slaaSammenUker(betalinger)

# Sorterer betalingene i en dict hvor nøkkelen er på formen "år-måned"

# Sorterer betalingene i en dict hvor nøkkelen er etter hvilken kategori den tilhører
# betalingerSortertKatagori = sorterBetalingerEtterKategori(betalinger)

utskriftsmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"


#dok = excelDokument(betalinger_per_uke)
#dok.columns = ["År", "Uke", "Ut", "Inn"]
#dok.make("Output.xlsx", utskriftsmappe)

nye_betalinger = fjernKategori(betalinger, ["Ikke relevant", "Lønn" "Leie"])
nye_betalinger = slaaSammenUker(nye_betalinger)

plottEtterÅr(nye_betalinger)

print("Program Completes")