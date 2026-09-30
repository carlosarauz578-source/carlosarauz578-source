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
    <!-- Filtros de brillo espacial y láseres neón -->
    <filter id="neon-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="laser-beam" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes shipHover {{
      0%, 100% {{ transform: translate(60px, 110px); }}
      50% {{ transform: translate(75px, 95px); }}
    }}
    @keyframes laserShot {{
      0%, 20% {{ opacity: 0; transform: scaleX(0); }}
      25% {{ opacity: 1; transform: scaleX(1); }}
      30% {{ opacity: 0; transform: scaleX(0); }}
      50%, 70% {{ opacity: 0; transform: scaleX(0); }}
      75% {{ opacity: 1; transform: scaleX(1); }}
      80% {{ opacity: 0; transform: scaleX(0); }}
      100% {{ opacity: 0; transform: scaleX(0); }}
    }}
    @keyframes targetDestroyed {{
      0%, 25% {{ opacity: 1; transform: translate(0, 0) scale(1); }}
      28% {{ opacity: 0; transform: translate(20px, -10px) scale(0.4) rotate(45deg); }}
      70% {{ opacity: 1; transform: translate(0, 0) scale(1); }}
      73% {{ opacity: 0; transform: translate(20px, 10px) scale(0.4) rotate(-45deg); }}
      100% {{ opacity: 1; transform: translate(0, 0) scale(1); }}
    }}
    @keyframes starTwinkle {{
      0%, 100% {{ opacity: 0.2; }}
      50% {{ opacity: 0.9; }}
    }}

    .defender-ship {{ animation: shipHover 4s infinite ease-in-out; transform-origin: center; }}
    .laser-fire {{ animation: laserShot 4s infinite linear; transform-origin: left center; }}
    .enemy-target {{ animation: targetDestroyed 4s infinite ease-in-out; transform-origin: center; }}
    .star-1 {{ animation: starTwinkle 2s infinite ease-in-out; }}
    .star-2 {{ animation: starTwinkle 3.5s infinite ease-in-out; }}
  </style>

  <!-- Fondo de Espacio Profundo / Ciberespacio -->
  <rect width="950" height="260" rx="16" fill="#010409" stroke="#1f2937" stroke-width="2.5"/>
  
  <!-- Campo de Estrellas (Starfield de fondo) -->
  <g fill="#ffffff">
    <circle cx="120" cy="50" r="1.5" class="star-1"/>
    <circle cx="340" cy="40" r="2" class="star-2"/>
    <circle cx="580" cy="60" r="1" class="star-1"/>
    <circle cx="820" cy="45" r="2" class="star-2"/>
    <circle cx="210" cy="210" r="1.5" class="star-2"/>
    <circle cx="450" cy="220" r="2" class="star-1"/>
    <circle cx="750" cy="205" r="1" class="star-1"/>
  </g>

  <!-- HUD Táctico Superior -->
  <text x="35" y="38" fill="#00ffcc" font-family="'Courier New', monospace" font-size="14" font-weight="bold" filter="url(#neon-glow)">
    [SPACE_DEFENDER // SEC_INTERCEPTOR_v6.0]
  </text>
  <text x="630" y="38" fill="#ff0055" font-family="'Courier New', monospace" font-size="12" font-weight="bold">
    REPOS_INDEXED: {public_repos}
  </text>

  <!-- Líneas de radar / cuadrícula espacial -->
  <line x1="35" y1="140" x2="915" y2="140" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="6 6"/>

  <!-- Amenazas Espaciales (Virus, CVEs, Hackers interceptados) -->
  <!-- Objetivo 1: VIRUS -->
  <g class="enemy-target" transform="translate(560, 95)">
    <rect x="0" y="0" width="65" height="40" rx="6" fill="#0d1117" stroke="#ff0055" stroke-width="2"/>
    <text x="12" y="25" fill="#ff0055" font-family="monospace" font-size="12" font-weight="bold">VIRUS</text>
  </g>

  <!-- Objetivo 2: CVE-BUG -->
  <g class="enemy-target" transform="translate(720, 95)">
    <rect x="0" y="0" width="65" height="40" rx="6" fill="#0d1117" stroke="#ff0055" stroke-width="2"/>
    <text x="14" y="25" fill="#ff0055" font-family="monospace" font-size="12" font-weight="bold">EXPLOIT</text>
  </g>

  <!-- Rayos Láser disparados por la nave -->
  <g class="laser-fire" transform="translate(145, 122)">
    <rect x="0" y="0" width="430" height="4" rx="2" fill="#00ffcc" filter="url(#laser-beam)"/>
    <rect x="0" y="1" width="430" height="2" rx="1" fill="#ffffff"/>
  </g>
  <g class="laser-fire" transform="translate(145, 138)">
    <rect x="0" y="0" width="430" height="4" rx="2" fill="#00ffcc" filter="url(#laser-beam)"/>
    <rect x="0" y="1" width="430" height="2" rx="1" fill="#ffffff"/>
  </g>

  <!-- Nave Espacial Defensora (Cyber Interceptor) -->
  <g class="defender-ship">
    <g transform="translate(-25, -20)">
      <!-- Estela de propulsión de la nave -->
      <path d="M -15,14 L -45,10 L -45,22 Z" fill="#ff5500" filter="url(#neon-glow)"/>
      <path d="M -15,16 L -30,16 Z" fill="#ffff00"/>
      
      <!-- Cuerpo principal de la nave -->
      <polygon points="0,5 50,16 0,27 12,16" fill="#00ffcc" filter="url(#neon-glow)"/>
      <polygon points="10,12 35,16 10,20" fill="#030712"/>
      
      <!-- Cabina de piloto (Cockpit) -->
      <ellipse cx="22" cy="16" rx="7" ry="4" fill="#ff0055" filter="url(#neon-glow)"/>
      
      <!-- Etiqueta de la nave -->
      <text x="2" y="-6" fill="#00ffcc" font-family="'Courier New', monospace" font-size="10" font-weight="bold">INTERCEPTOR</text>
    </g>
  </g>

  <!-- Panel de Telemetría Inferior -->
  <rect x="35" y="200" width="880" height="28" rx="6" fill="#0d1117" stroke="#1f2937" stroke-width="1.5"/>
  <text x="45" y="218" fill="#00ffcc" font-family="'Courier New', monospace" font-size="11">
    &gt; System_Log: Defensive cannons active. Eradicating incoming zero-day anomalies &amp; malware strains.
  </text>
</svg>
"""

with open("dist/custom-security-animation.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
