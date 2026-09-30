import os

# Crear carpeta de distribución si no existe
os.makedirs("dist", exist_ok=True)

# Aquí defines el contenido de tu animación SVG personalizada
svg_content = """<svg width="800" height="150" viewBox="0 0 800 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes scan {
        0% { transform: translateX(0px); }
        50% { transform: translateX(650px); }
        100% { transform: translateX(0px); }
      }
      .scanner-icon { animation: scan 4s infinite ease-in-out; }
    </style>
  </defs>
  
  <!-- Fondo de terminal -->
  <rect width="800" height="150" rx="8" fill="#030712" stroke="#1f2937" stroke-width="2"/>
  <text x="30" y="40" fill="#00FF66" font-family="monospace" font-size="14" font-weight="bold">
    [SEC-OPS_GRID]: Scanning vulnerabilities &amp; neutralizing threats...
  </text>
  
  <!-- Línea de patrullaje de red -->
  <line x1="50" y1="90" x2="750" y2="90" stroke="#1e293b" stroke-width="4" stroke-dasharray="8 4"/>

  <!-- Icono / Escudo de Seguridad Animado -->
  <g class="scanner-icon" transform="translate(50, 70)">
    <!-- Escudo Defensivo -->
    <path d="M 0,0 L 20,-10 L 40,0 L 40,15 C 40,30 20,40 20,40 C 20,40 0,30 0,15 Z" fill="#00FF66" opacity="0.9"/>
    <!-- Candado o visor central -->
    <circle cx="20" cy="12" r="5" fill="#030712"/>
    <text x="-15" y="-15" fill="#00F7FF" font-family="monospace" font-size="10">🛡️ SOC_AGENT</text>
  </g>
</svg>
"""

# Guardar el archivo SVG generado en la carpeta dist/
with open("dist/custom-security-animation.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
