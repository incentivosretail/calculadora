<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Incentivos</title>
    <link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --navy: #0B2B5C;
            --blue-accent: #1058B0;
            --yellow: #FFD100;
            --bg-gray: #F8FAFC;
            --card-bg: #FFFFFF;
            --border-color: #CBD5E1;
            --text-dark: #1E293B;
            --text-muted: #475569;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', sans-serif; }
        body { background-color: var(--bg-gray); color: var(--text-dark); padding: 12px; }

        .container { max-width: 600px; margin: 0 auto; padding-bottom: 20px; }

        /* Header Ejecutivo */
        .header {
            background: linear-gradient(135deg, var(--navy), var(--blue-accent));
            color: white; border-radius: 16px; padding: 20px; text-align: center;
            box-shadow: 0 4px 12px rgba(11, 43, 92, 0.25); margin-bottom: 12px;
        }
        .header h1 { font-size: 1.5rem; color: var(--yellow); font-weight: 700; margin: 0; }

        /* Tarjetas Estilo Streamlit Expander */
        .card {
            background: var(--card-bg); border-radius: 12px; padding: 16px;
            border-left: 5px solid var(--navy); box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            margin-bottom: 12px;
        }
        .card-title { font-size: 1.05rem; font-weight: 700; color: var(--navy); margin-bottom: 12px; }

        /* Inputs y Labels */
        label { font-size: 0.85rem; font-weight: 600; color: var(--text-muted); display: block; margin-bottom: 4px; }
        input, select {
            width: 100%; padding: 10px 12px; font-size: 1.05rem; font-weight: 600;
            border: 2px solid var(--navy); border-radius: 10px; margin-bottom: 12px;
            outline: none; transition: border-color 0.2s;
        }
        
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }

        /* Chips de Estatus */
        .chip { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; margin-bottom: 10px; margin-right: 5px; }
        .chip-green { background-color: #D1FAE5; color: #065F46; }
        .chip-red { background-color: #FEE2E2; color: #991B1B; }
        .chip-yellow { background-color: #FEF3C7; color: #92400E; }

        /* Cajas de Métricas Intermedias */
        .metrica-box {
            background: #EBF3FC; border-radius: 12px; padding: 10px; text-align: center; margin-top: 5px;
        }
        .metrica-etiqueta { font-size: 0.8rem; color: #475569; font-weight: 600; margin-bottom: 2px; }
        .metrica-valor { font-size: 1.4em; font-weight: 700; color: var(--navy); }

        /* Tarjeta de Resultado Final */
        .result-card {
            background: linear-gradient(135deg, var(--navy), var(--blue-accent));
            border-radius: 16px; padding: 24px 20px; text-align: center; color: white;
            box-shadow: 0 6px 20px rgba(11, 43, 92, 0.3); margin-top: 16px;
        }
        .result-title { font-size: 0.95rem; font-weight: 600; margin-bottom: 8px; }
        .result-total { font-size: 2.5rem; font-weight: 700; color: var(--yellow); }
        .result-breakdown { font-size: 0.85rem; color: #EBF3FC; margin-top: 12px; }
        
        .divider-azul { border: none; border-top: 1.5px solid #CBD5E1; opacity: 0.5; margin: 12px 0; }

        /* Footer */
        .footer { text-align: center; font-size: 0.75rem; color: var(--text-muted); margin-top: 20px; padding-bottom: 10px; }
    </style>
</head>
<body>

<div class="container">
    <!-- Header -->
    <div class="header">
        <h1>🏆 Calculadora de Incentivos</h1>
    </div>

    <!-- Puesto Selector -->
    <div class="card" style="border-left-color: var(--yellow);">
        <label for="puesto">👤 Selecciona tu Puesto:</label>
        <select id="puesto" onchange="calcular()">
            <option value="asesor">🎯 Asesor de Ventas</option>
            <option value="telefonia">📱 Asesor de Telefonía</option>
            <option value="optometrista">👁️ Optometrista</option>
        </select>
    </div>

    <!-- Pilar 1: Venta de Equipo -->
    <div class="card">
        <div class="card-title">🤝 Pilar 1 — Venta de Equipo</div>
        
        <div id="campo-optica-monto" style="display:none;">
            <label for="monto-optica">Venta Total de Óptica en el Mes ($):</label>
            <input type="number" id="monto-optica" placeholder="Ej: 146100" value="146100" oninput="calcular()">
        </div>

        <label for="cump-equipo">% Cumplimiento Meta del Equipo:</label>
        <input type="number" id="cump-equipo" placeholder="Ej: 103" value="103" oninput="calcular()">
        
        <div id="chip-pilar1"></div>
        <div class="metrica-box">
            <div class="metrica-etiqueta">💰 Incentivo Base Pilar 1</div>
            <div class="metrica-valor" id="res-p1">$0.00</div>
        </div>
    </div>

    <!-- Pilar 2: Venta Grupal -->
    <div class="card">
        <div class="card-title">🏪 Pilar 2 — Venta Grupal (Tienda)</div>
        <div class="grid-2">
            <div>
                <label for="cump-credito">% Venta a Crédito Tienda:</label>
                <input type="number" id="cump-credito" placeholder="Ej: 96" value="96" oninput="calcular()">
            </div>
            <div>
                <label for="cump-digital">% 1ª Compra Digital:</label>
                <input type="number" id="cump-digital" placeholder="Ej: 103" value="103" oninput="calcular()">
            </div>
        </div>
        <label for="cump-tienda">% Venta Total Tienda:</label>
        <input type="number" id="cump-tienda" placeholder="Ej: 100" value="100" oninput="calcular()">
        
        <div id="chips-pilar2"></div>
        <div class="metrica-box">
            <div class="metrica-etiqueta">🤝 Total Pilar 2 (Venta Grupal)</div>
            <div class="metrica-valor" id="res-p2">$0.00</div>
        </div>
    </div>

    <!-- Pilar 3: Comisiones Individuales -->
    <div class="card">
        <div class="card-title">💼 Pilar 3 — Comisión Individual (Unidades)</div>
        <div id="chip-pilar3-status"></div>
        <hr class="divider-azul">
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:12px; font-weight:600;">Ingresa la cantidad de unidades vendidas:</p>
        
        <div class="grid-2">
            <div>
                <label for="q-gex">🔧 Garantía Extendida:</label>
                <input type="number" id="q-gex" placeholder="0" value="45" oninput="calcular()">
            </div>
            <div>
                <label for="q-arm">🔩 Servicio Armado:</label>
                <input type="number" id="q-arm" placeholder="0" value="8" oninput="calcular()">
            </div>
            <div>
                <label for="q-inst">🔌 Instalaciones:</label>
                <input type="number" id="q-inst" placeholder="0" value="0" oninput="calcular()">
            </div>
            <div>
                <label for="q-club">🛡️ Club de Protección:</label>
                <input type="number" id="q-club" placeholder="0" value="0" oninput="calcular()">
            </div>
            <div>
                <label for="q-mrc">🏍️ Seguro Motos RC:</label>
                <input type="number" id="q-mrc" placeholder="0" value="20" oninput="calcular()">
            </div>
            <div>
                <label for="q-mplus">🏍️ Seguro Motos PLUS:</label>
                <input type="number" id="q-mplus" placeholder="0" value="0" oninput="calcular()">
            </div>
        </div>
        <label for="q-cel">📱 Seguro Celulares:</label>
        <input type="number" id="q-cel" placeholder="0" value="52" oninput="calcular()">

        <div class="grid-2">
            <div class="metrica-box">
                <div class="metrica-etiqueta">🔧 Servicios (GEX/Arm/Inst)</div>
                <div class="metrica-valor" id="res-p3-serv">$0.00</div>
            </div>
            <div class="metrica-box">
                <div class="metrica-etiqueta">🛡️ Seguros (Club/Motos/Cel)</div>
                <div class="metrica-valor" id="res-p3-seg">$0.00</div>
            </div>
        </div>
        <div class="metrica-box" style="margin-top: 10px;">
            <div class="metrica-etiqueta">💼 Total Comisiones Pilar 3</div>
            <div class="metrica-valor" id="res-p3-total">$0.00</div>
        </div>
    </div>

    <!-- Resultado Final -->
    <div class="result-card">
        <div class="result-title">🏆 TU INCENTIVO TOTAL DEL MES</div>
        <div class="result-total" id="total-incentivo">$0.00 MXN</div>
        <div class="result-breakdown" id="desglose-texto">Cargando desglose...</div>
    </div>

    <div class="footer">
        Calculadora Operativa de Incentivos
    </div>
</div>

<script>
    // Formateador de moneda para MXN
    const formater = new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' });

    function calcular() {
        const puesto = document.getElementById('puesto').value;
        const cumpEq = parseFloat(document.getElementById('cump-equipo').value) || 0;
        const montoOptica = parseFloat(document.getElementById('monto-optica').value) || 0;
        
        const cumpCredito = parseFloat(document.getElementById('cump-credito').value) || 0;
        const cumpDigital = parseFloat(document.getElementById('cump-digital').value) || 0;
        const cumpTienda = parseFloat(document.getElementById('cump-tienda').value) || 0;

        const qGex = parseInt(document.getElementById('q-gex').value) || 0;
        const qArm = parseInt(document.getElementById('q-arm').value) || 0;
        const qInst = parseInt(document.getElementById('q-inst').value) || 0;
        const qClub = parseInt(document.getElementById('q-club').value) || 0;
        const qMrc = parseInt(document.getElementById('q-mrc').value) || 0;
        const qMplus = parseInt(document.getElementById('q-mplus').value) || 0;
        const qCel = parseInt(document.getElementById('q-cel').value) || 0;

        // Mostrar / Ocultar campo especial Óptica
        document.getElementById('campo-optica-monto').style.display = (puesto === 'optometrista') ? 'block' : 'none';

        // -------------------------------------------------------------
        // PILAR 1: VENTA DE EQUIPO
        // -------------------------------------------------------------
        let incP1 = 0;
        let umbralMin = 85;
        let p1ChipText = "";
        let p1ChipClass = "chip-green";

        if (puesto === 'asesor') {
            umbralMin = 85;
            if (cumpEq < 85) { incP1 = 0; p1ChipText = "❌ < 85% — Sin pago base"; p1ChipClass = "chip-red"; }
            else if (cumpEq < 90) { incP1 = 250; p1ChipText = "⚠️ Cumplimiento Parcial (85%-89%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 95) { incP1 = 500; p1ChipText = "⚠️ Cumplimiento Parcial (90%-94%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 100) { incP1 = 850; p1ChipText = "⚠️ Cumplimiento Parcial (95%-99%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 110) { incP1 = 1300; p1ChipText = "✅ Meta Alcanzada (100%-109%)"; }
            else if (cumpEq < 120) { incP1 = 1650; p1ChipText = "✅ Sobremeta (110%-119%)"; }
            else { incP1 = 2000; p1ChipText = "✅ Máximo Cumplimiento (≥120%)"; }
        } 
        else if (puesto === 'telefonia') {
            umbralMin = 90;
            if (cumpEq < 90) { incP1 = 0; p1ChipText = "❌ < 90% — Sin pago base"; p1ChipClass = "chip-red"; }
            else if (cumpEq < 95) { incP1 = 900; p1ChipText = "⚠️ Cumplimiento Parcial (90%-94%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 100) { incP1 = 1100; p1ChipText = "⚠️ Cumplimiento Parcial (95%-99%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 110) { incP1 = 1450; p1ChipText = "✅ Meta Alcanzada (100%-109%)"; }
            else if (cumpEq < 120) { incP1 = 1750; p1ChipText = "✅ Sobremeta (110%-119%)"; }
            else { incP1 = 2100; p1ChipText = "✅ Máximo Cumplimiento (≥120%)"; }
        } 
        else if (puesto === 'optometrista') {
            umbralMin = 80;
            if (montoOptica < 45000) {
                incP1 = 0; p1ChipText = "❌ Venta Óptica < $45,000 — Sin pago base"; p1ChipClass = "chip-red";
            } else if (cumpEq < 80) {
                incP1 = 0; p1ChipText = "❌ < 80% — Sin pago base"; p1ChipClass = "chip-red";
            } else if (cumpEq < 90) { incP1 = 500; p1ChipText = "⚠️ Cumplimiento Parcial (80%-89%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 95) { incP1 = 900; p1ChipText = "⚠️ Cumplimiento Parcial (90%-94%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 100) { incP1 = 1200; p1ChipText = "⚠️ Cumplimiento Parcial (95%-99%)"; p1ChipClass = "chip-yellow"; }
            else if (cumpEq < 110) { incP1 = 1600; p1ChipText = "✅ Meta Alcanzada (100%-109%)"; }
            else if (cumpEq < 120) { incP1 = 1900; p1ChipText = "✅ Sobremeta (110%-119%)"; }
            else { incP1 = 2300; p1ChipText = "✅ Máximo Cumplimiento (≥120%)"; }
        }

        document.getElementById('chip-pilar1').innerHTML = `<span class="chip ${p1ChipClass}">${p1ChipText}</span>`;
        document.getElementById('res-p1').innerText = formater.format(incP1);

        // -------------------------------------------------------------
        // PILAR 2: VENTA GRUPAL
        // -------------------------------------------------------------
        let incCredito = (cumpCredito >= 90) ? 150 : 0;
        let incDigital = (cumpDigital >= 90) ? 150 : 0;
        let incTienda = (cumpTienda >= 100) ? 300 : 0;
        let incP2 = incCredito + incDigital + incTienda;

        let chipsP2Html = "";
        chipsP2Html += `<span class="chip ${incCredito > 0 ? 'chip-green' : 'chip-red'}">${incCredito > 0 ? '✅ Crédito ≥90% (+$150)' : '❌ Crédito <90% (+$0)'}</span> `;
        chipsP2Html += `<span class="chip ${incDigital > 0 ? 'chip-green' : 'chip-red'}">${incDigital > 0 ? '✅ Digital ≥90% (+$150)' : '❌ Digital <90% (+$0)'}</span> `;
        chipsP2Html += `<span class="chip ${incTienda > 0 ? 'chip-green' : 'chip-red'}">${incTienda > 0 ? '✅ Tienda ≥100% (+$300)' : '❌ Tienda <100% (+$0)'}</span>`;
        
        document.getElementById('chips-pilar2').innerHTML = chipsP2Html;
        document.getElementById('res-p2').innerText = formater.format(incP2);

        // -------------------------------------------------------------
        // PILAR 3: COMISIONES POR UNIDAD
        // -------------------------------------------------------------
        let incP3 = 0;
        let tServ = 0;
        let tSeg = 0;
        let habilitadoP3 = (cumpEq >= umbralMin) && (puesto !== 'optometrista' || montoOptica >= 45000);

        if (!habilitadoP3) {
            document.getElementById('chip-pilar3-status').innerHTML = `<span class="chip chip-red">❌ Requisito de Equipo No Cumplido — Comisiones Bloqueadas</span>`;
        } else {
            let esTop = (cumpEq >= 100);
            document.getElementById('chip-pilar3-status').innerHTML = `<span class="chip ${esTop ? 'chip-green' : 'chip-yellow'}">${esTop ? '✅ Tasas Máximas Activas (Equipo ≥100%)' : '⚠️ Tasas Básicas Activas'}</span>`;

            let mGex = esTop ? 30 : 15;
            let mArm = esTop ? 15 : 10;
            let mInst = esTop ? 70 : 40;
            let mClub = esTop ? 3.0 : 1.5;
            let mMrc = esTop ? 40 : 25;
            let mMplus = esTop ? 90 : 50;
            let mCel = esTop ? 10 : 5;

            tServ = (qGex * mGex) + (qArm * mArm) + (qInst * mInst);
            tSeg = (qClub * mClub) + (qMrc * mMrc) + (qMplus * mMplus) + (qCel * mCel);
            incP3 = tServ + tSeg;
        }

        document.getElementById('res-p3-serv').innerText = formater.format(tServ);
        document.getElementById('res-p3-seg').innerText = formater.format(tSeg);
        document.getElementById('res-p3-total').innerText = formater.format(incP3);

        // -------------------------------------------------------------
        // TOTAL Y DESGLOSE
        // -------------------------------------------------------------
        const totalFinal = incP1 + incP2 + incP3;
        
        document.getElementById('total-incentivo').innerText = formater.format(totalFinal) + " MXN";
        document.getElementById('desglose-texto').innerHTML = `Pilar 1 (Equipo): <b>${formater.format(incP1)}</b> | Pilar 2 (Grupal): <b>${formater.format(incP2)}</b> | Pilar 3 (Comisiones): <b>${formater.format(incP3)}</b>`;
    }

    // Ejecutar al cargar la pantalla
    window.onload = calcular;
</script>

</body>
</html>
