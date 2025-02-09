# Correlação entre latitude e longitude das unidades de saúde

import pandas as pd

def correlacao_lat_long(data: pd.DataFrame):
  corr_lat_long = data[['NU_LATITUDE', 'NU_LONGITUDE']].corr()
  
  print(corr_lat_long)