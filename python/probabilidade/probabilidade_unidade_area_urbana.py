# Análise de Probabilidade: Qual a probabilidade de uma unidade de saúde estar localizada em uma área urbana?

import pandas as pd

def probabilidade_area_urbana(data: pd.DataFrame):
  data['area_urbana'] = (data['NU_LATITUDE'] > -30) & (data['NU_LONGITUDE'] > -50)
  
  probabilidade_urbana = data['area_urbana'].mean()
  
  print(f'Probabilidade de a unidade estar em área urbana: {probabilidade_urbana:.2f}')