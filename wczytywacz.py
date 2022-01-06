from wynik_liczenia import wynik_liczenia
from openpyxl import load_workbook

def wczytaj():
    wb = load_workbook('E:\\ĆWICZENIE.XLSX')
    ws = wb['Arkusz1']
    komorka_nr_uzyt_pierwszy = ws['A2']
    ws.delete_cols(komorka_nr_uzyt_pierwszy.column+0, amount=3)
    for row in ws.iter_rows(min_row = komorka_nr_uzyt_pierwszy.row, max_col= komorka_nr_uzyt_pierwszy.column+3, min_col = komorka_nr_uzyt_pierwszy.column, max_row = None, values_only = True):
        print(wynik_liczenia(row[0], row[1], row[2]))

if __name__ == '__main__':
    wczytaj()