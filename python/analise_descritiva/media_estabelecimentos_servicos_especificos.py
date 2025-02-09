# Média de estabelecimentos com serviços específicos

import pandas as pd

def media_servicos_especificos(data: pd.DataFrame):
  media_cirurgico = data['ST_CENTRO_CIRURGICO'].mean()
  
  media_obstetrico = data['ST_CENTRO_OBSTETRICO'].mean()
  
  media_neonatal = data['ST_CENTRO_NEONATAL'].mean()
  
  media_hospitalar = data['ST_ATEND_HOSPITALAR'].mean()
  
  print(f'Média de unidades com centro cirúrgico: {media_cirurgico:.2f}')
  print(f'Média de unidades com centro obstétrico: {media_obstetrico:.2f}')
  print(f'Média de unidades com centro neonatal: {media_neonatal:.2f}')
  print(f'Média de unidades com centro hospitalar: {media_hospitalar:.2f}')