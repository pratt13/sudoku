import math
from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, start_matrix, solution_matrix):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__start_matrix = start_matrix
        self.__solution_matrix = solution_matrix
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        num_rows = int(math.sqrt(len(self.__solution_matrix)))
        print("=" * 10)
        print(f"Solution: {self.__solution_count}")
        print("\nStart matrix")
        for i in range(num_rows):
            print(
                ",".join(
                    [
                        str(self.__start_matrix[i][j])
                        if self.__start_matrix[i][j] is not None
                        else "?"
                        for j in range(num_rows)
                    ]
                )
            )
        print("\nSolution matrix")
        for i in range(num_rows):
            print(
                ",".join([str(self.value(self.__solution_matrix[(i, j)])) for j in range(num_rows)])
            )

    @property
    def solution_count(self):
        return self.__solution_count