name: Generate Snake

on:
  # Se ejecuta automáticamente cada 12 horas
  schedule:
    - cron: "0 */12 * * *"
  
  # Permite ejecutarlo manualmente desde la pestaña "Actions" en GitHub
  workflow_dispatch:
  
  # Se activa cada vez que haces un push a la rama principal
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      # Genera los archivos SVG de la serpiente (modo claro y modo oscuro)
      - name: Generate github-contribution-grid-snake.svg
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      # Sube los archivos generados a una rama llamada 'output'
      - name: Push snake to output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
