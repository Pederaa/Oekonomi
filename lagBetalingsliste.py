import numpy as np
import pandas as pd
import os

from Betalinger_class import *
from tagManager import *

def lagListeAvBetalinger(foldernavn, tagmanager):
    print("Henter betalinger fra: " + foldernavn)
    kombinertListeAvBetalinger = Betalinger()
    for filename in os.listdir(foldernavn):
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            path = os.path.join(foldernavn, filename)
            print("\t Henter fil: " + filename)
            betalinger = pd.read_excel(path)

            betalinger["Inn på konto"] = betalinger["Inn på konto"].fillna(0)
            betalinger["Ut fra konto"] = betalinger["Ut fra konto"].fillna(0)

            np_data = betalinger.to_numpy()
            np_data = np.delete(np_data, 2, 1)

        for i in range(0, len(np_data)): # Sorterer betalingen etter måned år.
            new_betaling = Betaling(np_data[i][0], np_data[i][1], np_data[i][2], np_data[i][3])
            new_betaling.tags = findTags(new_betaling, tagmanager)
            kombinertListeAvBetalinger.append(new_betaling)

    print("Sletter duplikater")
    kombinertListeAvBetalinger = Betalinger(set(kombinertListeAvBetalinger))
    kombinertListeAvBetalinger.sorts()

    print("Betalinger fra " + foldernavn + " ferdig hentet.")
    print()
    print()
    
    return kombinertListeAvBetalinger