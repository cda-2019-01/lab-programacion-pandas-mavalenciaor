##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd
import numpy as np

df = pd.read_csv('tbl0.tsv', delim_whitespace=True)
aux = df.copy()
anios = []
for i in aux['_c3']:
    anios.append(i.split("-")[0].replace("0     ", ""))
aux['ano'] = anios
print(aux)