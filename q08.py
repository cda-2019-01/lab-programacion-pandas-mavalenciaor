##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd
import numpy as np

df = pd.read_csv('tbl0.tsv', delim_whitespace=True)
aux = df.copy()
aux['ano'] = str(aux['_c3']).split("-")[0].replace("0     ", "")
print(aux)