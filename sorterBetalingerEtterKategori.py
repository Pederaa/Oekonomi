from kategoriidentifiserer import identifiserKategori
from Betalinger_class import *

def sorterBetalingerEtterKategori(betalinger):
    sortertEtterKategori = {}

    for betaling in betalinger.list:
        kategori = identifiserKategori(betaling.forklaring)

        try:
           sortertEtterKategori[kategori].append(betaling)
        except:
            sortertEtterKategori[kategori] = Betalinger()
    
    return sortertEtterKategori
