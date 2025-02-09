# Distribuição das unidades de saúde por natureza jurídica

import pandas as pd

def analisar_distribuicao_juridica(data: pd.DataFrame):
  natureza_counts = data['CO_NATUREZA_JUR'].value_counts()
  
  print(natureza_counts)
