import os

os.makedirs("dist", exist_ok=True)

svg_content = """<svg width="900" height="220" viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Filtros de brillo y neón avanzados -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <filter id="explosion-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes moveAgent {
      0% { transform: translate(60px, 110px); }
      35% { transform: translate(360px, 110px); }
      45% { transform: translate(360px, 110px); } /* Planta la carga */
      55% { transform: translate(120px, 110px); } /* Retrocede a zona segura */
      100% { transform: translate(60px, 110px); }
    }
    @keyframes bombCountdown {
      0%, 35% { opacity: 0; transform: scale(0); }
      36% { opacity: 1; transform: scale(1); }
      44% { opacity: 1; transform: scale(1.2); fill: #ff0055; }
      46% { opacity: 1; transform: scale(0.9); }
      48% { opacity: 1; transform: scale(1.3); }
      50% { opacity: 0; transform: scale(0); }
    }
    @keyframes blastWave {
      0%, 49% { opacity: 0; transform: scale(0); }
      50% { opacity: 1; transform: scale(1); }
      75% { opacity: 0.9; transform: scale(1.1); }
      100% { opacity: 0; transform: scale(0); }
    }
    @keyframes glitchVuln {
      0%, 49% { opacity: 1; transform: translate(0,0); }
      50% { opacity: 0; transform: translate(5px, -5px) scale(0.8); }
      100% { opacity: 0; transform: translate(0,0); }
    }
    @keyframes radarSweep {
      0% { opacity: 0.3; }
      50% { opacity: 0.8; }
      100% { opacity: 0.3; }
    }

    .sec-agent { animation: moveAgent 7s infinite cubic-bezier(0.4, 0, 0.2, 1); }
    .payload-bomb { animation: bombCountdown 7s infinite; transform-origin: center; }
    .blast-radius { animation: blastWave 7s infinite; transform-origin: center; }
    .vuln-node { animation: glitchVuln 7s infinite; transform-origin: center; }
    .terminal-hud { animation: radarSweep 2s infinite ease-in-out; }
  </style>

  <!-- Fondo de Estación Táctica / Consola de Ciberseguridad -->
  <rect width="900" height="220" rx="14" fill="#030712" stroke="#1f2937" stroke-width="2"/>
  <rect x="15" y="15" width="870" height="190" rx="10" fill="none" stroke="#00ffcc" stroke-width="1" stroke-dasharray="6 4" opacity="0.3"/>

  <!-- HUD y Telemetría Superior -->
  <text x="35" y="42" fill="#00ffcc" font-family="'Courier New', monospace" font-size="13" font-weight="bold" filter="url(#neon-glow)">
    [CYBER_SEC_OPS // TACTICAL_GRID_v4.2]
  </text>
  <text x="650" y="42" fill="#ff0055" font-family="'Courier New', monospace" font-size="12" font-weight="bold" class="terminal-hud">
    STATUS: THREAT_PURGE
  </text>

  <!-- Red / Pasillo de Operaciones (Grid Layout) -->
  <g fill="none" stroke="#1e293b" stroke-width="2">
    <!-- Líneas de la Red de Firewall -->
    <line x1="45" y1="126" x2="855" y2="126" stroke="#00ffcc" stroke-width="3" opacity="0.4" stroke-dasharray="10 6"/>
    <!-- Guías verticales de nodos -->
    <line x1="200" y1="80" x2="200" y2="172" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
    <line x1="520" y1="80" x2="520" y2="172" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
    <line x1="700" y1="80" x2="700" y2="172" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
  </g>

  <!-- Obstáculos Estables de Red (Bloques seguros) -->
  <g fill="#0f172a" stroke="#3b82f6" stroke-width="2" rx="4">
    <rect x="180" y="96" width="40" height="40" rx="6"/>
    <rect x="500" y="96" width="40" height="40" rx="6"/>
    <rect x="680" y="96" width="40" height="40" rx="6"/>
  </g>
  <text x="190" y="121" fill="#3b82f6" font-family="monospace" font-size="10" font-weight="bold">NET</text>
  <text x="510" y="121" fill="#3b82f6" font-family="monospace" font-size="10" font-weight="bold">IDS</text>
  <text x="690" y="121" fill="#3b82f6" font-family="monospace" font-size="10" font-weight="bold">WAF</text>

  <!-- Vulnerabilidades / Amenazas (Bloques que serán destruidos por la explosión) -->
  <g class="vuln-node">
    <!-- CVE Target 1 -->
    <rect x="420" y="96" width="40" height="40" rx="6" fill="#1f1d2b" stroke="#ff0055" stroke-width="2"/>
    <text x="428" y="121" fill="#ff0055" font-family="monospace" font-size="11" font-weight="bold">CVE</text>
  </g>
  <g class="vuln-node">
    <!-- Malware Target 2 -->
    <rect x="470" y="96" width="40" height="40" rx="6" fill="#1f1d2b" stroke="#ff0055" stroke-width="2"/>
    <text x="478" y="121" fill="#ff0055" font-family="monospace" font-size="10" font-weight="bold">BUG</text>
  </g>

  <!-- Carga Explosiva / Payload de Neutralización (Plantada en la zona de CVEs) -->
  <g transform="translate(445, 106)" class="payload-bomb">
    <circle cx="15" cy="15" r="11" fill="#0b0f19" stroke="#ff0055" stroke-width="2.5"/>
    <path d="M 15,4 C 15,2 18,1 20,0" fill="none" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="20" cy="0" r="2.5" fill="#fbbf24" filter="url(#neon-glow)"/>
  </g>

  <!-- Onda Expansiva Táctica (Limpieza de Vulnerabilidades en Cruz) -->
  <g class="blast-radius" transform="translate(465, 116)" filter="url(#explosion-glow)">
    <rect x="-90" y="-14" width="180" height="28" rx="6" fill="#ff0055" opacity="0.85"/>
    <rect x="-14" y="-70" width="28" height="140" rx="6" fill="#ff0055" opacity="0.85"/>
    <rect x="-60" y="-8" width="120" height="16" rx="4" fill="#fbbf24"/>
    <rect x="-8" y="-45" width="16" height="90" rx="4" fill="#fbbf24"/>
  </g>

  <!-- Agente Defensor (Cyber-Bomberman con armadura y visor neón) -->
  <g class="sec-agent">
    <g transform="translate(-16, -16)">
      <!-- Cuerpo del Agente -->
      <rect x="0" y="0" width="32" height="34" rx="8" fill="#00ffcc" filter="url(#neon-glow)"/>
      <!-- Casco / Visor Táctico -->
      <rect x="4" y="8" width="24" height="12" rx="3" fill="#030712"/>
      <circle cx="16" cy="14" r="3" fill="#ff0055" filter="url(#neon-glow)"/>
      <!-- Etiqueta de Identificación -->
      <text x="-12" y="-8" fill="#00ffcc" font-family="'Courier New', monospace" font-size="10" font-weight="bold">DEFENDER_AI</text>
    </g>
  </g>

  <!-- Barra de Estado Inferior con Telemetría en Vivo -->
  <rect x="35" y="165" width="830" height="24" rx="5" fill="#0b0f19" stroke="#1f2937" stroke-width="1.5"/>
  <text x="45" y="181" fill="#00ffcc" font-family="'Courier New', monospace" font-size="11">
    &gt; System_Log: Payload deployed successfully. Zero-day cluster neutralized in sector 4.
  </text>
</svg>
"""

with open("dist/custom-security-animation.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
