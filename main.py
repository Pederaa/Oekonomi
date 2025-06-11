import numpy as np
import pandas as pd
from datetime import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

from lagBetalingsliste import lagListeAvBetalinger
from sorterEtterMånder import sorterEtterAarmanneder
from sorterBetalingerEtterKategori import sorterBetalingerEtterKategori, fjernKategori
from slaaSammen import slaaSammenDager, slaaSammenUker
from exceldokument import excelDokument

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
# betalingerSortertTid = sorterEtterAarmanneder(betalinger)

# Sorterer betalingene i en dict hvor nøkkelen er etter hvilken kategori den tilhører
# betalingerSortertKatagori = sorterBetalingerEtterKategori(betalinger)

utskriftsmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"


#dok = excelDokument(betalinger_per_uke)
#dok.columns = ["År", "Uke", "Ut", "Inn"]
#dok.make("Output.xlsx", utskriftsmappe)


x = []
y = []

nye_betalinger = fjernKategori(betalinger, ["Ikke relevant", "Lønn" "Leie"])
#nye_betalinger = slaaSammenUker(nye_betalinger)

for betaling in nye_betalinger:
    if betaling.datestamp.year == 2024:
        x.append(betaling.datestamp)
        y.append(betaling.utFraKonto)


fig, ax = plt.subplots(figsize=(12, 12))
ax.plot(x, y)

date_form = DateFormatter("%d.%m")
ax.xaxis.set_major_formatter(date_form)

plt.show()

print("Program Completes")