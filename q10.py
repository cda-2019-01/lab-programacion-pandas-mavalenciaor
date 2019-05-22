##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd
import numpy as np

df = pd.read_csv('tbl1.tsv', delim_whitespace=True)
aux = df.sort_values('_c4').copy()
aux = aux.groupby('_c0').agg({'_c4' : lambda x: ','.join(x)}).reset_index()
aux = aux.rename(columns={ aux.columns[1]: "lista" })
print(aux)