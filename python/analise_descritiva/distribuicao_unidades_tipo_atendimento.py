# Distribuição de unidades por tipo de atendimento

import pandas as pd

def analisar_distribuicao_tipo_atendimento(data: pd.DataFrame):
  atend_ambulatorial_counts = data['ST_ATEND_AMBULATORIAL'].value_counts()
  
  servico_apoio_counts = data['ST_SERVICO_APOIO'].value_counts()
  
  print(atend_ambulatorial_counts)
  print(servico_apoio_counts)