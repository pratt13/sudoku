"""
Entrypoint for the sudoku solver
"""

import argparse, os, sys

from exceptions import InvalidInputSudoku


current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)


from constants import SCHEMA
from solver import SudokuSolver
from utils import is_square, json_parser, validate_json

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A program to solve a sudoku given the starting matrix"
    )
    parser.add_argument(
        "--size",
        "-s",
        default="3",
        help="The number of rows/columns in the sudoku matrix",
        type=int,
    )
    parser.add_argument(
        "--starting-matrix",
        "-m",
        type=str,
        default="src/schemas/example.json",
        help="The location of the JSON file that defines the starting matrix. "
        + "It must conform to the src/schemas/schema.json",
    )
    parser.add_argument(
        "--strict-sudoku",
        action="store_true",
        help="Whether to do a strict sudoku or not. For this to work, "
        + "it must be a square grid, so each sub-matrix contains 1 to number of rows.",
    )
    args = parser.parse_args()

    # Validate input file
    input_obj = json_parser(args.starting_matrix)
    schema = json_parser(SCHEMA)
    validate_json(schema, input_obj)

    # VaLidate square matrix if strict-sudoku is true
    if args.strict_sudoku and not is_square(args.size):
        raise ValueError(
            f"The strict sudoku constraint is set but {args.size} is nto a square number"
        )

    # Run the solver
    input_matrix = input_obj.get("matrix", [])
    try:
        solver = SudokuSolver(args.size, input_matrix, args.strict_sudoku)
        solver.solver()
    except InvalidInputSudoku as e:
        print(f"FAILURE: Invalid input matrix: {repr(e)}")
