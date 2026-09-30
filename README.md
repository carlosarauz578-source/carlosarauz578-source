name: Generate Snake Game

on:
  schedule:
    - cron: "0 0 * * *"   # corre cada día a medianoche
  workflow_dispatch:       # permite ejecutarlo manualmente

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Generate Snake Graph
        uses: Platane/snk@master
        with:
          github_user_name: carlosarauz578-source
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg
