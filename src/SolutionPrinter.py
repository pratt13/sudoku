import math
from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, start_matrix, solution_matrix, solution_limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__solution_matrix = solution_matrix
        self.__solution_count = 0
        self.__solution_limit = solution_limit
        # Print the start matrix on init only
        print("=" * 20 + "\nStarting Matrix")
        self.pretty_print_matrix(
            [[str(value) if value is not None else "?" for value in row] for row in start_matrix]
        )
        print("=" * 20)

    def on_solution_callback(self):
        self.__solution_count += 1
        num_rows = int(math.sqrt(len(self.__solution_matrix)))
        print("=" * 20)
        print(f"Solution: {self.__solution_count}")

        print("\nSolution matrix")
        self.pretty_print_matrix(
            [
                [self.value(self.__solution_matrix[(i, j)]) for j in range(num_rows)]
                for i in range(num_rows)
            ]
        )

        if self.__solution_limit is not None and self.__solution_count >= self.__solution_limit:
            print(f"Stop search after {self.__solution_limit} solutions")
            self.stop_search()

    @property
    def solution_count(self):
        return self.__solution_count

    @staticmethod
    def pretty_print_matrix(matrix):
        print(" \u0332 ".join([""] * (1 + len(matrix[0]))))
        for row in matrix:
            print(f"|".join([""] + [f"\u0332{str(value)}" for value in row]) + "|")
