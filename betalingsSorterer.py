from Betalinger_class import Betalinger
from kategoriidentifiserer import identifiserKategori, getKategorier


def sorterEtterAarmanneder(betalinger):
    maaneder_dict = {} #dict(zip_longest(maaneder_liste, [], fillvalue=[]))

    for betaling in betalinger:
        betelings_maaned = str(betaling.month) + " " + str(betaling.year)

        if not betelings_maaned in maaneder_dict:
            maaneder_dict[betelings_maaned] = Betalinger()
        maaneder_dict[betelings_maaned].append(betaling)

    maaneder_dict = dict(reversed(list(maaneder_dict.items())))
    return maaneder_dict

def sorterEtterAar(betalinger):
    aar_dict = {} #dict(zip_longest(maaneder_liste, [], fillvalue=[]))

    for betaling in betalinger:
        betelings_maaned = betaling.year

        if not betelings_maaned in aar_dict:
            aar_dict[betelings_maaned] = Betalinger()
        aar_dict[betelings_maaned].append(betaling)

    aar_dict = dict(reversed(list(aar_dict.items())))
    return aar_dict


def sorterBetalingerEtterKategori(betalinger):
    sortertEtterKategori = dict.fromkeys(getKategorier())
    for item in sortertEtterKategori.keys():
        sortertEtterKategori[item] = Betalinger()

    for betaling in betalinger:
        kategori = identifiserKategori(betaling.forklaring)

        if(kategori not in sortertEtterKategori):
            raise "Kategori " + str(kategori) + " not found"
        
        sortertEtterKategori[kategori].append(betaling)
    
    return sortertEtterKategori
