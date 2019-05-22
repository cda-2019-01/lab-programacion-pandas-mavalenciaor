##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

import pandas as pd
import numpy as np

df_a = pd.read_csv('tbl0.tsv', delim_whitespace=True)
df_b = pd.read_csv('tbl2.tsv', delim_whitespace=True)
df_c = pd.merge(df_a, df_b, left_on='_c0', right_on='_c0', how='inner')

#print(df_a)
#print(df_b)

#print(df_c)
print(df_c.groupby('_c1').sum()['_c5b'])