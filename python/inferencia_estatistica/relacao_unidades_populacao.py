# Análise de Correlação: Relação entre o número de unidades de saúde e a população do estado

import pandas as pd

def relacao_unidades_populacao(data: pd.DataFrame):
  populacao_estados = {
		'SP': 45000000,
    'RJ': 17000000,
    'MG': 21000000,
    'BA': 15000000,
    'PR': 11000000,
	}
  
  data['populacao'] = data['CO_UF'].map(populacao_estados)
  
  correlacao_populacao = data.groupby('CO_UF').size().corr(data.groupby('CO_UF')['populacao'].mean())
  
  print(f'Correlação entre número de unidades e população por estado: {correlacao_populacao:.2f}')