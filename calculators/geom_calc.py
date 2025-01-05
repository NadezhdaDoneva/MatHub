# ExampleConfigFiles/nade.txt
class GeomCalc:
    def menu(self):
        while True:
            print("\nGeometry Calculator")
            print("Choose functionality:")
            print("1. Check if a point lies on a line")
            print("2. Derive an equation of the line that is parallel to a given line and passes through a given point")
            print("3. Derive an equation of the line perpendicular to a given line and passes through a given point")
            print("4. Find the intersection of two lines")
            print("5. Construct the equations of heights, medians, and bisectors of a triangle")
            print("6. Derive an equation of the tangent to the given parabola at the given point")
            print("7. Derive points of intersection of a parabola and a line")
            print("8. Determine the type of quadrilateral four given lines form")
            print("9. Return to Main Menu")

            choice = input("Enter your choice (1-9): ")

            if choice == '1':
                self.check_point_on_line()
            elif choice == '2':
                self.parallel_line_equation()
            elif choice == '3':
                self.perpendicular_line_equation()
            elif choice == '4':
                self.find_line_intersection()
            elif choice == '5':
                self.construct_triangle_equations()
            elif choice == '6':
                self.tangent_to_parabola()
            elif choice == '7':
                self.parabola_line_intersection()
            elif choice == '8':
                self.determine_quadrilateral_type()
            elif choice == '9':
                return
            else:
                print("Invalid choice. Please try again.")

    def check_point_on_line(self):
        print("Functionality: Check if a point lies on a line")
        # Implementation goes here

    def parallel_line_equation(self):
        print("Functionality: Derive an equation of the line that is parallel to a given line and passes through a given point")
        # Implementation goes here

    def perpendicular_line_equation(self):
        print("Functionality: Derive an equation of the line perpendicular to a given line and passes through a given point")
        # Implementation goes here

    def find_line_intersection(self):
        print("Functionality: Find the intersection of two lines")
        # Implementation goes here

    def construct_triangle_equations(self):
        print("Functionality: Construct the equations of heights, medians, and bisectors of a triangle")
        # Implementation goes here

    def tangent_to_parabola(self):
        print("Functionality: Derive an equation of the tangent to the given parabola at the given point")
        # Implementation goes here

    def parabola_line_intersection(self):
        print("Functionality: Derive points of intersection of a parabola and a line")
        # Implementation goes here

    def determine_quadrilateral_type(self):
        print("Functionality: Determine the type of quadrilateral four given lines form")
        # Implementation goes here
