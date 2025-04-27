from kategoriidentifiserer import identifiserKategori
from Betalinger_class import *

def sorterBetalingerEtterKategori(betalinger):
    sortertEtterKategori = {}

    for betaling in betalinger:
        kategori = identifiserKategori(betaling.forklaring)

        try:
           sortertEtterKategori[kategori].append(betaling)
        except:
            sortertEtterKategori[kategori] = Betalinger()
    
    return sortertEtterKategori


def fjernKategori(betalinger, kategorierAaFjerne):
    ny_betalingsListe = Betalinger()
    for betaling in betalinger:
        betalingensKategori = identifiserKategori(betaling.forklaring)
        if betalingensKategori not in kategorierAaFjerne :
            ny_betalingsListe.append(betaling)
    
    return ny_betalingsListe