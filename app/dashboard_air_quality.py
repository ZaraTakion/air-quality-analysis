# ==========================================================
# DASHBOARD DE QUALIDADE DO AR — VERSÃO OTIMIZADA E ESTILIZADA
# ==========================================================
# Ferramenta: Dash + Plotly (v3+)
# Execução:   python app/dashboard_air_quality.py
# Acesso:     http://127.0.0.1:8050/
# ==========================================================

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# ----------------------------------------------------------
# 1️⃣ Carregar dados processados
# ----------------------------------------------------------
df = pd.read_csv("data/processed/air_quality_clean.csv")
df["Data"] = pd.to_datetime(df["Date"], errors="coerce")
df["Mês"] = df["Data"].dt.month
df["Índice de Poluição"] = df[["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]].mean(axis=1)

# Traduções e unidades
traducao_poluentes = {
    "PM2.5": "Material Particulado Fino (PM2.5)",
    "PM10": "Material Particulado Grosso (PM10)",
    "NO2": "Dióxido de Nitrogênio (NO₂)",
    "SO2": "Dióxido de Enxofre (SO₂)",
    "CO": "Monóxido de Carbono (CO)",
    "O3": "Ozônio (O₃)"
}

# Paleta de cores principal
COR_PRINCIPAL = "#1E3A8A"   # Azul profundo
COR_SECUNDARIA = "#2563EB"  # Azul vivo
COR_DESTAQUE = "#16A34A"    # Verde eficiência
COR_FUNDO = "#F8FAFC"       # Fundo neutro

# ----------------------------------------------------------
# 2️⃣ Inicializar app e layout
# ----------------------------------------------------------
app = Dash(__name__)
app.title = "Painel Interativo — Qualidade do Ar"

app.layout = html.Div(style={"backgroundColor": COR_FUNDO, "fontFamily": "Segoe UI"}, children=[
    html.H1("🌎 Painel de Qualidade do Ar", 
            style={"textAlign": "center", "color": COR_PRINCIPAL, "marginTop": "20px"}),

    html.P("Visualize o impacto do clima e da sazonalidade sobre a poluição nas grandes cidades.",
           style={"textAlign": "center", "fontSize": "16px", "color": "#475569"}),

    html.Div([
        html.Label("Selecione uma cidade:", style={"fontWeight": "bold", "color": "#0f172a"}),
        dcc.Dropdown(
            id="city_dropdown",
            options=[{"label": c, "value": c} for c in sorted(df["City"].unique())],
            value="Tokyo",
            clearable=False,
            style={"width": "60%", "margin": "auto"}
        )
    ], style={"textAlign": "center", "marginBottom": "30px"}),

    html.Div(id="kpi_cards", style={
        "display": "flex",
        "justifyContent": "center",
        "gap": "20px",
        "flexWrap": "wrap",
        "marginBottom": "40px"
    }),

    html.Hr(),

    dcc.Graph(id="grafico_tendencia"),
    dcc.Graph(id="grafico_relacao"),
    dcc.Graph(id="grafico_boxplot"),

    html.Footer("Fonte: Global Air Quality Dataset (Kaggle, 2023)",
                style={"textAlign": "center", "fontSize": "12px", "color": "#94A3B8", "marginTop": "40px"})
])

# ----------------------------------------------------------
# 3️⃣ Callbacks — KPIs e gráficos
# ----------------------------------------------------------
@app.callback(
    Output("kpi_cards", "children"),
    Output("grafico_tendencia", "figure"),
    Output("grafico_relacao", "figure"),
    Output("grafico_boxplot", "figure"),
    Input("city_dropdown", "value")
)
def atualizar_dashboard(cidade):
    subset = df[df["City"] == cidade]

    # --- KPIs ---
    media_pol = subset["Índice de Poluição"].mean()
    mes_pico = int(subset.groupby("Mês")["Índice de Poluição"].mean().idxmax())
    menor_pm25 = subset["PM2.5"].min()

    cards = [
        html.Div([
            html.H3("Índice Médio", style={"color": "#64748B"}),
            html.H2(f"{media_pol:.1f}", style={"color": COR_SECUNDARIA})
        ], style={"background": "white", "borderRadius": "12px", "padding": "20px", "width": "180px",
                  "boxShadow": "0 2px 6px rgba(0,0,0,0.1)", "textAlign": "center"}),

        html.Div([
            html.H3("Mês Mais Crítico", style={"color": "#64748B"}),
            html.H2(f"{mes_pico}", style={"color": "#DC2626"})
        ], style={"background": "white", "borderRadius": "12px", "padding": "20px", "width": "180px",
                  "boxShadow": "0 2px 6px rgba(0,0,0,0.1)", "textAlign": "center"}),

        html.Div([
            html.H3("Menor PM2.5", style={"color": "#64748B"}),
            html.H2(f"{menor_pm25:.2f}", style={"color": COR_DESTAQUE})
        ], style={"background": "white", "borderRadius": "12px", "padding": "20px", "width": "180px",
                  "boxShadow": "0 2px 6px rgba(0,0,0,0.1)", "textAlign": "center"})
    ]

    # --- Gráfico 1: Tendência Mensal ---
    tendencia = subset.groupby("Mês")["Índice de Poluição"].mean().reset_index()
    fig1 = px.line(
        tendencia, x="Mês", y="Índice de Poluição",
        markers=True, color_discrete_sequence=[COR_SECUNDARIA],
        title=f"Tendência Mensal da Poluição — {cidade}"
    )
    fig1.update_traces(mode="lines+markers", marker=dict(size=8))
    fig1.update_layout(template="plotly_white", title_font_color=COR_PRINCIPAL)

    # --- Gráfico 2: Relação Clima × Poluição ---
    fig2 = px.scatter(
        subset, x="Temperature", y="Índice de Poluição",
        color="Humidity", size="Wind Speed",
        color_continuous_scale="Viridis",
        title=f"Relação entre Clima e Poluição — {cidade}",
        labels={"Temperature": "Temperatura (°C)", "Humidity": "Umidade (%)", "Wind Speed": "Velocidade do Vento (km/h)"}
    )
    fig2.update_layout(template="plotly_white", title_font_color=COR_PRINCIPAL)

    # --- Gráfico 3: Distribuição de Poluentes ---
    melted = subset.melt(id_vars=["City"], 
                         value_vars=list(traducao_poluentes.keys()), 
                         var_name="Poluente", value_name="Concentração")
    melted["Poluente"] = melted["Poluente"].map(traducao_poluentes)
    fig3 = px.box(
        melted, x="Poluente", y="Concentração", color="Poluente",
        color_discrete_sequence=px.colors.qualitative.Safe,
        title=f"Distribuição dos Poluentes — {cidade}"
    )
    fig3.update_layout(template="plotly_white", showlegend=False, title_font_color=COR_PRINCIPAL)

    return cards, fig1, fig2, fig3

# ----------------------------------------------------------
# 4️⃣ Executar servidor
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
