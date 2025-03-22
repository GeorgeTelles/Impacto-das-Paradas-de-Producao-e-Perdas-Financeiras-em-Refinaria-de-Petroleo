# Análise de Impacto das Paradas de Produção e Perdas Financeiras em Refinaria de Petróleo

Este projeto visa analisar o impacto das paradas programadas e não programadas nas unidades de produção de uma refinaria de petróleo. O objetivo é quantificar as perdas financeiras decorrentes das quedas na produção devido a essas paradas, utilizando dados históricos e estimativas de impacto.

## Objetivos principais do projeto:

### 1. Análise de Produção Ajustada
O projeto começa com o carregamento de dados de produção histórica, eventos de parada e custos operacionais, provenientes de um arquivo Excel. Ele realiza ajustes na produção real das unidades de refino, levando em consideração os impactos das paradas nas operações.

### 2. Simulação de Impacto nas Paradas
Para cada parada registrada, o código calcula a redução na produção de petróleo (em barris por dia - bpd) durante o período de inatividade das unidades afetadas. Essa simulação ajuda a modelar como a produção esperada é alterada com base nos eventos de parada, evitando valores negativos de produção.

### 3. Cálculo das Perdas Financeiras
Com base no preço do barril de petróleo (definido como $74 USD), o impacto financeiro das paradas é calculado, refletindo as perdas financeiras resultantes das quedas na produção. Isso permite estimar o custo para a refinaria devido às paradas, ajudando na tomada de decisões e planejamento de manutenção.

### 4. Visualização de Dados
O projeto gera duas visualizações principais:

- **Gráfico de Impacto nas Produções**: Utilizando o Plotly, o projeto exibe uma linha do tempo das produções esperadas e reais, destacando os impactos das paradas. O gráfico permite comparar a produção esperada e a real ao longo do tempo, com a inclusão de marcadores indicando as datas de início e fim das paradas.
  
- **Gráfico de Perdas Financeiras**: Um gráfico de barras é gerado para mostrar as perdas financeiras diárias acumuladas devido às paradas de produção. Ele permite uma visualização clara de quando as maiores perdas financeiras ocorreram, auxiliando na análise de eficiência operacional.

## Tecnologias Utilizadas:

- **Pandas**: Para manipulação e análise dos dados de produção, paradas e custos operacionais.
- **Plotly**: Para criação das visualizações interativas, que ajudam a entender o impacto das paradas nas produções e perdas financeiras.
- **Excel (pandas.read_excel)**: Para carregar dados de várias planilhas de um arquivo Excel.

## Benefícios do Projeto:

- **Planejamento de Manutenção**: O projeto fornece uma visão clara de como as paradas afetam a produção e as finanças da refinaria, permitindo um melhor planejamento e priorização de eventos de manutenção.
  
- **Tomada de Decisão Informada**: As perdas financeiras são quantificadas e visualizadas, ajudando os gestores a identificar áreas críticas para melhorar a eficiência da produção e reduzir custos operacionais.
  
- **Otimização da Produção**: A análise das paradas e o impacto financeiro associando as mudanças de produção podem orientar a refinaria a minimizar as paradas e a otimizar sua produção.

## Conclusão
Em resumo, este projeto oferece uma solução prática para analisar o impacto das paradas na produção de petróleo e nas finanças de uma refinaria, com o uso de ferramentas de análise de dados e visualização avançadas para apoiar decisões estratégicas de manutenção e operação.
