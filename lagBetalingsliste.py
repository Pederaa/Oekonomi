import numpy as np
import pandas as pd
from Betalinger_class import *

def lagListeAvBetalinger(filnavn):
    mappe = "C://Users//Peder//OneDrive - NTNU//Dokumenter//Områder//Økonomi//Program//Økonomi"
    betalinger = pd.read_excel(mappe + "//" + filnavn)

    betalinger = betalinger.sort_values(['Dato'], ascending=True)
    betalinger["Inn på konto"].fillna(0, inplace=True)
    betalinger["Ut fra konto"].fillna(0, inplace=True)

    np_data = betalinger.to_numpy()
    np_data = np.delete(np_data, 2, 1)

    betalinger = Betalinger()
    for i in range(0, len(np_data)): # Sorterer betalingen etter måned år.
        new_betaling = Betaling(np_data[i][0], np_data[i][1], np_data[i][2], np_data[i][3])
        betalinger.append(new_betaling)

    return betalinger