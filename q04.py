##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 

import pandas as pd
import numpy as np

df = pd.read_csv('tbl1.tsv', delim_whitespace=True)
l = df['_c4'].values
l = sorted(set(l))
print([i.upper() for i in l])