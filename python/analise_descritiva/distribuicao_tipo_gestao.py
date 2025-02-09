# Distribuição dos tipos de gestão

import pandas as pd

def analisar_distribuicao_tipo_gestao(data: pd.DataFrame):
  gestao_counts = data['TP_GESTAO'].value_counts()
  
  print(gestao_counts)