class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    """ Ax + By + C = 0. """
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __repr__(self):
        return f"Line({self.A}x + {self.B}y + {self.C} = 0)"


class Parabola:
    """ y = ax^2 + bx + c."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"Parabola(y = {self.a}x^2 + {self.b}x + {self.c})"


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def __repr__(self):
        return f"Triangle({self.point1}, {self.point2}, {self.point3})"


class GeomCalc:
    def __init__(self):
        self.points = {}
        self.lines = {}
        self.parabolas = {}
        self.triangles = {}

    def menu(self):
        while True:
            print("\nGeometry Calculator")
            print("1. Create new objects (points, lines, parabolas, triangles)")
            print("2. Check if a point lies on a line")
            print("3. Equation of a line parallel to a given line and passing through a point")
            print("4. Equation of a line perpendicular to a given line and passing through a point")
            print("5. Find the intersection of two lines")
            print("6. Construct the equations of the altitudes, medians, and angle bisectors in a triangle")
            print("7. Equation of the tangent to a given parabola at a given point")
            print("8. Intersection points of a parabola and a line")
            print("9. Determine the type of quadrilateral formed by four lines")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            if choice == '1':
                self.create_objects_menu()
            elif choice == '2':
                self.check_point_on_line()
            elif choice == '3':
                self.parallel_line_equation()
            elif choice == '4':
                self.perpendicular_line_equation()
            elif choice == '5':
                self.find_line_intersection()
            elif choice == '6':
                self.construct_triangle_equations()
            elif choice == '7':
                self.tangent_to_parabola()
            elif choice == '8':
                self.parabola_line_intersection()
            elif choice == '9':
                self.determine_quadrilateral_type()
            elif choice == '10':
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_objects_menu(self):
        while True:
            print("\nCreate Objects Menu")
            print("1. Create a new point")
            print("2. Create a new line")
            print("3. Create a new parabola")
            print("4. Create a new triangle (using existing points)")
            print("5. Return to the main menu")

            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                self.create_point()
            elif choice == '2':
                self.create_line()
            elif choice == '3':
                self.create_parabola()
            elif choice == '4':
                self.create_triangle()
            elif choice == '5':
                return
            else:
                print("Invalid choice. Please try again.")

    def create_point(self):
        name = input("Enter a name for the point: ")
        if name in self.points:
            print(f"A point named '{name}' already exists! Please use a different name.")
            return
        try:
            x = float(input("Enter x-coordinate: "))
            y = float(input("Enter y-coordinate: "))
        except ValueError:
            print("Invalid coordinates. Please try again.")
            return
        self.points[name] = Point(x, y)
        print(f"Created point '{name}' at coordinates ({x}, {y}).")
    
    def create_line(self):
        name = input("Enter a name for the line: ")
        if name in self.lines:
            print(f"A line named '{name}' already exists! Please use a different name.")
            return
        print("Enter the coefficients A, B, C for the equation Ax + By + C = 0:")
        try:
            A = float(input("A: "))
            B = float(input("B: "))
            C = float(input("C: "))
        except ValueError:
            print("Invalid coefficients. Please try again.")
            return
        self.lines[name] = Line(A, B, C)
        print(f"Created line '{name}': {A}x + {B}y + {C} = 0.")

    def create_parabola(self):
        name = input("Enter a name for the parabola: ")
        if name in self.parabolas:
            print(f"A parabola named '{name}' already exists! Please use a different name.")
            return
        print("Enter the coefficients a, b, c for the equation y = ax^2 + bx + c:")
        try:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
        except ValueError:
            print("Invalid coefficients. Please try again.")
            return
        self.parabolas[name] = Parabola(a, b, c)
        print(f"Created parabola '{name}': y = {a}x^2 + {b}x + {c}.")

    def create_triangle(self):
        name = input("Enter a name for the triangle: ")
        if name in self.triangles:
            print(f"A triangle named '{name}' already exists! Please use a different name.")
            return
        print("Let's construct a triangle from existing points.")
        p1_name = input("Enter the name of the first point: ")
        if p1_name not in self.points:
            print(f"Point '{p1_name}' does not exist. Please create it first.")
            return
        p2_name = input("Enter the name of the second point: ")
        if p2_name not in self.points:
            print(f"Point '{p2_name}' does not exist. Please create it first.")
            return
        p3_name = input("Enter the name of the third point: ")
        if p3_name not in self.points:
            print(f"Point '{p3_name}' does not exist. Please create it first.")
            return
        p1 = self.points[p1_name]
        p2 = self.points[p2_name]
        p3 = self.points[p3_name]
        self.triangles[name] = Triangle(p1, p2, p3)
        print(f"Created triangle '{name}' from points ({p1_name}, {p2_name}, {p3_name}).")

    #The following funcs return the object if it exists, otherwise - None
    def get_point(self, point_name):
        return self.points.get(point_name)

    def get_line(self, line_name):
        return self.lines.get(line_name)

    def get_parabola(self, parabola_name):
        return self.parabolas.get(parabola_name)

    def get_triangle(self, triangle_name):
        return self.triangles.get(triangle_name)
    
    #Helper functions
    def get_line_and_point_interactive(self):
        """ Returns (line, point). If either is missing, prints an error and returns (None, None). """
        line_name = input("Enter the name of the line: ")
        point_name = input("Enter the name of the point: ")
        line = self.get_line(line_name)
        point = self.get_point(point_name)
        if line is None:
            print(f"Line '{line_name}' does not exist.")
            return None, None
        if point is None:
            print(f"Point '{point_name}' does not exist.")
            return None, None
        return line, point

    def store_new_line_interactive(self, new_line):
        """ Asks the user if they want to store the new line."""
        choice = input("Do you want to store this new line? (y/n): ").lower()
        if choice == 'y':
            new_line_name = input("Enter a name for the new line: ")
            if new_line_name in self.lines:
                print(f"A line named '{new_line_name}' already exists!")
                return new_line
            self.lines[new_line_name] = new_line
            print(f"Stored the new line '{new_line_name}'.")
        return new_line
    
    #Pure function logics
    @staticmethod
    def is_point_on_line(point, line, tolerance=1e-9):
        lhs = line.A * point.x + line.B * point.y + line.C
        return abs(lhs) < tolerance

    @staticmethod
    def compute_parallel_line(original_line, point):
        """ If original_line is A x + B y + C = 0, then parallel_line is A x + B y + C' = 0, where C' = -(A*point.x + B*point.y)."""
        A = original_line.A
        B = original_line.B
        C_prime = -(A * point.x + B * point.y)
        return Line(A, B, C_prime)
    
    @staticmethod
    def compute_perpendicular_line(original_line, point):
        """ If original_line is A x + B y + C = 0, a perpendicular line is B x - A y + C' = 0, where C' = A*point.y - B*point.x."""
        A = original_line.A
        B = original_line.B
        A_perp = B
        B_perp = -A
        C_perp = (A * point.y) - (B * point.x)
        return Line(A_perp, B_perp, C_perp)

    # Interactive methods
    def check_point_on_line(self):
        line, point = self.get_line_and_point_interactive()
        if line is None or point is None:
            return None
        result = self.is_point_on_line(point, line)
        if result:
            print(f"Point '{point}' lies on line '{line}'.")
        else:
            print(f"Point '{point}' does NOT lie on line '{line}'.")
        return result

    def parallel_line_equation(self):
        line, point = self.get_line_and_point_interactive()
        if line is None or point is None:
            return None
        new_line = self.compute_parallel_line(line, point)
        print(f"Parallel line equation: {new_line.A}x + {new_line.B}y + {new_line.C} = 0")
        self.store_new_line_interactive(new_line)
        return new_line

    def perpendicular_line_equation(self):
        line, point = self.get_line_and_point_interactive()
        if line is None or point is None:
            return None
        new_line = self.compute_perpendicular_line(line, point)
        print(f"Perpendicular line equation: {new_line.A}x + {new_line.B}y + {new_line.C} = 0")
        self.store_new_line_interactive(new_line)
        return new_line

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
