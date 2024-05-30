from ortools.sat.python import cp_model

from SolutionPrinter import VarArraySolutionPrinter


class SudokuSolver:
    def __init__(self, num_rows, input_matrix):
        self.num_rows = num_rows
        self.input_matrix = input_matrix

    @property
    def input_matrix(self):
        return self.__input_matrix

    @input_matrix.setter
    def input_matrix(self, value):
        self.validate_input_matrix(value, self.num_rows)
        self.__input_matrix = value

    @staticmethod
    def is_valid_matrix(matrix, num_rows):
        """
        Is a valid matrix
        * Every row/column has the numbers 1-num_rows in
        * Every row/column has no duplicates
        """
        numbers = [idx for idx in range(1, num_rows + 1)]
        columns = zip(*matrix)
        return not (
            any(number not in row for row in matrix for number in numbers)
            or any(number not in column for column in columns for number in numbers)
            or any(len(set(row)) != num_rows for row in matrix)
            or any(len(set(column)) != num_rows for column in columns)
        )

    @staticmethod
    def validate_input_matrix(matrix, num_rows):
        """
        Validate the matrix that is given.
        If the number of rows are 9, then there must be a 9x9 array
        """
        numbers = [idx for idx in range(1, 1 + num_rows)]
        columns = zip(*matrix)
        if len(matrix) != num_rows:
            raise ValueError(f"Input array should be {num_rows} x {num_rows}")
        elif any(len(sublist) != num_rows for sublist in matrix):
            raise ValueError(f"Input array should be {num_rows} x {num_rows}")
        elif any(el not in numbers + [None] for sublist in matrix for el in sublist):
            raise ValueError(f"Input element need to contain {numbers + [None]}")
        # FIlter Nones
        filtered_matrix = [[el for el in sublist if el is not None] for sublist in matrix]
        columns = zip(*filtered_matrix)
        if any(len(set(row)) != len(row) for row in filtered_matrix) or any(
            len(set(column)) != len(column) for column in columns
        ):
            raise ValueError(f"Must not contain duplicates")

    def construct_sudoku_constraint(self, num_rows, matrix_template):
        """
        Method to initialise the sudoku matrix,
        add the standard sudoku constraints (standard)
        and the constraints from the given matrix.
        """
        # Validate inputs
        self.validate_input_matrix(matrix_template, num_rows)

        # Initialise model
        model = cp_model.CpModel()
        # Initialise matrix for the sudoku constraint
        # Indexes start from 0, as is usual for python
        sudoku_matrix = {}
        for i in range(num_rows):
            for j in range(num_rows):
                sudoku_matrix[(i, j)] = model.new_int_var(1, num_rows, f"({i}_{j})")
        row_total = sum(range(1, num_rows + 1))
        # Conditions that matrix should sum values
        for i in range(num_rows):
            # Conditions that matrix should sum values
            model.add(sum(sudoku_matrix[(i, j)] for j in range(num_rows)) == row_total)
            model.add(sum(sudoku_matrix[(j, i)] for j in range(num_rows)) == row_total)
            # Unique element on each row/column
            for j in range(num_rows):
                for k in range(num_rows):
                    if j != k:
                        model.add(sudoku_matrix[(i, j)] != sudoku_matrix[(i, k)])
                        model.add(sudoku_matrix[(j, i)] != sudoku_matrix[(k, i)])

        # Constraints from starting point
        for i in range(num_rows):
            for j in range(num_rows):
                if matrix_template[i][j]:
                    model.add(matrix_template[i][j] == sudoku_matrix[(i, j)])

        return model, sudoku_matrix

    def solver(self):
        model, sudoku_matrix = self.construct_sudoku_constraint(self.num_rows, self.input_matrix)
        # Creates a solver and solves the model.
        solver = cp_model.CpSolver()
        solution_printer = VarArraySolutionPrinter(self.input_matrix, sudoku_matrix)
        # Enumerate all solutions.
        solver.parameters.enumerate_all_solutions = True
        # Solve.
        status = solver.solve(model, solution_printer)

        # Statistics.
        print("\nStatistics")
        print(f"  status   : {solver.status_name(status)}")
        print(f"  conflicts: {solver.num_conflicts}")
        print(f"  branches : {solver.num_branches}")
        print(f"  wall time: {solver.wall_time} s")
        print(f"  sol found: {solution_printer.solution_count}")


solver = SudokuSolver(3, [[1, 2, 3], [2, 3, 1], [3, None, None]])
solver.solver()
