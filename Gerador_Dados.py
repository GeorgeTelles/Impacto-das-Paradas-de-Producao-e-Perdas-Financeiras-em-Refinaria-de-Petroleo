import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Criando dados para Unidades de Produção
unidades = pd.DataFrame({
    'unidade_id': [1, 2, 3],
    'nome_unidade': ['Refinaria de Paulínia', 'Refinaria de Duque de Caxias', 'Refinaria de Capuava'],
    'capacidade_diaria_bpd': [200000, 150000, 100000],
    'eficiencia_atual': [0.95, 0.92, 0.90],
    'status_operacional': ['Operacional', 'Operacional', 'Operacional'],
    'data_instalacao': ['2005-07-12', '2010-05-20', '2015-08-15']
})

# Criando dados para Histórico de Produção
datas = pd.date_range(start='2024-01-01', periods=250, freq='D')
producoes = []
for data in datas:
    for i, row in unidades.iterrows():
        producao_real = row['capacidade_diaria_bpd'] * row['eficiencia_atual'] * np.random.uniform(0.95, 1.05)
        producoes.append([data.date(), row['unidade_id'], int(producao_real)])

historico_producao = pd.DataFrame(producoes, columns=['data', 'unidade_id', 'producao_real_bpd'])

# Criando dados para Paradas Programadas e Não Programadas
paradas = pd.DataFrame({
    'parada_id': [1, 2, 3, 4],
    'unidade_id': [1, 2, 1, 3],
    'tipo_parada': ['Programada', 'Não Programada', 'Programada', 'Não Programada'],
    'data_inicio': ['2024-03-10', '2024-02-20', '2024-04-05', '2024-02-25'],
    'data_fim': ['2024-03-15', '2024-02-22', '2024-04-10', '2024-02-27'],
    'motivo': ['Manutenção preventiva', 'Falha mecânica', 'Inspeção obrigatória', 'Falha elétrica'],
    'impacto_estimado_bpd': [20000, 50000, 15000, 30000]
})

# Criando dados para Custos Operacionais e Perdas
custos = pd.DataFrame({
    'custo_id': [1, 2, 3, 4],
    'unidade_id': [1, 2, 3, 1],
    'tipo_custo': ['Manutenção', 'Perda de Produção', 'Reparo emergencial', 'Perda de Produção'],
    'data': ['2024-03-10', '2024-02-20', '2024-02-25', '2024-04-05'],
    'valor_usd': [150000, 500000, 80000, 300000]
})

# Criando dados para Eventos de Manutenção
eventos_manutencao = pd.DataFrame({
    'evento_id': [1, 2, 3, 4],
    'unidade_id': [1, 2, 3, 1],
    'tipo_manutencao': ['Preventiva', 'Corretiva', 'Emergencial', 'Preventiva'],
    'data_planejada': ['2024-03-10', '2024-02-20', '2024-02-25', '2024-04-05'],
    'duração_dias': [5, 2, 3, 6],
    'status': ['Confirmado', 'Executado', 'Executado', 'Planejado']
})

with pd.ExcelWriter('simulacao_paradas_refinaria.xlsx', engine='openpyxl') as writer:
    unidades.to_excel(writer, sheet_name='Unidades_Producao', index=False)
    historico_producao.to_excel(writer, sheet_name='Historico_Producao', index=False)
    paradas.to_excel(writer, sheet_name='Paradas', index=False)
    custos.to_excel(writer, sheet_name='Custos_Operacionais', index=False)
    eventos_manutencao.to_excel(writer, sheet_name='Eventos_Manutencao', index=False)

print("Arquivo Excel criado com sucesso: simulacao_paradas_refinaria.xlsx")
