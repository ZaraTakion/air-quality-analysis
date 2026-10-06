# Etapa 4 — Modelagem explicativa

## Pergunta e escopo

O notebook [`04_modelagem_explicativa.ipynb`](../notebooks/04_modelagem_explicativa.ipynb) testa se variáveis meteorológicas e a época do ano ajudam a estimar o `Pollution_Index` disponível neste conjunto. Ele **não** usa concentrações de poluentes como preditores. O conjunto processado lido pelo notebook tem 5.203 observações.

## Variáveis realmente usadas

- **Alvo (`y`):** `Pollution_Index`.
- **Preditores (`X`):** `Temperature`, `Humidity`, `Wind Speed` e `Month`.
- `Month` é expandido com `pd.get_dummies(..., drop_first=True)`: janeiro é a categoria de referência e os outros 11 meses entram como indicadores.
- O código não padroniza as variáveis, não inclui cidade/país como preditores e não usa `PM2.5`, `PM10`, `NO2`, `SO2`, `CO` ou `O3` em `X`.

O alvo foi criado no notebook de limpeza como a média aritmética simples dos seis campos de poluentes: `PM2.5`, `PM10`, `NO2`, `SO2`, `CO` e `O3`. Essa composição e a ressalva sobre unidades estão descritas no [dicionário de dados](data_dictionary.md). O `Pollution_Index` é, portanto, um alvo composto deste projeto, não um índice oficial de qualidade do ar.

## Regressão linear (OLS)

O notebook ajusta `statsmodels.OLS` com intercepto a todas as 5.203 observações; **não** aplica uma divisão treino/teste para esse ajuste. Resultados registrados:

| Resultado | Valor | Leitura correta |
|---|---:|---|
| R² | 0,002 | O ajuste explica uma fração muito pequena da variação observada nesta amostra. |
| R² ajustado | −0,001 | A pequena melhora de ajuste não compensa a quantidade de preditores incluídos. |
| F-statistic | 0,598 | Teste conjunto dos coeficientes dos preditores. |
| Prob (F-statistic) | 0,869 | Sem evidência de associação linear conjunta no nível de 5%. |
| Temperatura: coeficiente / p-value | −0,0120 / 0,429 | Sinal negativo estimado, sem significância estatística a 5%. |
| Umidade: coeficiente / p-value | +0,0107 / 0,207 | Sinal positivo estimado, sem significância estatística a 5%. |
| Vento: coeficiente / p-value | −0,0272 / 0,484 | Sinal negativo estimado, sem significância estatística a 5%. |

Nenhum dos três coeficientes meteorológicos é estatisticamente significativo a 5%. Os sinais estimados, isoladamente, não permitem afirmar que calor ou vento dispersam poluentes nem que umidade os mantém suspensos. Os coeficientes dos meses também não têm p-value abaixo de 0,05 no resumo salvo no notebook.

## Random Forest

O mesmo notebook separa aleatoriamente 20% dos dados para teste com `train_test_split(test_size=0.2, random_state=42)` e ajusta `RandomForestRegressor(n_estimators=200, random_state=42)` usando os quatro preditores (após a expansão de `Month`). Resultados registrados no output salvo:

| Métrica no conjunto de teste | Resultado |
|---|---:|
| R² | −0,082 |
| RMSE | 16,519 |

Um R² de teste negativo indica que, nessa divisão, o modelo teve desempenho inferior ao preditor de referência que sempre usaria a média do alvo do conjunto de teste. O RMSE deve ser lido na escala do `Pollution_Index`, cuja composição tem limitações de unidade. O notebook não registra busca de hiperparâmetros nem validação cruzada para este modelo de quatro preditores.

## Não confundir com o notebook 06

O notebook [`06_validation_and_storytelling.ipynb`](../notebooks/06_validation_and_storytelling.ipynb) roda outro experimento, não uma validação do modelo da etapa 4. Ele usa nove preditores: `Temperature`, `Humidity`, `Wind Speed` e os seis poluentes que entram diretamente na fórmula do alvo. Com `KFold(n_splits=5, shuffle=True, random_state=42)`, registra R² por fold entre 0,972 e 0,977, média 0,974 e desvio-padrão 0,002.

Como `PM2.5`, `PM10`, `NO2`, `SO2`, `CO` e `O3` fazem parte do cálculo de `Pollution_Index`, fornecê-los ao modelo revela diretamente os componentes do alvo. Isso é vazamento de alvo: esses escores não medem previsão independente e não podem ser comparados com o teste da etapa 4 nem apresentados como evidência de generalização. A importância de variáveis desse experimento também não demonstra influência causal e pode refletir a dependência matemática entre os preditores e o alvo.

## Limites e interpretação

- O OLS usa toda a amostra e descreve associações lineares ajustadas; não é uma avaliação fora da amostra.
- A divisão aleatória do Random Forest não separa cidades nem períodos. Registros relacionados podem aparecer no treino e no teste; o resultado não mede generalização para uma cidade ou período novo.
- O conjunto cobre um único ano e não contém variáveis de cidade como preditores nesse notebook.
- O alvo é uma média simples de concentrações que o dicionário documenta em unidades diferentes. Até corrigir ou justificar a harmonização dessas unidades, ele não deve ser interpretado como medida física ou sanitária padronizada.
- Os resultados não demonstram causalidade e não sustentam recomendações ambientais ou políticas públicas.

## Próxima validação necessária

Antes de apresentar uma alegação preditiva, defina um alvo com unidade e interpretação coerentes. Em seguida, avalie primeiro um baseline e compare modelos sem incluir no conjunto de preditores componentes usados para construir o alvo. Separe treino e teste por cidade ou período conforme a pergunta de generalização e informe as métricas no teste. Para inferir efeitos meteorológicos, explicite controles e desenho apropriado; os modelos atuais não fazem essa inferência.
