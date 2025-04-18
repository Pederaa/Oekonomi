from kategoriidentifiserer import identifiserKategori

def sorterBetalingerEtterKategori(betalingsListe):
    sortertEtterKategori = {}

    for betaling in betalingsListe:
        kategori = identifiserKategori(betaling.forklaring)

        try:
           sortertEtterKategori[kategori].append(betaling)
        except:
            sortertEtterKategori[kategori] = []
    
    return sortertEtterKategori
