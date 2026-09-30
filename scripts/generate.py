import os

os.makedirs("dist", exist_ok=True)

svg_content = """<svg width="800" height="180" viewBox="0 0 800 180" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes moveBomberman {
        0% { transform: translateX(0px); }
        40% { transform: translateX(280px); }
        50% { transform: translateX(280px); } /* Se detiene a plantar bomba */
        100% { transform: translateX(0px); }
      }
      @keyframes bombFlash {
        0%, 100% { opacity: 0.3; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); fill: #FF0055; }
      }
      @keyframes explosion {
        0%, 45% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
        70% { opacity: 0.8; transform: scale(1.1); }
        100% { opacity: 0; transform: scale(0); }
      }
      @keyframes vulnDestroy {
        0%, 48% { opacity: 1; }
        52% { opacity: 0; }
        100% { opacity: 0; }
      }
      
      .bomberman { animation: moveBomberman 6s infinite ease-in-out; }
      .bomb { animation: bombFlash 1s infinite; transform-origin: center; }
      .blast-wave { animation: explosion 6s infinite; transform-origin: center; }
      .vulnerability { animation: vulnDestroy 6s infinite; }
    </style>
  </defs>
  
  <!-- Fondo de terminal estilo arcade / red -->
  <rect width="800" height="180" rx="12" fill="#030712" stroke="#1f2937" stroke-width="2"/>
  
  <!-- HUD Superior -->
  <text x="30" y="30" fill="#00FF66" font-family="'Courier New', monospace" font-size="12" font-weight="bold">
    [CYBER_BOMBERMAN]: SecOps_Protocol_v2.0 // Cleaning network blocks...
  </text>
  
  <!-- Cuadrícula / Laberinto de bloques de red y vulnerabilidades -->
  <g fill="#1e293b" stroke="#374151" stroke-width="2">
    <!-- Bloques estáticos del laberinto -->
    <rect x="120" y="70" width="30" height="30" rx="4"/>
    <rect x="220" y="70" width="30" height="30" rx="4"/>
    <rect x="420" y="70" width="30" height="30" rx="4"/>
    <rect x="520" y="70" width="30" height="30" rx="4"/>
    <rect x="620" y="70" width="30" height="30" rx="4"/>
  </g>

  <!-- Vulnerabilidades (Bloques rojos que van a estallar) -->
  <g class="vulnerability">
    <rect x="320" y="70" width="30" height="30" rx="4" fill="#FF0055" stroke="#ff3366"/>
    <text x="326" y="89" fill="#FFFFFF" font-family="monospace" font-size="11" font-weight="bold">BUG</text>
  </g>
  <g class="vulnerability">
    <rect x="370" y="70" width="30" height="30" rx="4" fill="#FF0055" stroke="#ff3366"/>
    <text x="374" y="89" fill="#FFFFFF" font-family="monospace" font-size="11" font-weight="bold">CVE</text>
  </g>

  <!-- Bomba plantada en el sector de vulnerabilidades -->
  <g transform="translate(285, 70)">
    <circle cx="15" cy="15" r="9" fill="#111827" stroke="#FF0055" stroke-width="2" class="bomb"/>
    <path d="M 15,6 C 15,3 18,2 19,1" fill="none" stroke="#FBBF24" stroke-width="2"/>
  </g>

  <!-- Onda Expansiva de la Bomba (Explosión en cruz limpiando el Bug) -->
  <g class="blast-wave" transform="translate(350, 85)">
    <!-- Cruz de explosión neón -->
    <rect x="-80" y="-12" width="160" height="24" rx="4" fill="#FF0055" opacity="0.8"/>
    <rect x="-12" y="-80" width="24" height="160" rx="4" fill="#FF0055" opacity="0.8"/>
    <rect x="-50" y="-8" width="100" height="16" rx="3" fill="#FBBF24"/>
    <rect x="-8" y="-50" width="16" height="100" rx="3" fill="#FBBF24"/>
  </g>

  <!-- Personaje (Cyber Bomberman / Analista Defensor) -->
  <g class="bomberman" transform="translate(50, 68)">
    <!-- Cuerpo / Casco del agente -->
    <rect x="0" y="0" width="28" height="32" rx="6" fill="#00FF66"/>
    <!-- Visor de seguridad tecnológico -->
    <rect x="4" y="8" width="20" height="10" rx="2" fill="#030712"/>
    <circle cx="14" cy="13" r="2" fill="#00F7FF"/>
    <text x="-4" y="-8" fill="#00FF66" font-family="monospace" font-size="9" font-weight="bold">BOMBER_SEC</text>
  </g>
  
  <!-- HUD Inferior de Estado -->
  <text x="30" y="150" fill="#00F7FF" font-family="'Courier New', monospace" font-size="11">
    &gt; Status: Deploying exploit-payloads to clear vulnerability clusters.
  </text>
</svg>
"""

with open("dist/custom-security-animation.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
