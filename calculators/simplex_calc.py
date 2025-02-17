class Task:
    def __init__(self):
        self.var_names = []  # Variable names
        self.objective_function = []  # Coefficients of the objective function
        self.constraints = []  # List of constraint coefficient lists
        self.rhs_values = []  # Right-hand side values

class SimplexCalc:
    def read_task_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found!")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        task = Task()
        # First line: Variable names
        task.var_names = lines[0].split()
        # Second line: Objective function coefficients
        objective_line = lines[1].split()
        task.objective_function = list(map(float, objective_line[:-1]))
        # Remaining lines: Constraints (Ax = b)
        for line in lines[2:]:
            parts = line.split("=")
            if len(parts) != 2:
                print(f"Error parsing constraint: {line}")
                return None
            coefficients = list(map(float, parts[0].split()))
            rhs_value = float(parts[1].strip())
            task.constraints.append(coefficients)
            task.rhs_values.append(rhs_value)
        return task
    
    @staticmethod
    def check_only_zeros(task, column, skip_row):
        """ Checks if all elements in the given column (except for the specified skip_row) are zero."""
        for i in range(len(task.constraints)):
            if i == skip_row:
                continue
            if task.constraints[i][column] != 0:
                return False
        return True
    
    def get_basis(self, task):
        """ Identifies basis variables in the constraints matrix and returns their indices. """
        basis = []
        for i, constraint in enumerate(task.constraints):
            for j in range(len(constraint)):
                if constraint[j] == 1 and SimplexCalc.check_only_zeros(task, j, i):
                    basis.append(j)
                    break  # Stop searching if basis is found
        return basis
    
    def print_basis(self, basis, task):
        print("Current Basis Variables:", [task.var_names[i] for i in basis])

    def print_table(self, table, is_result=False):
        print("Simplex Table:" if not is_result else "Result Table:")
        for row in table:
            print(row)

    @staticmethod
    def gauss(row, temp):
        for i in range(len(row)):
            row[i] += temp[i]

    def simplex(self, task, basis):
        simplex_task = task.objective_function[:]
        simplex_table = [row[:] + [rhs] for row, rhs in zip(task.constraints, task.rhs_values)]
        print("Initial Objective Function Coefficients:", simplex_task)
        print()
        while True:
            self.print_basis(basis, task)
            self.print_table(simplex_table)
            # Compute reduced costs
            result = [[0] * (len(simplex_task) + 1)]
            for i in range(len(simplex_task) + 1):
                if i in basis:
                    continue
                current = 0 if i == len(simplex_task) else simplex_task[i]
                for j in range(len(simplex_table)):
                    current -= simplex_table[j][i] * simplex_task[basis[j]]
                result[0][i] = current
            self.print_table(result, True)
            # Determine entering variable (most negative reduced cost)
            basis_min = result[0][0]
            basis_min_index = 0
            for i in range(1, len(result[0]) - 1):
                if result[0][i] < basis_min:
                    basis_min_index = i
                    basis_min = result[0][i]
            if basis_min >= 0:
                break  # Optimal solution found
            # Determine leaving variable (smallest ratio test)
            RATIO_DEFAULT = float('inf')
            KEY_MIN_DEFAULT = float('inf')
            ratio = RATIO_DEFAULT
            key_element_index_to_leave = -1
            key_min = KEY_MIN_DEFAULT
            for i in range(len(simplex_table)):
                if simplex_table[i][basis_min_index] <= 0:
                    continue
                current_ratio = simplex_table[i][-1] / simplex_table[i][basis_min_index]
                if current_ratio < ratio:
                    ratio = current_ratio
                    key_element_index_to_leave = i
                    key_min = simplex_table[i][basis_min_index]
            if key_min == KEY_MIN_DEFAULT and ratio == RATIO_DEFAULT:
                break  # No feasible solution
            # Update simplex table (pivot operation)
            new_simplex_table = [row[:] for row in simplex_table]
            # Normalize pivot row
            for i in range(len(new_simplex_table[key_element_index_to_leave])):
                new_simplex_table[key_element_index_to_leave][i] /= key_min
            # Perform row operations to make column zero
            for i in range(len(new_simplex_table)):
                if i == key_element_index_to_leave or new_simplex_table[i][basis_min_index] == 0:
                    continue
                factor = -new_simplex_table[i][basis_min_index] / key_min
                main_row = [val * factor for val in simplex_table[key_element_index_to_leave]]
                self.gauss(new_simplex_table[i], main_row)
            # Update basis
            basis[key_element_index_to_leave] = basis_min_index
            simplex_table = new_simplex_table
        print("Optimal solution found!")

    def solve(self, task):
            # Get the initial basis
            basis = self.get_basis(task)
            if len(basis) != len(task.constraints):
                print("Error: Invalid initial basis. The problem might not be in standard form.")
                return
            print("\nInitial Basis Identified:", basis)
            # Run the simplex algorithm
            self.simplex(task, basis)



    
