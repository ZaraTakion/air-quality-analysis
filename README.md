# Air Quality Analysis

Projeto exploratório de qualidade do ar com limpeza de dados, análises em notebooks, um dashboard em Dash e relatórios técnicos. O conjunto incluído é um recorte estático de 2023; o dashboard não consulta uma API nem atualiza os dados automaticamente.

## Conteúdo do repositório

```text
data/
  interim/air_quality_overview.csv
  processed/air_quality_clean.csv
notebooks/
  01_data_overview.ipynb
  02_data_cleaning.ipynb
  03_eda.ipynb
  04_modelagem_explicativa.ipynb
  06_validation_and_storytelling.ipynb
app/dashboard_air_quality.py
reports/
  Conclusao.md
  Dashboard.md
  Modelagem.md
  data_dictionary.md
```

O notebook 02 registra 10.000 linhas na entrada e remove 4.797 duplicatas pela chave cidade, país e data. A base processada carregada pelo notebook 03 tem 5.203 linhas e 16 colunas. A limpeza também aplica um filtro IQR às nove variáveis numéricas de poluição e meteorologia, cria `Year`, `Month`, `Pollution_Index` e `Temp_Bin`, e salva o CSV processado.

## Dashboard

O dashboard filtra uma cidade por vez. Exibe o índice médio do recorte, o mês com maior média do índice, o menor PM2.5, a tendência mensal do índice, um gráfico de temperatura versus índice e distribuições dos seis poluentes. Ele não oferece filtro de período, mapa nem comparação simultânea entre cidades. O índice é uma média aritmética dos valores de seis poluentes, não um índice oficial de qualidade do ar; veja as limitações em [`reports/data_dictionary.md`](reports/data_dictionary.md).

Execute da raiz do repositório:

```bash
python -m pip install -r requirements.txt
python app/dashboard_air_quality.py
```

Acesse `http://127.0.0.1:8050/`.

## O que a modelagem permite concluir

A etapa 4 modela `Pollution_Index` usando apenas `Temperature`, `Humidity`, `Wind Speed` e `Month`; o mês é convertido em variáveis indicadoras. O OLS registrado tem R² de 0,002 e não encontra coeficientes meteorológicos estatisticamente significativos a 5%. No teste aleatório de 20% da etapa 4, o Random Forest tem R² de −0,082 e RMSE de 16,519. Esses resultados não sustentam afirmações de que temperatura, umidade ou vento reduzem ou aumentam a poluição.

O notebook 06 usa um experimento diferente: inclui como preditores os seis poluentes que compõem diretamente o alvo. O R² médio registrado de 0,974 sofre vazamento de alvo e não deve ser apresentado como evidência de capacidade preditiva nem como validação independente. Detalhes e próximos passos estão em [`reports/Modelagem.md`](reports/Modelagem.md) e [`reports/Conclusao.md`](reports/Conclusao.md).

## Tecnologias

Python, Pandas, NumPy, scikit-learn, statsmodels, Matplotlib, Seaborn, Plotly e Dash.

## Autoria

Zara Takion · [GitHub](https://github.com/ZaraTakion)

## Licença e dados

Este repositório não contém um arquivo `LICENSE`; portanto, não declara uma licença de software. Consulte também os termos e a licença da fonte original dos dados antes de redistribuí-los.
