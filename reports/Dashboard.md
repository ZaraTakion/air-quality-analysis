# 📊 Dashboard Interativo — Air Quality Analysis

## 🎯 Objetivo

O dashboard foi desenvolvido para **visualizar e comunicar insights ambientais** de forma dinâmica e acessível.
Ele integra dados de qualidade do ar e variáveis meteorológicas, permitindo identificar padrões e anomalias entre diferentes cidades e períodos.

---

## 🧩 Estrutura e Funcionalidades

### 1️⃣ **Visão Geral**

* Mostra **índices médios de poluição por cidade** com base no `Pollution_Index`.
* Permite **comparar variáveis ambientais** (Temperatura, Umidade, Velocidade do Vento) e poluentes (PM2.5, PM10, NO₂, SO₂, CO, O₃).
* Oferece filtros por cidade e período para análises segmentadas.

### 2️⃣ **Componentes Interativos**

| Componente             | Função                                            |
| ---------------------- | ------------------------------------------------- |
| **Dropdowns**          | Selecionar cidade ou variável a analisar          |
| **Gráficos de Linha**  | Exibir tendência temporal dos índices de poluição |
| **Gráficos de Barras** | Comparar médias entre diferentes cidades          |
| **Mapa (opcional)**    | Visualizar dispersão geográfica de poluentes      |
| **Cards Numéricos**    | Mostrar KPIs como média de CO₂ e PM2.5            |

### 3️⃣ **Tecnologias Utilizadas**

* **Dash (Plotly)** — base do dashboard interativo
* **Pandas** — manipulação dos dados
* **Plotly Express** — geração dos gráficos
* **Bootstrap CSS** — layout responsivo e limpo

---

## 🧠 Storytelling e Interpretação

O dashboard foi projetado com foco em **narrativa de dados (data storytelling)**:

* Cada visualização responde a uma pergunta específica:

  * *Quais cidades apresentam maior poluição média?*
  * *Como temperatura e umidade afetam os níveis de partículas finas?*
  * *Quais meses concentram picos de poluição?*
* A combinação de **cores e interatividade** facilita a interpretação de tendências sem sobrecarregar o usuário.

---

## 🧱 Arquitetura do Código

Localização: `app/dashboard_air_quality.py`

Principais blocos:

```python
# Importações e configuração
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Leitura do dataset processado
df = pd.read_csv("../data/processed/air_quality_clean.csv")

# Layout principal
app.layout = html.Div([
    html.H1("Air Quality Dashboard"),
    dcc.Dropdown(id="city", options=[...], value="São Paulo"),
    dcc.Graph(id="pollution_trend"),
])
```

---

## ⚙️ Deploy e Execução

### Local

```bash
cd app
python dashboard_air_quality.py
```

Acesse: [http://127.0.0.1:8050](http://127.0.0.1:8050)

### Cloud (opcional)

* **Render / Railway / Vercel** — pode hospedar o app gratuitamente.
* Configure o `Procfile`:

  ```
  web: python app/dashboard_air_quality.py
  ```

---

## 📈 Benefícios do Dashboard

* Interface acessível para não-especialistas.
* Atualizável conforme novos dados são adicionados.
* Suporte à tomada de decisão por **órgãos ambientais** e **instituições de pesquisa**.

---

## 🧭 Conclusão

O dashboard se consolidou como a camada de **comunicação visual e interpretativa** do projeto, permitindo transformar análises técnicas em **insights acionáveis e compreensíveis**.
Ele reforça o papel da visualização de dados como ponte entre ciência, políticas públicas e o público geral.

---
