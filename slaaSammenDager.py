from Betalinger_class import Betalinger

def slaaSammenDager(betalinger):
    ny_betalingsliste = Betalinger()
    ny_betalingsliste.append(betalinger[0])

    for betaling in betalinger[1:len(betalinger)]:
        if betaling.dato == ny_betalingsliste[-1].dato:
            ny_betalingsliste[-1].utFraKonto += betaling.utFraKonto
            ny_betalingsliste[-1].innPaaKonto += betaling.innPaaKonto
        else:
            ny_betalingsliste.append(betaling)
    
    return ny_betalingsliste