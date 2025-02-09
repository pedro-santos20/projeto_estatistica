# Teste de hipótese: Existe uma diferença significativa entre as unidades públicas e privadas em relação ao número de leitos disponíveis?

import scipy.stats as stats
import pandas as pd

def diferenca_unidade_publica_privada_leitos(data: pd.DataFrame):
  publico_data = data[data['TP_GESTAO'] == 'Pública']['CO_NIVEL_HIERARQUIA'] 
  privado_data = data[data['TP_GESTAO'] == 'Privada']['CO_NIVEL_HIERARQUIA']
  
  t_stat, p_value = stats.ttest_ind(publico_data.dropna(), privado_data.dropna())
  
  print(f'T-statistic: {t_stat}')
  print(f'P-value: {p_value}')