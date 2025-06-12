import Betalinger_class
import pandas as pd
from datetime import datetime as dt
from itertools import zip_longest
import numpy as np

class excelDokument():
    def __init__(self, betalinger_):
        self.betalinger = betalinger_
        self.columns = ["År", "Måned", "Forklaring", "Inn", "Ut"]
    
    def lagSheet(self, betalinger):
        sheet = np.empty((len(betalinger), len(self.columns)), dtype=object)

        for i in range(len(betalinger)):
            betaling = betalinger[i]

            r = betaling.tonpArray(self.columns)
            for j in range(len(self.columns)):
                sheet[i][j] = r[j]   
        return sheet


    def make(self, filname, folder, **kwargs):
        sheet = self.lagSheet(self.betalinger)
        try:
            sheet_name = kwargs["sheet_name"]
        except:
            sheet_name = "Ark 1"

        with pd.ExcelWriter(folder+"//"+filname, engine="xlsxwriter") as writer:
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
