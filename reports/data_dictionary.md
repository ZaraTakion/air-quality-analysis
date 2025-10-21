---

# 📘 Data Dictionary — Air Quality Analysis

## 🎯 Objetivo

O dicionário de dados define o significado, tipo e unidade de medida de cada coluna presente no dataset utilizado na análise de qualidade do ar.
Essas informações garantem **clareza, rastreabilidade e consistência** ao longo de todo o pipeline de ciência de dados.

---

## 🧱 Estrutura do Dataset

* **Nome do arquivo:** `air_quality_clean.csv`
* **Origem dos dados:** *Global Air Quality Dataset (Kaggle, 2023)*
* **Dimensões:** 10.000 linhas × 12 colunas originais (17 após engenharia de atributos)
* **Período de coleta:** janeiro a dezembro de 2023
* **Nível de granularidade:** leituras diárias por cidade

---

## 📋 Dicionário de Variáveis Principais

| Coluna        | Tipo       | Unidade    | Descrição                                                                      |
| ------------- | ---------- | ---------- | ------------------------------------------------------------------------------ |
| `City`        | *object*   | —          | Nome da cidade onde os dados foram coletados.                                  |
| `Country`     | *object*   | —          | País correspondente à cidade.                                                  |
| `Date`        | *datetime* | AAAA-MM-DD | Data da observação.                                                            |
| `PM2.5`       | *float64*  | µg/m³      | Concentração média diária de partículas finas menores que 2,5 micrômetros.     |
| `PM10`        | *float64*  | µg/m³      | Concentração média diária de partículas inaláveis menores que 10 micrômetros.  |
| `NO2`         | *float64*  | µg/m³      | Dióxido de nitrogênio, associado à combustão de veículos e indústrias.         |
| `SO2`         | *float64*  | µg/m³      | Dióxido de enxofre, proveniente da queima de combustíveis fósseis.             |
| `CO`          | *float64*  | mg/m³      | Monóxido de carbono, indicador de poluição veicular.                           |
| `O3`          | *float64*  | µg/m³      | Ozônio troposférico, formado por reações químicas entre poluentes e luz solar. |
| `Temperature` | *float64*  | °C         | Temperatura média diária.                                                      |
| `Humidity`    | *float64*  | %          | Umidade relativa do ar.                                                        |
| `Wind Speed`  | *float64*  | m/s        | Velocidade média do vento.                                                     |

---

## ⚙️ Variáveis Derivadas (Feature Engineering)

| Nova Coluna       | Tipo       | Descrição                                                                                                        |
| ----------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| `Year`            | *int64*    | Ano extraído da coluna `Date`.                                                                                   |
| `Month`           | *int64*    | Mês numérico (1 a 12) para análise sazonal.                                                                      |
| `Temp_Bin`        | *category* | Classificação categórica da temperatura: “Muito Frio”, “Frio”, “Ameno”, “Quente”, “Muito Quente”.                |
| `Pollution_Index` | *float64*  | Índice sintético criado pela média ponderada de poluentes primários (`PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `O3`). |

---

## 🧮 Fórmula do Índice de Poluição

[
Pollution_Index = \frac{PM2.5 + PM10 + NO2 + SO2 + CO + O3}{6}
]

Esse índice resume o nível geral de poluição do ar, padronizando diferentes gases e partículas em uma única métrica de referência comparável entre cidades.

---

## 🧰 Observações Técnicas

* Todos os valores foram **validados quanto a nulos, outliers e tipos de dados**.
* Não há valores ausentes (`NaN`) no dataset final.
* Unidades de medida foram **normalizadas** (µg/m³ e °C).
* As categorias de `Temp_Bin` foram criadas com base em **quantis de temperatura** para manter equilíbrio entre classes.

---

## 🧭 Conclusão

O dataset final oferece uma **visão padronizada e limpa da qualidade do ar global**, permitindo análises comparativas entre cidades e a modelagem dos efeitos climáticos sobre a poluição atmosférica.
O `Pollution_Index` se mostrou eficaz para representar o comportamento agregado dos poluentes.

---
