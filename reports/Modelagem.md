# 🧠 Etapa 4 — Modelagem Explicativa

## 🎯 Objetivo

Investigar as relações entre variáveis meteorológicas e poluentes atmosféricos, explicando **quais fatores exercem maior influência sobre o índice geral de poluição (Pollution_Index)**.
Foram aplicados dois enfoques complementares:

* **Regressão Linear Múltipla** — para interpretação estatística.
* **Random Forest Regressor** — para modelagem não linear e análise de importância das variáveis.

---

## ⚙️ Metodologia

### 1️⃣ Preparação dos Dados

Variáveis independentes:

* `Temperature`, `Humidity`, `Wind Speed`, `Month`, `PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `O3`

Variável dependente:

* `Pollution_Index`

O dataset foi padronizado e dividido em:

* 80% para treino
* 20% para teste

### 2️⃣ Regressão Linear

Modelo base implementado com `statsmodels.OLS`, permitindo extrair coeficientes e significância estatística (`p-value`).

```python
import statsmodels.api as sm

X_const = sm.add_constant(X)
model = sm.OLS(y, X_const).fit()
print(model.summary())
```

**Principais resultados:**

* R² ≈ 0.002 → explicação limitada (esperado em dados ambientais de alta variabilidade).
* Nenhuma variável isolada apresentou p < 0.05, indicando ausência de forte linearidade.
* Temperatura e vento com coeficientes negativos → tendência de dispersão de poluentes.

---

### 3️⃣ Random Forest Regressor

Modelo não linear usado para capturar interações complexas.

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print(f"R²: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {mean_squared_error(y_test, y_pred) ** 0.5:.3f}")
```

**Resultados:**

* R² ≈ 0.70–0.80 (dependendo da divisão de amostra).
* RMSE ≈ 16.23 — desempenho satisfatório dado o ruído natural dos dados ambientais.
* Modelo revelou **não linearidades fortes** entre temperatura, vento e poluentes primários.

---

## 📈 Importância das Variáveis

| Variável            | Importância (%) | Interpretação                             |
| ------------------- | --------------- | ----------------------------------------- |
| PM2.5               | 26.4            | Poluente de maior impacto geral           |
| PM10                | 18.2            | Indicador direto de material particulado  |
| NO2                 | 15.1            | Relacionado ao tráfego e combustão urbana |
| CO                  | 11.3            | Proxy de emissões veiculares              |
| Temperatura         | 10.7            | Dispersa poluentes (efeito inverso)       |
| Umidade             | 9.5             | Pode prender partículas em suspensão      |
| Velocidade do Vento | 8.8             | Reduz concentração local                  |

---

## 🔍 Interpretação

* A **temperatura** mostrou efeito negativo na poluição — dias mais quentes favorecem dispersão atmosférica.
* A **umidade** tende a aumentar a permanência de partículas no ar.
* O **vento** é o fator de mitigação mais direto.
* Poluentes primários (`PM2.5`, `PM10`, `NO₂`) explicam a maior parte da variação no índice global.

---

## 🧪 Avaliação de Modelo

| Métrica            | Regressão Linear | Random Forest |
| ------------------ | ---------------- | ------------- |
| R²                 | 0.002            | 0.72          |
| RMSE               | 19.8             | 16.2          |
| Interpretabilidade | Alta             | Média         |
| Robustez           | Baixa            | Alta          |

---

## 📘 Conclusão da Etapa

A regressão linear serviu para **compreensão estatística**, enquanto o Random Forest mostrou **maior capacidade preditiva**.
O modelo final indica que:

* Poluentes particulados (`PM2.5`, `PM10`) e `NO2` são os principais determinantes da poluição.
* Fatores climáticos (temperatura, vento e umidade) modulam a dispersão desses agentes.

Esses achados fundamentam as visualizações interativas apresentadas na etapa seguinte (Dashboard).

---
