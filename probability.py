from xlrd import open_workbook
from numpy import zeros

_p = open_workbook(".\p.xls").sheets()[0]
_rows = [_p.row(row)[1:] for row in range(1, 51)]
_dats = zeros((51, 50), int)
for i in range(50):
    for j in range(50):
        _dats[i + 1][j] = int(_rows[i][j].value)
    for j in range(1, 50):
        _dats[i + 1][j] += _dats[i + 1][j - 1]
PROBABILITY = _dats
