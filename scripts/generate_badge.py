import os

def generate_svg():
    """Genera la estructura SVG utilizando animaciones nativas SMIL compatibles con GitHub."""
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap');
            .bg { fill: #0a0a16; }
            .title { font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 22px; fill: #00ffff; letter-spacing: 2px; }
            .hud-text { font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 13px; fill: #ff00ff; }
        </style>
        
        <linearGradient id="grad-hud" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#12122c" stop-opacity="0.95"/>
            <stop offset="100%" stop-color="#050511" stop-opacity="0.98"/>
        </linearGradient>
    </defs>

    <!-- Fondo Cyberpunk -->
    <rect width="800" height="400" class="bg"/>
    
    <!-- Grid Cibernético -->
    <g stroke="#00ffff" stroke-opacity="0.08" stroke-width="1">
        <line x1="0" y1="100" x2="800" y2="100"/>
        <line x1="0" y1="200" x2="800" y2="200"/>
        <line x1="0" y1="300" x2="800" y2="300"/>
        <line x1="200" y1="0" x2="200" y2="400"/>
        <line x1="400" y1="0" x2="400" y2="400"/>
        <line x1="600" y1="0" x2="600" y2="400"/>
    </g>

    <!-- Panel HUD Principal -->
    <rect x="30" y="30" width="740" height="340" rx="15" fill="url(#grad-hud)" stroke="#00ffff" stroke-width="2"/>
    
    <!-- Encabezado HUD -->
    <text x="60" y="80" class="title">CYBER SPACE DEFENDER</text>
    <text x="620" y="80" class="hud-text">SECURITY: ACTIVE</text>
    <line x1="60" y1="95" x2="740" y2="95" stroke="#ff00ff" stroke-width="1.5" stroke-dasharray="5,5"/>

    <!-- Zona de Combate Central -->
    <g transform="translate(80, 180)">
        
        <!-- Grupo de la Nave y Láseres con Movimiento Vertical Nativo (SMIL) -->
        <g>
            <!-- La nave sube y baja de forma fluida cubriendo gran parte del eje vertical -->
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-55; 0,55; 0,0" dur="5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1; 0.4 0 0.6 1; 0.4 0 0.6 1"/>
            
            <!-- Nave Defensora -->
            <g>
                <polygon points="0,0 55,-15 55,15" fill="#00ffff" filter="drop-shadow(0 0 8px #00ffff)"/>
                <polygon points="12,-8 42,-3 42,3 12,8" fill="#1a1a3a" stroke="#ff00ff" stroke-width="1.5"/>
                <polygon points="5,-5 0,0 5,5" fill="#ff9900"/>
            </g>

            <!-- Láseres sincronizados saliendo de la punta -->
            <g transform="translate(55, 0)">
                <rect x="0" y="-2" width="60" height="4" fill="#00ff66" rx="2" filter="drop-shadow(0 0 6px #00ff66)">
                    <animate attributeName="opacity" values="0;1;1;0" dur="1.8s" repeatCount="indefinite"/>
                    <animate attributeName="transform" type="translate" values="0,0; 450,0" dur="1.8s" repeatCount="indefinite" calcMode="linear"/>
                </rect>
                <rect x="0" y="-2" width="60" height="4" fill="#00ff66" rx="2" filter="drop-shadow(0 0 6px #00ff66)">
                    <animate attributeName="opacity" values="0;1;1;0" begin="0.6s" dur="1.8s" repeatCount="indefinite"/>
                    <animate attributeName="transform" type="translate" values="0,0; 450,0" begin="0.6s" dur="1.8s" repeatCount="indefinite" calcMode="linear"/>
                </rect>
                <rect x="0" y="-2" width="60" height="4" fill="#00ff66" rx="2" filter="drop-shadow(0 0 6px #00ff66)">
                    <animate attributeName="opacity" values="0;1;1;0" begin="1.2s" dur="1.8s" repeatCount="indefinite"/>
                    <animate attributeName="transform" type="translate" values="0,0; 450,0" begin="1.2s" dur="1.8s" repeatCount="indefinite" calcMode="linear"/>
                </rect>
            </g>
        </g>

        <!-- Amenaza 1 (Hacker / Malware) -->
        <g transform="translate(480, -30)">
            <circle cx="0" cy="0" r="14" fill="#ff0055" filter="drop-shadow(0 0 10px #ff0055)"/>
            <circle cx="-4" cy="-3" r="3" fill="#ffffff"/>
            <circle cx="4" cy="-3" r="3" fill="#ffffff"/>
            <line x1="-8" y1="-8" x2="-2" y2="-2" stroke="#ff0055" stroke-width="2"/>
            <line x1="8" y1="-8" x2="2" y2="-2" stroke="#ff0055" stroke-width="2"/>
        </g>

        <!-- Amenaza 2 (Vulnerabilidad Crítica) -->
        <g transform="translate(560, 45)">
            <polygon points="0,-12 12,10 -12,10" fill="#ffcc00" filter="drop-shadow(0 0 10px #ffcc00)"/>
            <text x="-3" y="5" font-family="monospace" font-weight="900" font-size="12" fill="#0a0a16">!</text>
        </g>

        <!-- Amenaza 3 (Exploit / Inyección de Código) -->
        <g transform="translate(630, -45)">
            <rect x="-10" y="-10" width="20" height="20" rx="3" fill="#bd00ff" filter="drop-shadow(0 0 10px #bd00ff)"/>
            <text x="-7" y="5" font-family="'Orbitron', sans-serif" font-weight="700" font-size="10" fill="#ffffff">01</text>
        </g>

    </g>

    <!-- Barra de Estado Inferior -->
    <text x="60" y="340" fill="#8888aa" font-family="'Orbitron', sans-serif" font-size="10">STATUS: INTERCEPTING THREATS &amp; VULNERABILITIES // SYSTEM SECURE</text>
</svg>
'''
    return svg_content

if __name__ == "__main__":
    os.makedirs("dist", exist_ok=True)
    svg_data = generate_svg()
    file_path = "dist/space-defender.svg"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_data)
    
    print("¡SVG actualizado con animaciones nativas SMIL para movimiento vertical y láseres!")
