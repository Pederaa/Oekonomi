import numpy as np
import pandas as pd
from datetime import datetime as dt
from itertools import zip_longest

måneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

class Betaling():
    def __init__(self, datestamp, forklaring, utFraKonto, innPaaKonto):
        self.dato = datestamp.day
        self.month = måneder[datestamp.month-1]
        self.year = datestamp.year
        self.gooning = 2

        self.datestamp = datestamp

        self.forklaring = forklaring
        self.utFraKonto = utFraKonto
        self.innPaaKonto = innPaaKonto

        self.kategorier = []
    
    def tonpArray(self, columns):
        row = np.empty(len(columns), dtype=object)
        for j in range(len(columns)):
            match columns[j]:
                case "Dato":
                    row[j] = str(self.dato) + ". " + str(self.month) + " " + str(self.year)
                case "År":
                    row[j] = self.year
                case "Måned":
                    row[j] = str(self.month)
                case "Forklaring":
                    row[j] = self.forklaring
                case "Ut":
                    row[j] = self.utFraKonto
                case "Inn":
                    row[j] = self.innPaaKonto
                case "Uke":
                    row[j] = self.datestamp.week
                case "datestamp":
                    row[j] = self.datestamp
                case _:
                    raise Exception("Ukjent kolonne") 
        return row


class Betalinger(list):
    def __init__(self):
        self.columns = ["År", "Måned", "Ut", "Inn"]
    
    def sum(self):
        innskudd = 0
        utgift = 0
        for betaling in self:
            innskudd += betaling.innPaaKonto
            utgift += betaling.utFraKonto
        
        return utgift, innskudd

    def lagSheet(self):
        sheet = np.empty((len(self), len(self.columns)), dtype=object)

        for i in range(len(self)):
            betaling = self[i]

            r = betaling.tonpArray(self.columns)
            for j in range(len(self.columns)):
                sheet[i][j] = r[j]   
        return sheet
    
    def toExcel(self, filname, **kwargs):
        sheet = self.lagSheet()
        try:
            sheet_name = kwargs["sheet_name"]
        except:
            sheet_name = "Ark 1"

        with pd.ExcelWriter(filname, engine="xlsxwriter") as writer:
            to_write = pd.DataFrame(sheet, columns=self.columns)
            to_write.to_excel(writer, sheet_name=sheet_name)

            worksheet = writer.sheets[sheet_name]
            # worksheet.set_zoom(90)

            workbook = writer.book
            money_fmt = workbook.add_format({'num_format': '#,##0.00'})
            bold_fmt = workbook.add_format({'bold': True, 'num_format': '#,##0.00'})

            worksheet.set_column('A:B', 8)      # Indeks og årstall
            worksheet.set_column('C:C', 15)     # Måned
            worksheet.set_column('D:E', 15, money_fmt)  # /Inn/ut

            # Totalen
            worksheet.write(len(sheet)+1, 3, '=SUM(D2:D' + str(len(sheet)-1) + str(")"))
            worksheet.write(len(sheet)+1, 4, '=SUM(E2:E' + str(len(sheet)-1) + str(")"))
            worksheet.set_row(len(sheet)+1, 21, bold_fmt)  # Total-rad

            # Utgifter
            worksheet.write(0, 6, 0)
            worksheet.write('F2:F' + str(len(sheet)), "=")