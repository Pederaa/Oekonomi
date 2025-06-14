from kategoriidentifiserer import *
from Betalinger_class import *

def fjernKategori(betalinger, kategorierAaFjerne):
    ny_betalingsListe = Betalinger()
    for betaling in betalinger:
        betalingensKategori = identifiserKategori(betaling.forklaring)
        if betalingensKategori not in kategorierAaFjerne :
            ny_betalingsListe.append(betaling)
    
    return ny_betalingsListe

def kunKategori(betalinger, kategoriAaBeholde):
    ny_betalingsListe = Betalinger()
    for betaling in betalinger:
        betalingensKategori = identifiserKategori(betaling.forklaring)
        if betalingensKategori in kategoriAaBeholde:
            ny_betalingsListe.append(betaling)
    
    return ny_betalingsListe
