import pandas as pd
import plotly.express as px
from datetime import datetime

# Carregar os dados do arquivo Excel
darq = 'simulacao_paradas_refinaria.xlsx'
unidades = pd.read_excel(darq, sheet_name='Unidades_Producao')
historico_producao = pd.read_excel(darq, sheet_name='Historico_Producao')
paradas = pd.read_excel(darq, sheet_name='Paradas')
custos = pd.read_excel(darq, sheet_name='Custos_Operacionais')
eventos_manutencao = pd.read_excel(darq, sheet_name='Eventos_Manutencao')

# Converter colunas de datas
historico_producao['data'] = pd.to_datetime(historico_producao['data'])
paradas['data_inicio'] = pd.to_datetime(paradas['data_inicio'])
paradas['data_fim'] = pd.to_datetime(paradas['data_fim'])

# Criar um dataframe para armazenar a produção ajustada
producao_simulada = historico_producao.copy()

# Produção esperada (sem paradas)
producao_simulada['producao_esperada_bpd'] = producao_simulada['producao_real_bpd']

# Aplicar impacto das paradas programadas e não programadas
for _, parada in paradas.iterrows():
    mask = (producao_simulada['unidade_id'] == parada['unidade_id']) & \
           (producao_simulada['data'] >= parada['data_inicio']) & \
           (producao_simulada['data'] <= parada['data_fim'])
    
    producao_simulada.loc[mask, 'producao_real_bpd'] -= parada['impacto_estimado_bpd']
    producao_simulada['producao_real_bpd'] = producao_simulada['producao_real_bpd'].clip(lower=0)  # Evitar valores negativos

# Calcular a perda financeira
preco_barril_usd = 74  # Preço do barril de petróleo (ajuste conforme necessário)
producao_simulada['perda_financeira_usd'] = (producao_simulada['producao_esperada_bpd'] - producao_simulada['producao_real_bpd']) * preco_barril_usd

# Verifique se a coluna foi criada corretamente
print(producao_simulada[['data', 'perda_financeira_usd']])

# Reformar os dados com melt para criar uma coluna de tipo de produção
producao_simulada_melted = producao_simulada.melt(id_vars=['data', 'unidade_id'], 
                                                  value_vars=['producao_esperada_bpd', 'producao_real_bpd'],
                                                  var_name='producao_tipo', 
                                                  value_name='producao_bpd')

# Visualizar impacto com Plotly
grafico = px.line(
    producao_simulada_melted,
    x='data',
    y='producao_bpd',
    color='producao_tipo',
    line_group='unidade_id',
    title='Impacto das Paradas na Produção de Petróleo',
    labels={'producao_bpd': 'Produção (bpd)', 'data': 'Data', 'unidade_id': 'Unidade', 'producao_tipo': 'Tipo de Produção'}
)


# Identificar as datas de início e fim das paradas e os valores de produção esperada correspondentes
datas_paradas_inicio = []
producoes_esperadas_inicio = []
datas_paradas_fim = []
producoes_esperadas_fim = []

for _, parada in paradas.iterrows():
    unidade_id = parada['unidade_id']
    data_inicio = parada['data_inicio']
    data_fim = parada['data_fim']
    
    # Encontrar o valor de produção esperado da unidade na data de início da parada
    producao_esperada_inicio = producao_simulada.loc[
        (producao_simulada['unidade_id'] == unidade_id) & 
        (producao_simulada['data'] == data_inicio), 
        'producao_esperada_bpd'
    ].values[0]
    
    # Encontrar o valor de produção esperado da unidade na data de fim da parada
    producao_esperada_fim = producao_simulada.loc[
        (producao_simulada['unidade_id'] == unidade_id) & 
        (producao_simulada['data'] == data_fim), 
        'producao_esperada_bpd'
    ].values[0]
    
    # Armazenar as datas e os valores de produção
    datas_paradas_inicio.append(data_inicio)
    producoes_esperadas_inicio.append(producao_esperada_inicio)
    
    datas_paradas_fim.append(data_fim)
    producoes_esperadas_fim.append(producao_esperada_fim)

# Adicionar pontos nas datas de início e fim para cada parada com o valor de produção esperado
grafico.add_scatter(
    x=datas_paradas_inicio + datas_paradas_fim,  # Início e fim das paradas
    y=producoes_esperadas_inicio + producoes_esperadas_fim,  # Produção esperada nas datas de início e fim
    mode='markers',
    name='Paradas',
    marker=dict(color='red', size=7)
)

grafico.show()

# Visualizar perdas financeiras
grafico_perdas = px.bar(
    producao_simulada.groupby('data')[['perda_financeira_usd']].sum().reset_index(),
    x='data',
    y='perda_financeira_usd',
    title='Perdas Financeiras por Dia devido às Paradas',
    labels={'perda_financeira_usd': 'Perda (USD)', 'data': 'Data'}
)
grafico_perdas.show()
