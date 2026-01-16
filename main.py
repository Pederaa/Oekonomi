import os
import screens
from tagManager import basicTagManager
from lagBetalingsliste import lagListeAvBetalinger

# Kodesnutt som sjekker hvor mappen med betalinger ligger. Den ligger forskjellig sted på laptop enn pc
inputmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//NTNU//Økonomi//Betalinger" 
if not os.path.isdir(inputmappe):
    inputmappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//GitHub//Betalinger" 
    if not os.path.isdir(inputmappe):
        raise FileExistsError(f"Ingen mappe funnet: {inputmappe}")


print("Program started")
tagmanager = basicTagManager()
betalinger = lagListeAvBetalinger(inputmappe, tagmanager)
utskriftsmappe = "C://Users//Peder Aa. Hoff//OneDrive - NTNU//Dokumenter//GitHub//Betalinger//Output"

def do_nothing(b):
    pass

options = {
    "Ukentlig": screens.weekly_b_year,
    "Ingenting": do_nothing
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
            print("Må gi et tall")
            continue

    c = 0
    for option, funct in options.items():
        if c == answer:
            funct(betalinger)
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