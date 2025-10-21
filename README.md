<h1 align="center">🌍 Air Quality Analysis</h1>
<p align="center">
  <em>Análise e visualização de dados ambientais — integrando estatística, machine learning e storytelling visual.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python"/>
  <img src="https://img.shields.io/badge/Dash-Plotly-orange.svg" alt="Dash"/>
  <img src="https://img.shields.io/badge/Status-Concluído-success.svg" alt="Status"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="License"/>
</p>

---

## 🎯 Objetivo
Explorar e compreender **quais fatores mais influenciam o aumento da poluição atmosférica** em grandes cidades.  
O projeto combina análise estatística, modelagem preditiva e **visualização interativa** via Dash.

---

## 🧱 Estrutura do Projeto
```

air-quality-analysis/
│
├── data/                  # Dados brutos e processados
├── notebooks/             # Notebooks de análise (Etapas 1–6)
├── app/                   # Dashboard interativo em Dash
├── reports/               # Documentação técnica (.md)
├── requirements.txt
└── README.md

````

---

## ⚙️ Tecnologias Utilizadas
| Categoria | Ferramentas |
|------------|-------------|
| Linguagem | Python 3.11 |
| Visualização | Matplotlib, Seaborn, Plotly, Dash |
| Machine Learning | Scikit-learn, Statsmodels |
| Manipulação de Dados | Pandas, NumPy |

---

## 📊 Pipeline Analítico
| Etapa | Descrição |
|-------|------------|
| **1.** | Coleta e análise inicial do dataset |
| **2.** | Limpeza e engenharia de atributos |
| **3.** | EDA (Análise Exploratória de Dados) |
| **4.** | Modelagem explicativa — Regressão Linear & Random Forest |
| **5.** | Dashboard interativo com Dash |
| **6–7.** | Validação, storytelling e conclusões finais |

---

## 🖥️ Dashboard
Visualização interativa que exibe:
- Índice médio de poluição por cidade  
- Relação entre poluentes e variáveis meteorológicas  
- Tendências mensais e sazonais  

### Execução local:
```bash
cd app
python dashboard_air_quality.py
````

👉 Acesse em: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 📈 Principais Insights

* **Temperatura e vento** reduzem os níveis de poluição.
* **Umidade** tende a manter partículas suspensas.
* **Meses frios e secos** concentram maiores índices.
* O modelo **Random Forest** apresentou maior poder explicativo e estabilidade.

---

## 🌐 Deploy (opcional)

Você pode publicar o dashboard gratuitamente em:

* [Render](https://render.com)
* [Railway](https://railway.app)
* [Vercel](https://vercel.com)

---

## ✨ Autor

**Zara Takion**
📧 [[seuemail@dominio.com](mailto:seuemail@dominio.com)]
🔗 [github.com/seuusuario](https://github.com/seuusuario)

---

## 🪶 Licença

Distribuído sob a [MIT License](LICENSE).
