import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('cnes_estabelecimentos.csv', sep=';', encoding='ISO-8859-1', low_memory=False)

def grafico_distribuicao_unidades_estado(data):
  plt.figure(figsize=(12, 6))
  data['CO_UF'].value_counts().sort_index().plot(kind='bar', color='steelblue')
  plt.xlabel('Estado (UF)')
  plt.ylabel('Número de estabelecimentos')
  plt.title('Distribuição de estabelecimentos por estado')
  plt.xticks(rotation=90)
  plt.savefig('graficos/distribuicao_unidades_estado.png')
  plt.close()

def grafico_tipo_gestao(data):
    plt.figure(figsize=(8, 6))
    data['TP_GESTAO'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=["skyblue", "orange", "green"], startangle=90)
    plt.title("Distribuição dos Tipos de Gestão")
    plt.ylabel("")
    plt.savefig("graficos/distribuicao_tipo_gestao.png")
    plt.close()

def grafico_natureza_juridica(data):
    plt.figure(figsize=(12, 6))
    data['CO_NATUREZA_JUR'].value_counts().nlargest(10).plot(kind='bar', color='purple')
    plt.xlabel("Natureza Jurídica")
    plt.ylabel("Quantidade de Estabelecimentos")
    plt.title("Top 10 Naturezas Jurídicas mais comuns")
    plt.xticks(rotation=90)
    plt.savefig("graficos/distribuicao_natureza_juridica.png")
    plt.close()

def boxplot_turnos_atendimento(data):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="DS_TURNO_ATENDIMENTO", y="CO_UF", hue="DS_TURNO_ATENDIMENTO", data=data, palette="Set2", legend=False)
    plt.xticks(rotation=45)
    plt.xlabel("Turno de Atendimento")
    plt.ylabel("Código UF (Estado)")
    plt.title("Distribuição das Unidades de Saúde por Turno de Atendimento")
    plt.savefig("graficos/bloxpot_turnos_atendimento.png")
    plt.show()

def boxplot_servico_apoio_por_gestao(data):
    plt.figure(figsize=(8, 6))

    sns.boxplot(x=data["TP_GESTAO"], y=data["ST_SERVICO_APOIO"], palette="Set2")

    plt.xlabel("Tipo de Gestão")
    plt.ylabel("Presença de Serviço de Apoio (0 = Não, 1 = Sim)")
    plt.title("Distribuição da Presença de Serviços de Apoio por Tipo de Gestão")
    plt.savefig("graficos/servico_apoio_por_gestao.png")
    plt.show()
    
def grafico_distribuicao_tipo_atendimento(data: pd.DataFrame):
    atend_ambulatorial_counts = data['ST_ATEND_AMBULATORIAL'].value_counts()
    servico_apoio_counts = data['ST_SERVICO_APOIO'].value_counts()

    df_plot = pd.DataFrame({
        "Tipo de Atendimento": ["Ambulatorial"] * len(atend_ambulatorial_counts) + ["Serviço de Apoio"] * len(servico_apoio_counts),
        "Status": atend_ambulatorial_counts.index.tolist() + servico_apoio_counts.index.tolist(),
        "Quantidade": atend_ambulatorial_counts.tolist() + servico_apoio_counts.tolist()
    })

    plt.figure(figsize=(8, 5))
    sns.barplot(x="Tipo de Atendimento", y="Quantidade", hue="Status", data=df_plot, palette="Set2")

    plt.xlabel("Tipo de Atendimento")
    plt.ylabel("Quantidade de Unidades")
    plt.title("Distribuição de Unidades por Tipo de Atendimento")
    plt.legend(title="Status", labels=["Não possui", "Possui"])
    
    plt.savefig("graficos/distribuicao_tipo_atendimento.png", bbox_inches='tight')
    plt.close()

def gerar_todos_graficos(data):
    grafico_distribuicao_unidades_estado(data)
    grafico_tipo_gestao(data)
    grafico_natureza_juridica(data)
    boxplot_turnos_atendimento(data)
    boxplot_servico_apoio_por_gestao(data)
    grafico_distribuicao_tipo_atendimento(data)
    print("Todos os gráficos foram gerados com sucesso!")

import os
if not os.path.exists("graficos"):
    os.makedirs("graficos")

gerar_todos_graficos(data)