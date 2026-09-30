<!-- Radar orbital avanzado con cambio de color -->
<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Fondo -->
  <circle cx="150" cy="150" r="140" fill="black" stroke="lime" stroke-width="2"/>
  
  <!-- Líneas de cuadrícula -->
  <circle cx="150" cy="150" r="40" fill="none" stroke="lime" stroke-width="0.5"/>
  <circle cx="150" cy="150" r="80" fill="none" stroke="lime" stroke-width="0.5"/>
  <circle cx="150" cy="150" r="120" fill="none" stroke="lime" stroke-width="0.5"/>
  
  <!-- Línea giratoria (haz del radar) -->
  <line x1="150" y1="150" x2="150" y2="10" stroke="lime" stroke-width="2">
    <animateTransform attributeName="transform" attributeType="XML"
      type="rotate" from="0 150 150" to="360 150 150" dur="4s" repeatCount="indefinite"/>
  </line>
  
  <!-- Nodos de seguridad con cambio de color -->
  <circle cx="190" cy="80" r="10" fill="green">
    <animate attributeName="fill" values="green;red;green" dur="2s" repeatCount="indefinite"/>
  </circle>
  
  <circle cx="80" cy="200" r="10" fill="green">
    <animate attributeName="fill" values="green;red;green" dur="3s" repeatCount="indefinite"/>
  </circle>
  
  <circle cx="220" cy="220" r="10" fill="green">
    <animate attributeName="fill" values="green;red;green" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  
  <circle cx="100" cy="100" r="10" fill="green">
    <animate attributeName="fill" values="green;red;green" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  
  <!-- Íconos de seguridad encima de los nodos -->
  <text x="185" y="85" font-size="16">🔐</text>
  <text x="75" y="205" font-size="16">🛰️</text>
  <text x="215" y="225" font-size="16">🛡️</text>
  <text x="95" y="105" font-size="16">🚀</text>
</svg>
