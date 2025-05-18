# Sudoku Solver

A python script that solves sudokus using back propagation

# Quick start

The general start command is
```bash
python main.py [-flag(s)]
```

## Flags

| Flag | descriptios | example |
| --- | --- | --- |
| `-i [path]` | Import a sudoku form an existing CSV file | `python main.py -i example.csv` |

## How it works

The algoritm creates two arrays, one with the original values and the other with the current attemp,
an index is used to keep track of the value that is currently beeing changed,
if the index is inside a cell with an original value than that cell is skipped,
otherwise the value of the cell is incremented by one and the validity of the current configuration is checked.

## Repo structure

| File | Description |
| --- | --- |
| `main.py` | main executable |
| `sudoku.py` | responsible for sudoku checking and value storing |
| `window.py` | responsible for GUIs and visualizations |