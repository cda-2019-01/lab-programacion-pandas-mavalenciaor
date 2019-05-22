##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd
import numpy as np

df = pd.read_csv('tbl2.tsv', delim_whitespace=True)
df = df.sort_values('_c5a').copy()
df['_c5b'] = df['_c5b'].astype(str)
df['lista'] = df['_c5a'] +":"+ df['_c5b']
df = df.groupby('_c0').agg({'lista' : lambda x: ','.join(x)}).reset_index()
print(df)