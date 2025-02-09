# Distribuição das unidades de saúde por estado
 
import pandas as pd

def analisar_distribuicao_unidade(data: pd.DataFrame):
  estado_counts = data['CO_UF'].value_counts()
  
  texto = (
		"A análise da distribuição das unidades de saúde por estado "
		"revela o número de unidades registradas em cada estado. "
		"Os estados com maior número de unidades podem indicar maior oferta "
		"de serviços ou maior concentração populacional."
	)
  
  return texto, estado_counts 