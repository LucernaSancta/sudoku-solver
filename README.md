# Sudoku Solver

A python script that solves sudokus using back propagation

# Quick start

Just execute the main file
```bash
python main.py
```

## Customizations

To customize the sudoku solver you can modify tha constants at the start
of the `main.py` file
```python
# in main.py

FILE_PATH = 'example.csv'
ACTIVATE_GUI = True
FPS = 10
```

## Warning

The script is extremly slow and it is used only for graphical demostrations,
to use this script as efficently as possilbe set the `ACTIVATE_GUI` in the `main.py` file to `False`
```python
ACTIVATE_GUI = False
```

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