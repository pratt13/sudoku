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


## Examples
Example command, 
```sh
python src/sudoku_solver.py --size 9 -m src/schemas/example_hard_9x9.json --strict-sudoku
```

Example output
```sh
====================
Starting Matrix
 ̲  ̲  ̲  ̲  ̲  ̲  ̲  ̲  ̲ 
|̲5|̲?|̲?|̲?|̲2|̲?|̲?|̲?|̲?|
|̲8|̲3|̲1|̲?|̲?|̲?|̲?|̲?|̲?|
|̲6|̲?|̲?|̲?|̲5|̲9|̲?|̲?|̲?|
|̲?|̲?|̲7|̲?|̲?|̲?|̲?|̲5|̲?|
|̲?|̲?|̲?|̲7|̲4|̲?|̲9|̲?|̲?|
|̲?|̲1|̲?|̲?|̲?|̲?|̲6|̲?|̲?|
|̲?|̲?|̲?|̲5|̲?|̲?|̲?|̲3|̲8|
|̲?|̲?|̲?|̲?|̲?|̲3|̲?|̲?|̲?|
|̲?|̲?|̲6|̲?|̲?|̲8|̲?|̲?|̲1|
====================
====================
Solution: 1

Solution matrix
 ̲  ̲  ̲  ̲  ̲  ̲  ̲  ̲  ̲ 
|̲5|̲7|̲9|̲8|̲2|̲1|̲3|̲4|̲6|
|̲8|̲3|̲1|̲6|̲7|̲4|̲2|̲9|̲5|
|̲6|̲2|̲4|̲3|̲5|̲9|̲1|̲8|̲7|
|̲9|̲6|̲7|̲1|̲3|̲2|̲8|̲5|̲4|
|̲2|̲8|̲5|̲7|̲4|̲6|̲9|̲1|̲3|
|̲4|̲1|̲3|̲9|̲8|̲5|̲6|̲7|̲2|
|̲1|̲9|̲2|̲5|̲6|̲7|̲4|̲3|̲8|
|̲7|̲4|̲8|̲2|̲1|̲3|̲5|̲6|̲9|
|̲3|̲5|̲6|̲4|̲9|̲8|̲7|̲2|̲1|

********************
Statistics
  status   : OPTIMAL
  conflicts: 0
  branches : 0
  wall time: 0.014204235 s
  sol found: 1
********************
```