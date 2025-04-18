from lagBetalingsliste import lagListeAvBetalinger
from sorterEtterMånder import sorterEtterAarmanneder
from sorterBetalingerEtterKategori import sorterBetalingerEtterKategori

filnavn = "okt23_nov24.xlsx"
print("Hello world")
# Ordner betalingene (egen class) i en egen liste fra exel-dokumentet
betalinger_liste = lagListeAvBetalinger(filnavn) 


# Sorterer betalingene i en dict hvor nøkkelen er på formen "år-måned"
betalinger_sortert_etter_aarmaneder = sorterEtterAarmanneder(betalinger_liste)

# Sorterer betalingene i en dict hvor nøkkelen er etter hvilken kategori den tilhører
betalinger_sortert_etter_katagori = sorterBetalingerEtterKategori(betalinger_liste)


print(betalinger_sortert_etter_katagori)
"""
for betaling in betalinger_sortert_etter_katagori:
    print(str(betaling.year) + "-" + str(betaling.month) + "-" + str(betaling.dato), end="\t")
    print(float(betaling.innPaaKonto) - float(betaling.utFraKonto))
"""