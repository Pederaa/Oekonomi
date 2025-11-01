import numpy as np
import pandas as pd
from datetime import datetime as dt
from itertools import zip_longest

from Tag import *

måneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

class Betaling():
    def __init__(self, datestamp, forklaring, utFraKonto, innPaaKonto):
        self.dato = datestamp.day
        self.month = måneder[datestamp.month-1]
        self.year = datestamp.year
        self.currency = "kr"

        self.datestamp = datestamp

        self.forklaring = forklaring
        self.utFraKonto = utFraKonto
        self.innPaaKonto = innPaaKonto

        self.tags = Tags()
    
    def __eq__(self, other):
        return self.datestamp == other.datestamp and self.currency == other.currency and self.forklaring == other.forklaring and self.utFraKonto == other.utFraKonto and self.innPaaKonto == other.innPaaKonto

    def __hash__(self):
        return hash((self.datestamp, self.currency, self.forklaring, self.utFraKonto, self.innPaaKonto))
    
    def tonpArray(self, columns):
        row = np.empty(len(columns), dtype=object)
        for j in range(len(columns)):
            col = columns[j].lower()
            match col:
                case "dato":
                    row[j] = str(self.dato) + ". " + str(self.month) + " " + str(self.year)
                case "år":
                    row[j] = self.year
                case "måned":
                    row[j] = str(self.month)
                case "forklaring":
                    row[j] = self.forklaring
                case "ut":
                    row[j] = self.utFraKonto
                case "inn":
                    row[j] = self.innPaaKonto
                case "uke":
                    row[j] = self.datestamp.week
                case "datestamp":
                    row[j] = self.datestamp
                case _:
                    raise Exception('Ukjent kolonne: "' + columns[j] + '"')
            pass
        return row

class Betalinger(list):
    def __init__(self, items=None):
        self.tittel = "Betalinger"
        self.xlabel = "Tid"
        self.currency = "kr"
        
        if items is None:
            items = []
        super().__init__(items)
            
    def sum(self):
        innskudd = 0
        utgift = 0
        for betaling in self:
            innskudd += betaling.innPaaKonto
            utgift += betaling.utFraKonto
        
        return utgift, innskudd
    
    def sortByDatestamp(self):
        self.sort(key=lambda obj: obj.datestamp)