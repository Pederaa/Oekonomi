from Betalinger_class import Betalinger

def slaaSammenDager(betalinger):
    ny_betalingsliste = Betalinger()
    ny_betalingsliste.append(betalinger[0])
    ny_betalingsliste[-1].forklaring = None

    for betaling in betalinger[1:len(betalinger)]:
        if betaling.dato == ny_betalingsliste[-1].dato:
            ny_betalingsliste[-1].utFraKonto += betaling.utFraKonto
            ny_betalingsliste[-1].innPaaKonto += betaling.innPaaKonto
        else:
            ny_betalingsliste.append(betaling)
            ny_betalingsliste[-1].forklaring = None
    
    return ny_betalingsliste

def slaaSammenUker(betalinger):
    ny_betalingsliste = Betalinger()
    ny_betalingsliste.append(betalinger[0])
    ny_betalingsliste[-1].forklaring = None

    for betaling in betalinger[1:len(betalinger)]:
        if betaling.datestamp.week == ny_betalingsliste[-1].datestamp.week:
            ny_betalingsliste[-1].utFraKonto += betaling.utFraKonto
            ny_betalingsliste[-1].innPaaKonto += betaling.innPaaKonto
        else:
            ny_betalingsliste.append(betaling)
            ny_betalingsliste[-1].forklaring = None
    
    return ny_betalingsliste