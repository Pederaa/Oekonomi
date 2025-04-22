import numpy as np
import pandas as pd
from datetime import datetime as dt

from lagBetalingsliste import lagListeAvBetalinger
from sorterEtterMånder import sorterEtterAarmanneder
from sorterBetalingerEtterKategori import sorterBetalingerEtterKategori
from slaaSammenDager import slaaSammenDager

filnavn = "okt23_nov24.xlsx"
print("Hello world")

# Ordner betalingene (egen class) i en egen liste fra exel-dokumentet
betalinger = lagListeAvBetalinger(filnavn) 
betalinger = slaaSammenDager(betalinger)

# Sorterer betalingene i en dict hvor nøkkelen er på formen "år-måned"
# betalingerSortertTid = sorterEtterAarmanneder(betalinger)

# Sorterer betalingene i en dict hvor nøkkelen er etter hvilken kategori den tilhører
# betalingerSortertKatagori = sorterBetalingerEtterKategori(betalinger)

mappe = "Betalinger"
utskriftsfil = "Test.xlsx"

betalinger.toExcel(utskriftsfil, sheet_name="Nytt ark")
