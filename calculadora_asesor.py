import base64
import os
import streamlit as st

st.set_page_config(
    page_title="Incentivos Coppel",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
.stApp { background-color: #F8FAFC; font-family: 'Segoe UI', sans-serif; }
div.block-container { padding-top: 0.5rem !important; padding-bottom: 1rem !important; }
[data-testid="stSidebar"] { display: none !important; }
button[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarCollapseButton"] { display: none !important; }
div[data-testid="stVerticalBlock"] > div { gap: 0.3rem !important; }

div[data-testid="stExpander"] summary p {
    font-size: 1.05em !important;
    font-weight: bold !important;
    color: #0B2B5C !important;
}
div[data-testid="stExpander"] {
    border-left: 5px solid #0B2B5C !important;
    border-radius: 12px !important;
    background: white !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    margin-bottom: 8px !important;
}

.chip-verde    { background-color: #D1FAE5; color: #065F46; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; font-weight: bold; display: inline-block; margin: 2px 0; }
.chip-rojo     { background-color: #FEE2E2; color: #991B1B; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; font-weight: bold; display: inline-block; margin: 2px 0; }
.chip-amarillo { background-color: #FEF3C7; color: #92400E; border-radius: 20px; padding: 4px 12px; font-size: 0.85em; font-weight: bold; display: inline-block; margin: 2px 0; }

.metrica-box { background: #EBF3FC; border-radius: 12px; padding: 8px 10px; text-align: center; margin: 4px 0; }
.metrica-valor { font-size: 1.3em; font-weight: bold; color: #0B2B5C; }
.metrica-etiqueta { font-size: 0.75em; color: #475569; }

.resultado-card {
    background: linear-gradient(135deg, #0B2B5C, #1058B0);
    border-radius: 16px; padding: 20px; text-align: center;
    color: white; margin-top: 12px; box-shadow: 0 6px 20px rgba(11,43,92,0.3);
}
.resultado-total { font-size: 2.5em; font-weight: bold; color: #FFD100; }
.resultado-label { font-size: 0.95em; color: white; margin-bottom: 6px; }

.divider-azul { border: none; border-top: 1.5px solid #CBD5E1; opacity: 0.5; margin: 6px 0 8px 0; }

.stSelectbox > div > div {
    border: 2px solid #0B2B5C !important;
    border-radius: 12px !important;
}

.stTextInput > div > div > input {
    border: 2px solid #0B2B5C !important;
    border-radius: 10px !important;
    font-size: 1.05em !important;
    padding: 8px 12px !important;
}

#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)


def leer_porcentaje(label, placeholder, key):
    val = st.text_input(label, placeholder=placeholder, key=key)
    try:
        resultado = float(val.replace(",", ".")) if val else 0.0
        return max(0.0, min(200.0, resultado))
    except:
        st.markdown(
            "<span class='chip-rojo'>⚠️ Número no válido</span>",
            unsafe_allow_html=True,
        )
        return 0.0


def leer_monto(label, placeholder, key):
    val = st.text_input(label, placeholder=placeholder, key=key)
    try:
        resultado = (
            float(val.replace(",", "").replace("$", "")) if val else 0.0
        )
        return max(0.0, resultado)
    except:
        st.markdown(
            "<span class='chip-rojo'>⚠️ Monto no válido</span>",
            unsafe_allow_html=True,
        )
        return 0.0


def leer_unidades(label, placeholder, key):
    val = st.text_input(label, placeholder=placeholder, key=key)
    try:
        resultado = (
            int(val.replace(",", "").replace(".", "")) if val else 0
        )
        return max(0, resultado)
    except:
        st.markdown(
            "<span class='chip-rojo'>⚠️ Cantidad no válida</span>",
            unsafe_allow_html=True,
        )
        return 0


def chip(tipo, texto):
    st.markdown(
        "<span class='chip-" + tipo + "'>" + texto + "</span>",
        unsafe_allow_html=True,
    )


def metrica(etiqueta, valor):
    html = (
        "<div class='metrica-box'><div class='metrica-etiqueta'>"
        + etiqueta
        + "</div><div class='metrica-valor'>"
        + valor
        + "</div></div>"
    )
    st.markdown(html, unsafe_allow_html=True)


def resultado_final(total, desglose):
    html = "<div class='resultado-card'>"
    html += "<div class='resultado-label'>🏆 TU INCENTIVO TOTAL DEL MES</div>"
    html += (
        "<div class='resultado-total'>$" + "{:,.2f}".format(total) + " MXN</div>"
    )
    html += (
        "<br><div style='font-size:0.85em;color:#EBF3FC;'>"
        + desglose
        + "</div>"
    )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def divider():
    st.markdown("<hr class='divider-azul'>", unsafe_allow_html=True)


def header_azul(titulo, subtitulo):
    if os.path.exists("logo_coppel.png"):
        with open("logo_coppel.png", "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
        st.markdown(
            "<div style='text-align:center;margin-bottom:0px;padding:6px 0px 0px 0px;'>"
            "<img src='data:image/png;base64,"
            + logo_b64
            + "' style='height:100px;'>"
            "</div>",
            unsafe_allow_html=True,
        )
    html = (
        "<div style='background:linear-gradient(135deg,#0B2B5C,#1058B0);"
    )
    html += "padding:16px 20px;border-radius:16px;text-align:center;"
    html += "margin-bottom:12px;margin-top:4px;box-shadow:0 4px 12px rgba(11,43,92,0.25);'>"
    html += (
        "<span style='font-size:1.4em;font-weight:bold;color:#FFD100;'>"
        + titulo
        + "</span><br>"
    )
    html += (
        "<span style='color:white;font-size:0.9em;'>" + subtitulo + "</span>"
    )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ==============================================================================
# TABULADORES PILAR 1 POR PUESTO
# ==============================================================================
def inc_base_asesor_ventas(cump):
    if cump < 85:
        return 0
    elif cump < 90:
        return 250
    elif cump < 95:
        return 500
    elif cump < 100:
        return 850
    elif cump < 110:
        return 1300
    elif cump < 120:
        return 1650
    else:
        return 2000


def inc_base_telefonia(cump):
    if cump < 90:
        return 0
    elif cump < 95:
        return 900
    elif cump < 100:
        return 1100
    elif cump < 110:
        return 1450
    elif cump < 120:
        return 1750
    else:
        return 2100


def inc_base_optometrista(cump, venta_monto):
    if venta_monto < 45000:
        return 0
    if cump < 80:
        return 0
    elif cump < 90:
        return 500
    elif cump < 95:
        return 900
    elif cump < 100:
        return 1200
    elif cump < 110:
        return 1600
    elif cump < 120:
        return 1900
    else:
        return 2300


# ==============================================================================
# PILAR 2: VENTA GRUPAL (INDICADORES DE TIENDA - MONTOS FIJOS)
# ==============================================================================
def pilar2_venta_grupal(prefix):
    st.markdown("**Indicadores de Tienda (Incentivos Adicionales Fijos)**")
    cump_credito = leer_porcentaje(
        "% Cumplimiento Venta a Crédito Tienda", "Ej: 96.0", prefix + "_credito"
    )
    cump_digital = leer_porcentaje(
        "% Cumplimiento 1ª Compra Canal Digital",
        "Ej: 103.0",
        prefix + "_digital",
    )
    cump_tienda = leer_porcentaje(
        "% Cumplimiento Venta Total Tienda", "Ej: 100.0", prefix + "_tienda"
    )

    inc_credito = 150.0 if cump_credito >= 90 else 0.0
    inc_digital = 150.0 if cump_digital >= 90 else 0.0
    inc_tienda = 300.0 if cump_tienda >= 100 else 0.0

    if inc_credito > 0:
        chip("verde", "✅ Crédito Tienda ≥ 90% → +$150")
    else:
        chip("rojo", "❌ Crédito Tienda < 90% → +$0")

    if inc_digital > 0:
        chip("verde", "✅ 1ª Compra Digital ≥ 90% → +$150")
    else:
        chip("rojo", "❌ 1ª Compra Digital < 90% → +$0")

    if inc_tienda > 0:
        chip("verde", "✅ Venta Tienda ≥ 100% → +$300")
    else:
        chip("rojo", "❌ Venta Tienda < 100% → +$0")

    total_pilar2 = inc_credito + inc_digital + inc_tienda
    metrica(
        "🤝 Total Pilar 2 (Venta Grupal)", "$" + "{:,.2f}".format(total_pilar2)
    )
    return total_pilar2


# ==============================================================================
# PILAR 3: COMISIÓN INDIVIDUAL (MONTO FIJO POR UNIDAD VENDIDA)
# ==============================================================================
def pilar3_comision_unidades(cump_equipo, umbral_min, prefix):
    if cump_equipo < umbral_min:
        chip(
            "rojo",
            f"❌ Cump. Equipo < {umbral_min}% — No habilita comisiones del Pilar 3",
        )
        return 0.0

    es_top = cump_equipo >= 100
    if es_top:
        chip("verde", "✅ Cump. Equipo ≥ 100% → Tasas Máximas Activas")
        m_club, m_mrc, m_mplus, m_cel, m_gex, m_arm, m_inst = (
            3.0,
            40.0,
            90.0,
            10.0,
            30.0,
            15.0,
            70.0,
        )
    else:
        chip(
            "amarillo",
            f"⚠️ Cump. Equipo ≥ {umbral_min}% → Tasas Básicas Activas",
        )
        m_club, m_mrc, m_mplus, m_cel, m_gex, m_arm, m_inst = (
            1.5,
            25.0,
            50.0,
            5.0,
            15.0,
            10.0,
            40.0,
        )

    divider()
    st.markdown("**Ingresa el número de servicios/seguros vendidos:**")

    q_gex = leer_unidades(
        "🔧 Garantía Extendida GEX (Cantidad)", "Ej: 45", prefix + "_gex"
    )
    q_arm = leer_unidades(
        "🔩 Servicio de Armado (Cantidad)", "Ej: 8", prefix + "_arm"
    )
    q_inst = leer_unidades(
        "🔌 Servicio de Instalaciones (Cantidad)", "Ej: 2", prefix + "_inst"
    )
    q_club = leer_unidades(
        "🛡️ Club de Protección (Cantidad)", "Ej: 40", prefix + "_club"
    )
    q_mrc = leer_unidades(
        "🏍️ Seguro Motos RC (Cantidad)", "Ej: 20", prefix + "_mrc"
    )
    q_mplus = leer_unidades(
        "🏍️ Seguro Motos Plus (Cantidad)", "Ej: 5", prefix + "_mplus"
    )
    q_cel = leer_unidades(
        "📱 Seguro Celulares (Cantidad)", "Ej: 52", prefix + "_cel"
    )

    t_gex = q_gex * m_gex
    t_arm = q_arm * m_arm
    t_inst = q_inst * m_inst
    t_club = q_club * m_club
    t_mrc = q_mrc * m_mrc
    t_mplus = q_mplus * m_mplus
    t_cel = q_cel * m_cel

    total_comision = t_gex + t_arm + t_inst + t_club + t_mrc + t_mplus + t_cel

    col1, col2 = st.columns(2)
    with col1:
        metrica(
            "🔧 Servicios (GEX/Arm/Inst)",
            "$" + "{:,.2f}".format(t_gex + t_arm + t_inst),
        )
    with col2:
        metrica(
            "🛡️ Seguros (Club/Motos/Cel)",
            "$" + "{:,.2f}".format(t_club + t_mrc + t_mplus + t_cel),
        )

    metrica(
        "💼 Total Comisiones Pilar 3", "$" + "{:,.2f}".format(total_comision)
    )
    return total_comision


# ==============================================================================
# INTERFAZ PRINCIPAL
# ==============================================================================
header_azul(
    "🏆 Incentivos Coppel 2026", "Calculadora Operativa para Tiendas Piloto"
)

puesto = st.selectbox(
    "👤 Selecciona tu puesto:",
    options=[
        "🎯 Asesor de Ventas",
        "📱 Asesor de Telefonía",
        "👁️ Optometrista",
    ],
)
divider()

# ------------------------------------------------------------------------------
# PANTALLA: ASESOR DE VENTAS
# ------------------------------------------------------------------------------
if puesto == "🎯 Asesor de Ventas":
    header_azul("🎯 Asesor de Ventas", "Esquema de 3 Pilares")

    with st.expander("🤝 Pilar 1 — Venta de Equipo", expanded=True):
        cump_eq = leer_porcentaje(
            "% Cumplimiento Meta del Equipo", "Ej: 103.0", "av_eq"
        )
        inc_p1 = inc_base_asesor_ventas(cump_eq)
        if cump_eq < 85:
            chip("rojo", "❌ < 85% — Sin incentivo base")
        elif cump_eq < 100:
            chip("amarillo", "⚠️ Cumplimiento parcial (85%-99%)")
        else:
            chip("verde", "✅ Meta alcanzada (≥ 100%)")
        metrica("💰 Incentivo Base Pilar 1", "$" + "{:,.2f}".format(inc_p1))

    with st.expander("🏪 Pilar 2 — Venta Grupal", expanded=True):
        inc_p2 = pilar2_venta_grupal("av")

    with st.expander("💼 Pilar 3 — Comisión Individual", expanded=True):
        inc_p3 = pilar3_comision_unidades(cump_eq, 85, "av")

    total_final = inc_p1 + inc_p2 + inc_p3
    desglose = f"Pilar 1 (Equipo): ${inc_p1:,.2f} | Pilar 2 (Grupal): ${inc_p2:,.2f} | Pilar 3 (Comisiones): ${inc_p3:,.2f}"
    resultado_final(total_final, desglose)

# ------------------------------------------------------------------------------
# PANTALLA: ASESOR DE TELEFONÍA
# ------------------------------------------------------------------------------
elif puesto == "📱 Asesor de Telefonía":
    header_azul("📱 Asesor de Telefonía", "Esquema de 3 Pilares")

    with st.expander("🤝 Pilar 1 — Venta de Equipo (Telefonía)", expanded=True):
        cump_eq = leer_porcentaje(
            "% Cumplimiento Meta de Telefonía", "Ej: 106.0", "at_eq"
        )
        inc_p1 = inc_base_telefonia(cump_eq)
        if cump_eq < 90:
            chip("rojo", "❌ < 90% — Sin incentivo base")
        elif cump_eq < 100:
            chip("amarillo", "⚠️ Cumplimiento parcial (90%-99%)")
        else:
            chip("verde", "✅ Meta alcanzada (≥ 100%)")
        metrica("💰 Incentivo Base Pilar 1", "$" + "{:,.2f}".format(inc_p1))

    with st.expander("🏪 Pilar 2 — Venta Grupal", expanded=True):
        inc_p2 = pilar2_venta_grupal("at")

    with st.expander("💼 Pilar 3 — Comisión Individual", expanded=True):
        inc_p3 = pilar3_comision_unidades(cump_eq, 90, "at")

    total_final = inc_p1 + inc_p2 + inc_p3
    desglose = f"Pilar 1 (Telefonía): ${inc_p1:,.2f} | Pilar 2 (Grupal): ${inc_p2:,.2f} | Pilar 3 (Comisiones): ${inc_p3:,.2f}"
    resultado_final(total_final, desglose)

# ------------------------------------------------------------------------------
# PANTALLA: OPTOMETRISTA
# ------------------------------------------------------------------------------
elif puesto == "👁️ Optometrista":
    header_azul("👁️ Optometrista", "Esquema de 3 Pilares")

    with st.expander("🤝 Pilar 1 — Venta de Óptica", expanded=True):
        v_monto = leer_monto(
            "Venta Total de Óptica en el Mes ($)", "Ej: 146100", "opt_monto"
        )
        cump_eq = leer_porcentaje(
            "% Cumplimiento Meta de Óptica", "Ej: 100.0", "opt_eq"
        )

        if v_monto <= 45000:
            chip("rojo", "❌ Venta de Óptica ≤ $45,000 — Sin incentivo base")
        elif cump_eq < 80:
            chip("rojo", "❌ < 80% Cumplimiento — Sin incentivo base")
        elif cump_eq < 100:
            chip("amarillo", "⚠️ Cumplimiento parcial (80%-99%)")
        else:
            chip("verde", "✅ Meta y Requisito alcanzados (≥ 100%)")

        inc_p1 = inc_base_optometrista(cump_eq, v_monto)
        metrica("💰 Incentivo Base Pilar 1", "$" + "{:,.2f}".format(inc_p1))

    with st.expander("🏪 Pilar 2 — Venta Grupal", expanded=True):
        inc_p2 = pilar2_venta_grupal("opt")

    with st.expander("💼 Pilar 3 — Comisión Individual", expanded=True):
        inc_p3 = pilar3_comision_unidades(cump_eq, 80, "opt")

    total_final = inc_p1 + inc_p2 + inc_p3
    desglose = f"Pilar 1 (Óptica): ${inc_p1:,.2f} | Pilar 2 (Grupal): ${inc_p2:,.2f} | Pilar 3 (Comisiones): ${inc_p3:,.2f}"
    resultado_final(total_final, desglose)

st.markdown("<br>", unsafe_allow_html=True)
st.caption(
    "Calculadora Interna Coppel - Versión Ajustada Octubre 2026 - Equipos Enfocados 2.0"
)
