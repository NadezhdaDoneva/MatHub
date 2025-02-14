class Task:
    def __init__(self):
        self.var_names = []  # Variable names
        self.objective_function = []  # Coefficients of the objective function
        self.constraints = []  # List of constraint coefficient lists
        self.rhs_values = []  # Right-hand side values

class SimplexCalc:
    def read_task_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Error: File not found!")
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

