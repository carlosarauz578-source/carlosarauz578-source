name: Generate Snake Game

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

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
            output/github-contribution-grid-snake.svg
            output/github-contribution-grid-snake-dark.svg
