import pandas as pd
from pandasgui import show
from python.analise_descritiva.distribuicao_unidades_estado import analisar_distribuicao_unidade
from python.analise_descritiva.distribuicao_tipo_gestao import analisar_distribuicao_tipo_gestao
from python.analise_descritiva.distribuicao_unidades_juridica import analisar_distribuicao_juridica
from python.analise_descritiva.correlacao_latitute_longitude_unidades import correlacao_lat_long
from python.analise_descritiva.media_estabelecimentos_servicos_especificos import media_servicos_especificos
from python.analise_descritiva.distribuicao_unidades_tipo_atendimento import analisar_distribuicao_tipo_atendimento 


 
file_path = 'cnes_estabelecimentos.csv'

data = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', low_memory=False)
print(data.head())
print(data.columns)

gui = show(data)

analisar_distribuicao_unidade(data)
analisar_distribuicao_tipo_gestao(data)
analisar_distribuicao_tipo_atendimento(data)
analisar_distribuicao_juridica(data)
media_servicos_especificos(data)
correlacao_lat_long(data)
