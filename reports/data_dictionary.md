# Dicionário de dados — Air Quality Analysis

## Arquivos e dimensões observadas

- **Entrada do notebook de limpeza:** 10.000 linhas e 12 colunas, conforme o output salvo do notebook 02.
- **Duplicatas removidas:** 4.797, pela combinação `City`, `Country` e `Date`.
- **Arquivo processado carregado pelo notebook 03:** 5.203 linhas e 16 colunas.
- **Período observado:** 2023, um único ano.
- **Granularidade registrada:** observação associada a cidade e data; a documentação não deve presumir cobertura diária completa.
- **Fonte indicada pelo projeto:** Global Air Quality Dataset (Kaggle, 2023). Consulte os metadados originais para confirmar a proveniência e as unidades.

O filtro IQR também é aplicado às nove variáveis numéricas no notebook 02. O notebook não imprime uma contagem separada de linhas removidas por esse filtro; portanto, este dicionário não atribui uma quantidade a essa etapa.

## Colunas de entrada

| Coluna | Tipo lógico | Unidade documentada no projeto | Descrição |
|---|---|---|---|
| `City` | texto | — | Cidade associada à observação. |
| `Country` | texto | — | País associado à cidade. |
| `Date` | data | AAAA-MM-DD | Data da observação. |
| `PM2.5` | numérico | µg/m³* | Concentração de partículas finas. |
| `PM10` | numérico | µg/m³* | Concentração de partículas inaláveis. |
| `NO2` | numérico | µg/m³* | Dióxido de nitrogênio. |
| `SO2` | numérico | µg/m³* | Dióxido de enxofre. |
| `CO` | numérico | mg/m³* | Monóxido de carbono. |
| `O3` | numérico | µg/m³* | Ozônio. |
| `Temperature` | numérico | °C* | Temperatura. |
| `Humidity` | numérico | %* | Umidade relativa. |
| `Wind Speed` | numérico | m/s* | Velocidade do vento conforme o dicionário anterior; confirme na fonte. |

\* Unidades herdadas da documentação anterior do projeto; ainda precisam ser verificadas nos metadados da fonte. O dashboard, por exemplo, rotula `Wind Speed` em km/h, divergindo deste dicionário.

## Colunas derivadas no notebook de limpeza

| Coluna | Cálculo no código | Observação |
|---|---|---|
| `Year` | Ano extraído de `Date` | No recorte processado observado, os registros são de 2023. |
| `Month` | Mês numérico (1–12) extraído de `Date` | Usado como variável categórica expandida em indicadores no notebook 04. |
| `Pollution_Index` | Média aritmética simples de `PM2.5`, `PM10`, `NO2`, `SO2`, `CO` e `O3` por linha | Não é média ponderada nem índice oficial de qualidade do ar. |
| `Temp_Bin` | `pd.cut(Temperature, [-15, 0, 10, 20, 30, 45])` | Faixas fixas: Muito Frio, Frio, Ameno, Quente e Muito Quente; não são quantis. |

## Limitação do `Pollution_Index`

O código calcula uma média direta dos seis números. A documentação anterior atribui CO em mg/m³ e os demais poluentes em µg/m³; se essas unidades estiverem corretas, a média agrega grandezas em escalas diferentes sem conversão ou padronização. Assim, `Pollution_Index` deve ser descrito apenas como um **alvo composto aritmético específico do projeto**, sem interpretação como concentração física comum, AQI oficial ou medida de risco à saúde. Confirme as unidades da fonte e redefina ou justifique a construção antes de apresentar interpretações substantivas.

## Relação com os notebooks

- O notebook 04 usa como preditores somente `Temperature`, `Humidity`, `Wind Speed` e `Month`; `Pollution_Index` é o alvo.
- O notebook 06 também usa os seis campos de poluentes como preditores, embora eles componham o próprio alvo. O alto R² salvo nesse experimento está sujeito a vazamento de alvo e não representa validação independente. Veja [`Modelagem.md`](Modelagem.md).
