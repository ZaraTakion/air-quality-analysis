# Dashboard interativo — Air Quality Analysis

## Objetivo e dados

O app em [`app/dashboard_air_quality.py`](../app/dashboard_air_quality.py) é um painel exploratório de uma cidade por vez, usando `data/processed/air_quality_clean.csv`. O código converte `Date` para data, deriva o mês e recalcula o índice pela média aritmética de `PM2.5`, `PM10`, `NO2`, `SO2`, `CO` e `O3`. O índice é uma composição específica deste projeto, não um índice oficial; veja [`data_dictionary.md`](data_dictionary.md).

## Controles e indicadores

O único controle do layout é um seletor de cidade, inicialmente “Tokyo”. O painel não possui seletor de intervalo de datas, filtro de poluente ou comparação de cidades.

| Componente | Cálculo apresentado |
|---|---|
| Índice Médio | Média do `Índice de Poluição` nas linhas da cidade selecionada. |
| Mês Mais Crítico | Mês com a maior média mensal do índice naquela cidade. |
| Menor PM2.5 | Menor valor de `PM2.5` encontrado nas linhas da cidade. |
| Tendência Mensal | Média mensal do índice por mês do ano para a cidade selecionada. |
| Relação Clima × Poluição | Dispersão de `Temperature` versus índice; cor representa `Humidity` e tamanho representa `Wind Speed`. |
| Distribuição dos Poluentes | Boxplots de `PM2.5`, `PM10`, `NO2`, `SO2`, `CO` e `O3` para a cidade selecionada. |

As visualizações são descritivas. Um padrão visual não estabelece que as variáveis meteorológicas causem mudanças no índice; os resultados da etapa de modelagem também não sustentam essa conclusão atualmente.

## Executar localmente

Execute a partir da raiz do repositório, pois o caminho do CSV no código é relativo à raiz:

```bash
python -m pip install -r requirements.txt
python app/dashboard_air_quality.py
```

Abra `http://127.0.0.1:8050/`.

## Limites conhecidos na documentação e interface

O dashboard rotula a velocidade do vento como km/h no gráfico de dispersão, enquanto o dicionário atual descreve `Wind Speed` em m/s. A unidade precisa ser confirmada na fonte antes de alterar esse rótulo. O app também recalcula `Índice de Poluição`, embora a coluna `Pollution_Index` já esteja no CSV processado; as duas fórmulas são atualmente iguais no código. Confirme a definição e as unidades antes de interpretar esse índice.
