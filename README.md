# Sudoku Solver

## Setup
```sh
python3 -m venv sudoku-venv
source sudoku-venv/bin/activate
pip3 install -r requirements.txt
```

## Running the solver
The sudoku being solved must be at minimum 2 rows, at maximum 100.
The sudoku starting point must be defined in a json file, an example is found in `schemas/example.json`.
By default this is the template used, it can be changed by specifying the file path at run time when executing the solver.

For the default example, 
```sh
python3 src/sudoku_solver.py
```

For a custom configuration, but a 3x3 sudoku
```sh
python3 src/sudoku_solver.py -m src/schemas/example.json
```

For a 9x9 sudoku
```sh
python3 src/sudoku_solver.py -size 9 -m src/schemas/example.json --strict-sudoku
```
The parameter `--strict-sudoku` enforces strict sudoku sub matrix rules.

For full details run
```sh
python3 src/sudoku_solver.py --help
```
