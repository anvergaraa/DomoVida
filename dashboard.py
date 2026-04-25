"""
================================================================================
DomoVida  ·  Plataforma IoT Asistencial con Telemetría Biomédica
Dashboard Clínico — Versión 3.0  (Rediseño Corporativo)
================================================================================
Tesis: Diseño e Implementación de una Plataforma IoT Asistencial con
       Telemetría Biomédica Orientada a la Inclusión y Autonomía Funcional
Institución: Duoc UC  |  Fecha: 2026
================================================================================
"""

import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import time
from datetime import datetime

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DomoVida · Clinical Monitor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────────────────
# SISTEMA DE DISEÑO — CSS CORPORATIVO MÉDICO
# ──────────────────────────────────────────────────────────────────────────────
def aplicar_estilos():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Outfit:wght@300;400;500;600&family=Roboto+Mono:wght@400;600&display=swap');

    :root {
        --bg-base:        #070c14;
        --bg-surface:     #0d1520;
        --bg-elevated:    #111d2e;
        --bg-card:        #0f1a28;
        --border-subtle:  rgba(30, 200, 200, 0.10);
        --border-mid:     rgba(30, 200, 200, 0.20);
        --border-strong:  rgba(30, 200, 200, 0.45);
        --teal:           #1ec8c8;
        --teal-glow:      rgba(30, 200, 200, 0.18);
        --teal-dim:       rgba(30, 200, 200, 0.06);
        --blue-accent:    #2d82ff;
        --green:          #00d97e;
        --green-dim:      rgba(0, 217, 126, 0.12);
        --amber:          #ffb547;
        --amber-dim:      rgba(255, 181, 71, 0.12);
        --red:            #ff4f6a;
        --red-dim:        rgba(255, 79, 106, 0.12);
        --text-primary:   #e8f4f8;
        --text-secondary: #7a9ab5;
        --text-dim:       #3d5a72;
        --font-display:   'Syne', sans-serif;
        --font-body:      'Outfit', sans-serif;
        --font-mono:      'Roboto Mono', monospace;
        --radius-sm:      8px;
        --radius-md:      14px;
        --radius-lg:      20px;
    }

    /* ── BASE ── */
    .stApp, [data-testid="stAppViewContainer"] {
        background: var(--bg-base) !important;
        font-family: var(--font-body);
        color: var(--text-primary);
    }

    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] {
        background: var(--bg-surface) !important;
        border-right: 1px solid var(--border-subtle);
    }
    [data-testid="stSidebar"] * { color: var(--text-primary) !important; }

    /* ── HEADER ── */
    .dv-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 0 16px 0;
        border-bottom: 1px solid var(--border-subtle);
        margin-bottom: 28px;
    }
    .dv-logo {
        font-family: var(--font-display);
        font-size: 34px;
        font-weight: 800;
        background: linear-gradient(110deg, #ffffff 0%, var(--teal) 60%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
    }
    .dv-logo-sub {
        font-family: var(--font-body);
        font-size: 12px;
        color: var(--text-secondary);
        letter-spacing: 0.15em;
        text-transform: uppercase;
    }
    .dv-status-pill {
        display: flex; align-items: center; gap: 8px;
        background: var(--green-dim); border: 1px solid rgba(0, 217, 126, 0.25);
        border-radius: 40px; padding: 6px 16px; font-size: 12px; color: var(--green);
    }
    .dv-dot {
        width: 8px; height: 8px; border-radius: 50%; background: var(--green);
        box-shadow: 0 0 8px var(--green); animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }

    /* ── MÉTRICAS ── */
    .metric-wrap {
        background: var(--bg-card); border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md); padding: 22px; position: relative;
    }
    .metric-wrap::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0;
        height: 2px; background: var(--teal);
    }
    .metric-wrap.st-normal::before  { background: var(--green); }
    .metric-wrap.st-warning::before { background: var(--amber); }
    .metric-wrap.st-critical::before{ background: var(--red);   }

    .metric-label { font-size: 11px; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 6px; }
    .metric-val { font-family: var(--font-mono); font-weight: 600; line-height: 1; }
    .metric-val.sz-xl  { font-size: 52px; }
    .metric-val.sz-lg  { font-size: 36px; }

    .metric-val.c-normal   { color: var(--green); }
    .metric-val.c-warning  { color: var(--amber); }
    .metric-val.c-critical { color: var(--red);   }
    .metric-val.c-blue     { color: var(--teal);  }

    .metric-badge {
        display: inline-block; font-size: 11px; padding: 3px 10px;
        border-radius: 20px; margin-top: 10px;
    }
    .badge-normal   { background: var(--green-dim); color: var(--green); }
    .badge-warning  { background: var(--amber-dim); color: var(--amber); }
    .badge-critical { background: var(--red-dim);   color: var(--red);   }
    .badge-neutral  { background: var(--teal-dim);  color: var(--teal);  }

    /* ── PERFIL ── */
    .profile-card { background: var(--bg-elevated); border-radius: var(--radius-md); padding: 18px; }
    .profile-name { font-family: var(--font-display); font-size: 16px; font-weight: 700; }
    .allergy-tag {
        display: inline-block; background: var(--red-dim); color: var(--red);
        border-radius: 4px; padding: 2px 8px; font-size: 10px; margin: 2px;
    }
    .dv-section {
        font-size: 11px; font-weight: 600; color: var(--teal);
        text-transform: uppercase; letter-spacing: 0.1em; margin: 15px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# MÓDULOS DE DATOS Y LÓGICA
# ──────────────────────────────────────────────────────────────────────────────
def obtener_signos_vitales(limite=40):
    conn = sqlite3.connect('base_domovida.db')
    df = pd.read_sql_query(f"SELECT * FROM signos_vitales ORDER BY id DESC LIMIT {limite}", conn)
    conn.close()
    return df.iloc[::-1].reset_index(drop=True)

def obtener_perfil_paciente():
    return {
        "nombre": "María González Rojas", "edad": 78, "rut": "12.345.678-9",
        "habitacion": "304-B", "diagnostico": "Hipertensión Arterial",
        "medico": "Dr. Carlos Fuentes", "alergias": ["Penicilina", "Ibuprofeno"]
    }

def evaluar_bpm(bpm):
    if bpm < 60: return {"estado": "Bradicardia", "clase": "warning", "emoji": "⚠️", "badge": "badge-warning", "card": "st-warning"}
    if bpm <= 100: return {"estado": "Normal", "clase": "normal", "emoji": "✅", "badge": "badge-normal", "card": "st-normal"}
    return {"estado": "Taquicardia", "clase": "critical", "emoji": "🚨", "badge": "badge-critical", "card": "st-critical"}

# ──────────────────────────────────────────────────────────────────────────────
# RENDERIZADO UI
# ──────────────────────────────────────────────────────────────────────────────
def main():
    aplicar_estilos()
    perfil = obtener_perfil_paciente()

    # Sidebar
    st.sidebar.markdown("<div class='dv-logo' style='font-size:24px'>DomoVida</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<div class='dv-section'>👤 Paciente</div>", unsafe_allow_html=True)
    alergias_html = "".join([f"<span class='allergy-tag'>{a}</span>" for a in perfil["alergias"]])
    st.sidebar.markdown(f"""
        <div class='profile-card'>
            <div class='profile-name'>{perfil['nombre']}</div>
            <div style='font-size:12px; color:#7a9ab5'>{perfil['rut']}</div>
            <div style='font-size:13px; margin-top:10px'>🏥 Hab: {perfil['habitacion']}</div>
            <div style='margin-top:10px'>{alergias_html}</div>
        </div>
    """, unsafe_allow_html=True)
    
    intervalo = st.sidebar.slider("Refresco (seg)", 2, 10, 3)
    n_registros = st.sidebar.slider("Registros", 10, 60, 30)

    # Header
    ahora = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"""
        <div class='dv-header'>
            <div><div class='dv-logo'>DomoVida</div><div class='dv-logo-sub'>Monitor Clínico IoT</div></div>
            <div class='dv-status-pill'><span class='dv-dot'></span> Sistema Activo · {ahora}</div>
        </div>
    """, unsafe_allow_html=True)

    placeholder = st.empty()

    while True:
        with placeholder.container():
            datos = obtener_signos_vitales(limite=n_registros)
            if not datos.empty:
                ultimo_bpm = datos['valor'].iloc[-1]
                ev = evaluar_bpm(ultimo_bpm)

                # Métricas
                st.markdown("<div class='dv-section'>📊 Métricas Actuales</div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.markdown(f"<div class='metric-wrap {ev['card']}'><div class='metric-label'>Frecuencia</div><span class='metric-val sz-xl c-{ev['clase']}'>{int(ultimo_bpm)}</span><span style='color:#3d5a72'> bpm</span><br><div class='metric-badge {ev['badge']}'>{ev['emoji']} {ev['estado']}</div></div>", unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<div class='metric-wrap'><div class='metric-label'>Promedio</div><span class='metric-val sz-lg c-blue'>{round(datos['valor'].mean(),1)}</span><span style='color:#3d5a72'> bpm</span><br><div class='metric-badge badge-neutral'>Sesión</div></div>", unsafe_allow_html=True)
                with c3:
                    st.markdown(f"<div class='metric-wrap'><div class='metric-label'>Máximo</div><span class='metric-val sz-lg' style='color:#ffb547'>{int(datos['valor'].max())}</span><span style='color:#3d5a72'> bpm</span><br><div class='metric-badge badge-warning'>Pico</div></div>", unsafe_allow_html=True)

                # Gráfico
                st.markdown("<div class='dv-section'>📈 Evolución Temporal</div>", unsafe_allow_html=True)
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=datos['fecha'], y=datos['valor'], mode='lines+markers', 
                                         line=dict(color='#1ec8c8', width=3, shape='spline'),
                                         fill='tozeroy', fillcolor='rgba(30,200,200,0.05)'))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                                  height=300, margin=dict(l=0,r=0,t=0,b=0),
                                  xaxis=dict(showgrid=False, color="#3d5a72"),
                                  yaxis=dict(gridcolor='rgba(30,200,200,0.1)', range=[40,140], color="#3d5a72"))
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("<div class='dv-section'>📋 Historial Registrado</div>", unsafe_allow_html=True)
                st.dataframe(datos, use_container_width=True)
            time.sleep(intervalo)

if __name__ == "__main__":
    main()
