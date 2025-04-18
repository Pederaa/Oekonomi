from lagBetalingsliste import lagListeAvBetalinger
from sorterEtterMånder import sorterEtterAarmanneder
from sorterBetalingerEtterKategori import sorterBetalingerEtterKategori

filnavn = "okt23_nov24.xlsx"
print("Hello world")
# Ordner betalingene (egen class) i en egen liste fra exel-dokumentet
betalinger = lagListeAvBetalinger(filnavn) 


# Sorterer betalingene i en dict hvor nøkkelen er på formen "år-måned"
betalingerSortertTid = sorterEtterAarmanneder(betalinger)

# Sorterer betalingene i en dict hvor nøkkelen er etter hvilken kategori den tilhører
betalingerSortertKatagori = sorterBetalingerEtterKategori(betalinger)
