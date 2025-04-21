import numpy as np
import pandas as pd
from datetime import datetime as dt
from itertools import zip_longest
import os
import xlsxwriter
#from xlsxwriter.utility import xl_rowcol_to_cell

måneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

class Betaling():
    def __init__(self, datestamp, forklaring, utFraKonto, innPaaKonto):
        self.dato = datestamp.day
        self.month = måneder[datestamp.month-1]
        self.year = datestamp.year

        self.datestamp = datestamp

        self.forklaring = forklaring
        self.utFraKonto = utFraKonto
        self.innPaaKonto = innPaaKonto

        self.kategorier = []
    
    def tonpArray(self):
        row = np.empty(4, dtype=object)
        row[0] = str(self.dato) + ". " + str(self.month)
        row[1] = self.forklaring
        row[2] = self.utFraKonto
        row[3] = self.innPaaKonto

        return row


class Betalinger(list):
    def __init__(self):
        pass
    
    def sum(self):
        innskudd = 0
        utgift = 0
        for betaling in self:
            innskudd += betaling.innPaaKonto
            utgift += betaling.utFraKonto
        
        return utgift, innskudd

    def lagSheet(self):
        sheet = np.empty((len(self)+1, 4), dtype=object)
        total = [0, 0]

        for i in range(len(self)):
            betaling = self[i]

            r = betaling.tonpArray()
            sheet[i][0] = r[0]
            sheet[i][1] = r[1]
            sheet[i][2] = r[2]
            sheet[i][3] = r[3]

            total[0] += betaling.utFraKonto
            total[1] += betaling.innPaaKonto
    
        sheet[-1][1] = "Total:"
        sheet[-1][2] = total[0]
        sheet[-1][3] = total[1]
    
        return sheet
    
    def toExcel(self, filname, sheet, **kwargs):
        try:
            sheet_name = kwargs["sheet_name"]
        except:
            sheet_name = "Ark 1"

        with pd.ExcelWriter(filname, engine="xlsxwriter") as writer:
            to_write = pd.DataFrame(sheet, columns=["År", "Måned", "Ut", "Inn"])
            to_write.to_excel(writer, sheet_name=sheet_name)

            worksheet = writer.sheets[sheet_name]
            # worksheet.set_zoom(90)

            workbook = writer.book
            money_fmt = workbook.add_format({'num_format': '#,##0.00'})
            bold_fmt = workbook.add_format({'bold': True, 'num_format': '#,##0.00'})

            worksheet.set_column('A:B', 8)      # Indeks og årstall
            worksheet.set_column('C:C', 15)     # Måned
            worksheet.set_column('D:E', 15, money_fmt)  # /Inn/ut
            worksheet.set_row(len(sheet), 21, bold_fmt)  # Total-rad