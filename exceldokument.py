import pandas as pd
import numpy as np

import os

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
        print("Lager excel-dokument i mappe: " + folder)
        sheet = self.lagSheet(self.betalinger)
        try:
            sheet_name = kwargs["sheet_name"]
        except:
            sheet_name = "Ark 1"

        fullpath = os.path.join(folder, filname)
        with pd.ExcelWriter(fullpath, engine="xlsxwriter") as writer:
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

        print("Document" + str(filname) + "made")
