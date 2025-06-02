import numpy as np
import pandas as pd
from datetime import datetime as dt

from lagBetalingsliste import lagListeAvBetalinger
from sorterEtterMånder import sorterEtterAarmanneder
from sorterBetalingerEtterKategori import sorterBetalingerEtterKategori, fjernKategori
from slaaSammen import slaaSammenDager, slaaSammenUker
from exceldokument import excelDokument

inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger"

# Ordner betalingene (egen class) i en egen liste fra exel-dokumentet
betalinger = lagListeAvBetalinger(inputmappe)

#for betaling in betalinger:
    #print(betaling.datestamp)

# Fjerner kategorier jeg ikke vil ha med
#betalinger = fjernKategori(betalinger, ["Ikke relevant", "Lønn", "Leie"])

# Slå sammen uker i en betaling 
betalinger = slaaSammenUker(betalinger)

# Sorterer betalingene i en dict hvor nøkkelen er på formen "år-måned"
# betalingerSortertTid = sorterEtterAarmanneder(betalinger)

# Sorterer betalingene i en dict hvor nøkkelen er etter hvilken kategori den tilhører
# betalingerSortertKatagori = sorterBetalingerEtterKategori(betalinger)

utskriftsmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Output"

dok = excelDokument(betalinger)
dok.columns = ["År", "Uke", "Ut", "Inn"]
dok.make("Output.xlsx", utskriftsmappe)