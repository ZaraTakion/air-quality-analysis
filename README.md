# 🌍 Air Quality Analysis — Análise e Visualização da Qualidade do Ar

Projeto completo de **Ciência de Dados aplicada ao meio ambiente**, explorando a relação entre condições meteorológicas e níveis de poluição em grandes cidades.  
Inclui desde a coleta e limpeza de dados até a modelagem explicativa e criação de um **dashboard interativo em Dash**.

---

## 🎯 Objetivo
Identificar **quais fatores mais influenciam o aumento da poluição atmosférica** e comunicar os resultados de forma clara e visual, unindo análise estatística e storytelling de dados.

---

## 🧱 Estrutura do Projeto
```
air-quality-analysis/
│
├── data/
│   ├── raw/                → dados brutos originais
│   ├── processed/          → dataset limpo e final
│
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_modelagem_explicativa.ipynb
│   └── 06_validation_and_storytelling.ipynb
│
├── app/
│   └── dashboard_air_quality.py
│
├── reports/
│   ├── data_dictionary.md
│   ├── Etapa_4_Modelagem.md
│   ├── Dashboard.md
│   └── Etapa_7_Conclusao.md
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.11+**
- Pandas, NumPy  
- Matplotlib, Seaborn, Plotly  
- Scikit-learn, Statsmodels  
- Dash (visualização interativa)

---

## 📊 Etapas do Projeto
| Etapa | Descrição |
|-------|------------|
| **1.** | Coleta e análise inicial do dataset |
| **2.** | Limpeza, tratamento e engenharia de atributos |
| **3.** | Análise exploratória e visualização (EDA) |
| **4.** | Modelagem explicativa (Regressão Linear e Random Forest) |
| **5.** | Dashboard interativo em Dash |
| **6–7.** | Validação, storytelling e conclusão |

---

## 🎨 Dashboard
Dashboard interativo construído com **Dash + Plotly**, exibindo:
- Índice médio de poluição por cidade  
- Correlação entre temperatura, umidade e poluentes  
- Variações mensais e sazonais  

Para executar localmente:
```bash
cd app
python dashboard_air_quality.py
```
Acesse: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 📈 Principais Insights
- **Temperatura** e **vento** reduzem os níveis de poluição.  
- **Umidade** e **meses frios** elevam a concentração de partículas.  
- Cidades com **alto tráfego e clima estável** tendem a ser as mais poluídas.  
- O modelo **Random Forest** capturou relações não lineares com melhor precisão.

---

## 🚀 Próximos Passos
- Incluir dados de múltiplos anos e mais cidades.  
- Implementar modelos explicáveis (XGBoost + SHAP).  
- Integrar APIs em tempo real de qualidade do ar e clima.  
- Publicar o dashboard online (Render, Railway, ou Vercel).

---

## ✨ Autor
**Zara Takion**  
📧 Contato: [seuemail@dominio.com]  
🔗 Portfólio: [github.com/seuusuario](https://github.com/seuusuario)

---

## 🪶 Licença
Este projeto é distribuído sob a [MIT License](LICENSE).
