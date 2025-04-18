måneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

class Betaling:
    def __init__(self, datestamp, forklaring, utFraKonto, innPaaKonto):
        self.dato = datestamp.day
        self.month = måneder[datestamp.month-1]
        self.year = datestamp.year

        self.datestamp = datestamp

        self.forklaring = forklaring
        self.utFraKonto = utFraKonto
        self.innPaaKonto = innPaaKonto

        self.kategorier = []


class Betalinger:
    def __init__(self):
        self.list = []

    def append(self, betaling):
        self.list.append(betaling)
    
    def sum(self):
        innskudd = 0
        utgift = 0
        for betaling in self.list:
            innskudd += betaling.innPaaKonto
            utgift += betaling.utFraKonto
        
        return utgift, innskudd
