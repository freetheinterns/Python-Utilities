# Created By: Theodore Tenedorio
# Date: 10/29/2015
# Requires: Python2.7 & openpyxl

# 'https://pypi.python.org/pypi/openpyxl' or 'pip install openpyxl'
from openpyxl import load_workbook

# Reads the active worksheet of .xlsx (MS Excel 2010) into an array of columns.
# header variable skips the first row if true.
# WARNING: DATA MUST BE IN A SQUARE MATRIX (NO UNEVEN COLUMNS OR ROWS)
def read_xlsx(filename, header=True):
    wb = load_workbook(filename)
    rows = len(wb.active.rows)
    cols = len(wb.active.columns)
    data = []
    for x in range(cols):
        col = []
        for y in range(1 if header else 0, rows):
            col.append(wb.active.rows[y][x].value)
        data.append(col)
        
    return data
