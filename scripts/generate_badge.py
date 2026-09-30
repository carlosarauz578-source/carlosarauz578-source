import os
import urllib.request
import json

def get_github_repos(username):
    """Consulta la cantidad de repositorios públicos desde la API de GitHub."""
    try:
        url = f"https://api.github.com/users/{username}"
        # Usar el token de GitHub si está disponible en el entorno de GitHub Actions
        headers = {'User-Agent': 'Python-Script'}
        token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
        if token:
            headers['Authorization'] = f'Bearer {token}'
            
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('public_repos', 0)
    except Exception as e:
        print(f"Error al obtener repositorios: {e}")
        return 12  # Valor por defecto

def generate_svg(repo_count):
    """Genera la estructura SVG con estilos CSS y animaciones integradas."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap');
            .bg {{ fill: #0a0a16; }}
            .title {{ font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 24px; fill: #00ffff; letter-spacing: 2px; }}
            .hud-text {{ font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 14px; fill: #ff00ff; }}
            .stat-val {{ font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 18px; fill: #00ff66; }}
            
            @keyframes pulse-glow {{
                0%, 100% {{ filter: drop-shadow(0 0 2px #00ffff); }}
                50% {{ filter: drop-shadow(0 0 10px #00ffff); }}
            }}
            @keyframes move-laser {{
                0% {{ transform: translateX(0); opacity: 1; }}
                100% {{ transform: translateX(700px); opacity: 0.8; }}
            }}
            @keyframes float-ship {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-8px); }}
            }}
            @keyframes enemy-move {{
                0% {{ transform: translateX(750px); }}
                100% {{ transform: translateX(-50px); }}
            }}
            
            .ship {{ animation: float-ship 3s ease-in-out infinite; }}
            .laser {{ animation: move-laser 1.2s linear infinite; }}
            .enemy {{ animation: enemy-move 6s linear infinite; }}
            .glow-box {{ animation: pulse-glow 2s infinite; }}
        </style>
        
        <linearGradient id="grad-hud" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#12122c" stop-opacity="0.9"/>
            <stop offset="100%" stop-color="#050511" stop-opacity="0.95"/>
        </linearGradient>
    </defs>

    <rect width="800" height="400" class="bg"/>
    
    <g stroke="#00ffff" stroke-opacity="0.1" stroke-width="1">
        <line x1="0" y1="100" x2="800" y2="100"/>
        <line x1="0" y1="200" x2="800" y2="200"/>
        <line x1="0" y1="300" x2="800" y2="300"/>
        <line x1="200" y1="0" x2="200" y2="400"/>
        <line x1="400" y1="0" x2="400" y2="400"/>
        <line x1="600" y1="0" x2="600" y2="400"/>
    </g>

    <rect x="30" y="30" width="740" height="340" rx="15" fill="url(#grad-hud)" stroke="#00ffff" stroke-width="2" class="glow-box"/>
    
    <text x="60" y="80" class="title">CYBER SPACE DEFENDER</text>
    <text x="600" y="80" class="hud-text">SYS.ONLINE</text>
    <line x1="60" y1="95" x2="740" y2="95" stroke="#ff00ff" stroke-width="1.5" stroke-dasharray="5,5"/>

    <g transform="translate(60, 130)">
        <rect x="0" y="0" width="200" height="80" rx="8" fill="#0a0a20" stroke="#00ff66" stroke-width="1"/>
        <text x="20" y="30" class="hud-text" font-size="12">PUBLIC REPOS</text>
        <text x="20" y="60" class="stat-val">{repo_count} REPOSITORIES</text>
    </g>

    <g transform="translate(300, 140)">
        <g class="ship" transform="translate(50, 40)">
            <polygon points="0,20 40,10 40,30" fill="#00ffff" filter="drop-shadow(0 0 5px #00ffff)"/>
            <polygon points="10,12 30,5 30,35 10,28" fill="#1a1a3a" stroke="#ff00ff" stroke-width="1.5"/>
            <polygon points="5,15 0,20 5,25" fill="#ff9900"/>
        </g>
        <rect x="100" y="57" width="40" height="3" fill="#00ff66" class="laser" rx="1.5"/>
        <g class="enemy" transform="translate(320, 35)">
            <circle cx="15" cy="15" r="12" fill="#ff0055" filter="drop-shadow(0 0 8px #ff0055)"/>
            <circle cx="11" cy="12" r="3" fill="#ffffff"/>
            <circle cx="19" cy="12" r="3" fill="#ffffff"/>
            <line x1="3" y1="3" x2="9" y2="9" stroke="#ff0055" stroke-width="2"/>
            <line x1="27" y1="3" x2="21" y2="9" stroke="#ff0055" stroke-width="2"/>
        </g>
    </g>

    <text x="60" y="340" fill="#8888aa" font-family="'Orbitron', sans-serif" font-size="10">STATUS: DEFENDING PERIMETER // REAL-TIME GITHUB SYNC</text>
</svg>'''

if __name__ == "__main__":
    os.makedirs("dist", exist_ok=True)
    
    # Usuario detectado en el contexto
    username = "carlosarauz578-source"
    repos = get_github_repos(username)
    
    svg_data = generate_svg(repos)
    file_path = "dist/space-defender.svg"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_data)
    
    print(f"SVG actualizado correctamente para {username}: {repos} repos.")
