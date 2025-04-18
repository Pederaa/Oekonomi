from Modul1 import lagListeAvBetalinger
from Modul2 import sorterEtterAarmanneder

dataFil = "okt23_nov24.xlsx"
betalinger_liste = lagListeAvBetalinger(dataFil)
betalinger_sortert_etter_aarmaneder = sorterEtterAarmanneder(betalinger_liste)



# betalinger_sortert_etter_type_og_aarmaneder = sorterBetalingerEtterType(betalinger_liste)


print(betalinger_sortert_etter_aarmaneder)
