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

"""
print("Dato: ", end="")
print(betalinger.list[0].datestamp)
print("Forklaring: ", end="")
print(betalinger.list[0].forklaring)
print("Ut: ", end="")
print(betalinger.list[0].utFraKonto)
print("Inn: ", end="")
print(betalinger.list[0].innPaaKonto)

"""
g = betalinger.lagNpArray()

print("Dato: ", end="")
print(g[0][0])
print("Forklaring: ", end="")
print(g[0][1])
print("Ut: ", end="")
print(g[0][2])
print("Inn: ", end="")
print(g[0][3])

"""
for i in range(len(g)):
    print(str(g[0]) + " " + str(g[1]) + " " + str(g[2]) + " " + str(g[3]))
    print()
    print()
"""
