import os

os.makedirs("dist", exist_ok=True)

svg_content = """<svg width="800" height="150" viewBox="0 0 800 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes scanPatrol {
        0% { transform: translateX(0px); }
        50% { transform: translateX(680px); }
        100% { transform: translateX(0px); }
      }
      @keyframes pulseGlow {
        0%, 100% { opacity: 0.8; }
        50% { opacity: 1; filter: drop-shadow(0 0 8px #00FF66); }
      }
      .scanner-unit { animation: scanPatrol 5s infinite ease-in-out; }
      .shield-glow { animation: pulseGlow 1.5s infinite; }
    </style>
  </defs>
  
  <!-- Fondo de consola táctica de ciberseguridad -->
  <rect width="800" height="150" rx="10" fill="#030712" stroke="#1f2937" stroke-width="2"/>
  
  <!-- Textos de estado HUD -->
  <text x="30" y="35" fill="#00FF66" font-family="'Courier New', monospace" font-size="13" font-weight="bold">
    [SEC-OPS_GRID]: Scanning vulnerabilities &amp; neutralizing threats in real-time...
  </text>
  
  <text x="30" y="125" fill="#00F7FF" font-family="'Courier New', monospace" font-size="11">
    &gt; Status: Firewall active // Zero-day vectors intercepted.
  </text>
  
  <!-- Carril / Línea de red de datos -->
  <line x1="40" y1="75" x2="760" y2="75" stroke="#1e293b" stroke-width="3" stroke-dasharray="6 4"/>

  <!-- Icono / Escudo de Ciberseguridad Animado que patrulla -->
  <g class="scanner-unit" transform="translate(40, 52)">
    <g class="shield-glow">
      <!-- Escudo Defensivo Vectorial -->
      <path d="M 0,0 L 16,-8 L 32,0 L 32,14 C 32,25 16,34 16,34 C 16,34 0,25 0,14 Z" fill="#00FF66"/>
      <!-- Icono interior (Candado / Núcleo seguro) -->
      <rect x="12" y="10" width="8" height="7" rx="1" fill="#030712"/>
      <path d="M 14,10 L 14,7 C 14,5.5 15,4.5 16,4.5 C 17,4.5 18,5.5 18,7 L 18,10" fill="none" stroke="#030712" stroke-width="1.5"/>
    </g>
    <!-- Etiqueta táctica sobre el escudo -->
    <text x="-12" y="-14" fill="#00FF66" font-family="'Courier New', monospace" font-size="10" font-weight="bold">🛡️ SOC_AGENT</text>
  </g>
</svg>
"""

with open("dist/custom-security-animation.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
