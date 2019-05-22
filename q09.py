##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd
import numpy as np

df = pd.read_csv('tbl0.tsv', delim_whitespace=True)
aux = df.sort_values('_c2').copy()
aux['_c2'] = aux['_c2'].astype(str)
aux = aux.groupby('_c1').agg({'_c2' : lambda x: ':'.join(x)}).reset_index()
aux = aux.rename(columns={ aux.columns[0]: "_c0" }).rename(columns={ aux.columns[1]: "lista" })
print(aux)