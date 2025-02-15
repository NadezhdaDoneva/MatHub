from calculators.algebra_calc import AlgebraCalc
from calculators.geom_calc import GeomCalc
from calculators.simplex_calc import SimplexCalc


class Calculators:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Calculators, cls).__new__(cls)
            cls._instance.algebra_calc = AlgebraCalc()
            cls._instance.geom_calc = GeomCalc()
            cls._instance.simplex_calc = SimplexCalc()
        return cls._instance

    def main_menu(self):
        while True:
            print("\nMatHub Main Menu")
            print("Choose your calculator:")
            print("1. Geometry Calculator")
            print("2. Algebra Calculator")
            print("3. Simplex Calculator")
            print("4. Exit")
            choice = input("Enter your choice (14-4): ")
            if choice == '1':
                self.geom_calc.menu()
            elif choice == '2':
                self.algebra_calc.menu()
            elif choice == '3':
                file_name = input("Enter the name of the file containing the Simplex task: ").strip()
                task = self.simplex_calc.read_task_from_file(file_name)
                #file_path = "D:\\Data\\FMI\\Python\\MatHub\\simplex1_task.txt"
                task = self.simplex_calc.read_task_from_file(file_name)
                if task:
                    print("\nTask successfully loaded! Ready to solve.")
                    self.simplex_calc.solve(task)
                else:
                    print("Failed to load task. Please check the file and try again.")
            elif choice == '4':
                print("Exiting MatHub. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    calculators = Calculators()
    calculators.main_menu()
