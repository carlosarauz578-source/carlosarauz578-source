import os
import json
import urllib.request

# Consultar datos reales de tu perfil en la API pública de GitHub
username = "carlosarauz578-source"
api_url = f"https://api.github.com/users/{username}"

public_repos = 15  # Valor de respaldo predeterminado

try:
    req = urllib.request.Request(
        api_url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        public_repos = data.get("public_repos", 15)
except Exception as e:
    print(f"Aviso de sincronización de API: {e}")

os.makedirs("dist", exist_ok=True)

svg_content = f"""<svg width="950" height="260" viewBox="0 0 950 260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Filtros avanzados de neón y explosión -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="explosion-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes agentPatrol {{
      0% {{ transform: translate(50px, 125px); }}
      30% {{ transform: translate(380px, 125px); }}
      40% {{ transform: translate(380px, 125px); }} /* Planta la carga explosiva */
      55% {{ transform: translate(150px, 125px); }} /* Retrocede a zona segura */
      100% {{ transform: translate(50px, 125px); }}
    }}
    @keyframes bombPulse {{
      0%, 30% {{ opacity: 0; transform: scale(0); }}
      31% {{ opacity: 1; transform: scale(1); }}
      38% {{ opacity: 1; transform: scale(1.3); fill: #ff0055; }}
      40% {{ opacity: 1; transform: scale(0.9); }}
      42% {{ opacity: 1; transform: scale(1.4); }}
      45% {{ opacity: 0; transform: scale(0); }}
    }}
    @keyframes blastWave {{
      0%, 44% {{ opacity: 0; transform: scale(0); }}
      45% {{ opacity: 1; transform: scale(1); }}
      70% {{ opacity: 0.9; transform: scale(1.15); }}
      100% {{ opacity: 0; transform: scale(0); }}
    }}
    @keyframes vulnGlitch {{
      0%, 44% {{ opacity: 1; transform: translate(0,0); }}
      45% {{ opacity: 0; transform: translate(8px, -8px) scale(0.7); }}
      100% {{ opacity: 0; transform: translate(0,0); }}
    }}
    @keyframes matrixRain {{
      0% {{ opacity: 0.3; }}
      50% {{ opacity: 0.9; }}
      100% {{ opacity: 0.3; }}
    }}

    .agent {{ animation: agentPatrol 8s infinite cubic-bezier(0.4, 0, 0.2, 1); }}
    .bomb {{ animation: bombPulse 8s infinite; transform-origin: center; }}
    .explosion {{ animation: blastWave 8s infinite; transform-origin: center; }}
    .vuln {{ animation: vulnGlitch 8s infinite; transform-origin: center; }}
    .matrix-text {{ animation: matrixRain 2.5s infinite ease-in-out; }}
  </style>

  <!-- Fondo de Estación Táctica Principal -->
  <rect width="950" height="260" rx="16" fill="#020617" stroke="#1e293b" stroke-width="2.5"/>
  <rect x="18" y="18" width="914" height="224" rx="12" fill="none" stroke="#00ffcc" stroke-width="1.2" stroke-dasharray="8 6" opacity="0.25"/>

  <!-- Panel de Control Superior con Métricas Reales de la API -->
  <text x="35" y="42" fill="#00ffcc" font-family="'Courier New', monospace" font-size="14" font-weight="bold" filter="url(#neon-glow)">
    [SEC_OPS_COMMAND // TACTICAL_GRID_v5.0]
  </text>
  <text x="640" y="42" fill="#ff0055" font-family="'Courier New', monospace" font-size="12" font-weight="bold" class="matrix-text">
    LIVE_REPOS: {public_repos} SYNCED
  </text>

  <!-- Red Tablero / Nodos Conectados -->
  <g stroke="#1e293b" stroke-width="2">
    <line x1="60" y1="140" x2="890" y2="140" stroke="#00ffcc" stroke-width="3" opacity="0.35" stroke-dasharray="12 6"/>
    <line x1="220" y1="80" x2="220" y2="200" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
    <line x1="480" y1="80" x2="480" y2="200" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
    <line x1="720" y1="80" x2="720" y2="200" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
  </g>

  <!-- Nodos de Infraestructura Seguros -->
  <g fill="#090d16" stroke="#3b82f6" stroke-width="2">
    <rect x="195" y="105" width="50" height="50" rx="8"/>
    <rect x="695" y="105" width="50" height="50" rx="8"/>
  </g>
  <text x="207" y="135" fill="#3b82f6" font-family="monospace" font-size="11" font-weight="bold">CORE</text>
  <text x="705" y="135" fill="#3b82f6" font-family="monospace" font-size="11" font-weight="bold">FIRE</text>

  <!-- Sectores Vulnerables (Bugs / CVEs bajo asedio) -->
  <g class="vuln">
    <rect x="440" y="105" width="50" height="50" rx="8" fill="#111118" stroke="#ff0055" stroke-width="2"/>
    <text x="451" y="135" fill="#ff0055" font-family="monospace" font-size="12" font-weight="bold">CVE</text>
  </g>
  <g class="vuln">
    <rect x="500" y="105" width="50" height="50" rx="8" fill="#111118" stroke="#ff0055" stroke-width="2"/>
    <text x="510" y="135" fill="#ff0055" font-family="monospace" font-size="11" font-weight="bold">BUG</text>
  </g>

  <!-- Carga Explosiva / Payload con mecha parpadeante -->
  <g transform="translate(465, 118)" class="bomb">
    <circle cx="15" cy="15" r="12" fill="#030712" stroke="#ff0055" stroke-width="3"/>
    <path d="M 15,3 C 15,1 18,0 20,-1" fill="none" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="20" cy="-1" r="3" fill="#fbbf24" filter="url(#neon-glow)"/>
  </g>

  <!-- Onda Expansiva Neón masiva -->
  <g class="explosion" transform="translate(490, 130)" filter="url(#explosion-glow)">
    <rect x="-110" y="-16" width="220" height="32" rx="8" fill="#ff0055" opacity="0.85"/>
    <rect x="-16" y="-80" width="32" height="160" rx="8" fill="#ff0055" opacity="0.85"/>
    <rect x="-70" y="-10" width="140" height="20" rx="5" fill="#fbbf24"/>
    <rect x="-10" y="-50" width="20" height="100" rx="5" fill="#fbbf24"/>
  </g>

  <!-- Cyber-Bomberman (Agente Táctico Defensor Avanzado) -->
  <g class="agent">
    <g transform="translate(-18, -18)">
      <rect x="0" y="0" width="36" height="38" rx="9" fill="#00ffcc" filter="url(#neon-glow)"/>
      <rect x="5" y="9" width="26" height="13" rx="3" fill="#030712"/>
      <circle cx="18" cy="15.5" r="3.5" fill="#ff0055" filter="url(#neon-glow)"/>
      <text x="-10" y="-10" fill="#00ffcc" font-family="'Courier New', monospace" font-size="11" font-weight="bold">SOC_AGENT</text>
    </g>
  </g>

  <!-- Barra de Estado Inferior con Telemetría Conectada -->
  <rect x="35" y="200" width="880" height="28" rx="6" fill="#090d16" stroke="#1e293b" stroke-width="1.5"/>
  <text x="45" y="218" fill="#00ffcc" font-family="'Courier New', monospace" font-size="11">
    &gt; Telemetry_Feed: Live connection established. Public repos indexed: {public_repos}. Zero-day cluster neutralized.
  </text>
</svg>
"""

with open("dist/custom-security-animation.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
