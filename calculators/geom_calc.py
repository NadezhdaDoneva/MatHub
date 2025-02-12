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
            print("9. See created objects")
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
                self.construct_triangle_altitudes()
            elif choice == '7':
                self.tangent_to_parabola()
            elif choice == '8':
                self.parabola_line_intersection()
            elif choice == '9':
                self.see_created_objects()
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

    
    def add_point(self, name, x, y):
        if name in self.points:
            return f"A point named '{name}' already exists! Please use a different name."
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            return "Invalid coordinates. Please enter numeric values."
        self.points[name] = Point(x, y)
        return f"Created point '{name}' at coordinates ({x}, {y})."

    def add_line(self, name, A, B, C):
        if name in self.lines:
            return f"A line named '{name}' already exists! Please use a different name."
        if not all(isinstance(i, (int, float)) for i in [A, B, C]):
            return "Invalid coefficients. Please enter numeric values."
        self.lines[name] = Line(A, B, C)
        return f"Created line '{name}': {A}x + {B}y + {C} = 0."

    def add_parabola(self, name, a, b, c):
        if name in self.parabolas:
            return f"A parabola named '{name}' already exists! Please use a different name."
        if not all(isinstance(i, (int, float)) for i in [a, b, c]):
            return "Invalid coefficients. Please enter numeric values."
        self.parabolas[name] = Parabola(a, b, c)
        return f"Created parabola '{name}': y = {a}x^2 + {b}x + {c}."

    def add_triangle(self, name, p1_name, p2_name, p3_name):
        if name in self.triangles:
            return f"A triangle named '{name}' already exists! Please use a different name."
        if any(p not in self.points for p in [p1_name, p2_name, p3_name]):
            return "One or more points do not exist. Please create them first."
        p1, p2, p3 = self.points[p1_name], self.points[p2_name], self.points[p3_name]
        self.triangles[name] = Triangle(p1, p2, p3)
        return f"Created triangle '{name}' from points ({p1_name}, {p2_name}, {p3_name})."

    def create_point(self):
        name = input("Enter a name for the point: ")
        x = input("Enter x-coordinate: ")
        y = input("Enter y-coordinate: ")
        print(self.add_point(name, x, y))
    
    def create_line(self):
        name = input("Enter a name for the line: ")
        print("Enter the coefficients A, B, C for the equation Ax + By + C = 0:")
        A = input("A: ")
        B = input("B: ")
        C = input("C: ")
        print(self.add_line(name, A, B, C))

    def create_parabola(self):
        name = input("Enter a name for the parabola: ")
        print("Enter the coefficients a, b, c for the equation y = ax^2 + bx + c:")
        a = input("a: ")
        b = input("b: ")
        c = input("c: ")
        print(self.add_parabola(name, a, b , c))

    def create_triangle(self):
        name = input("Enter a name for the triangle: ")
        print("Let's construct a triangle from existing points.")
        p1_name = input("Enter the name of the first point: ")
        p2_name = input("Enter the name of the second point: ")
        p3_name = input("Enter the name of the third point: ")
        print(self.add_triangle(name, p1_name, p2_name, p3_name))

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
    
    @staticmethod
    def compute_line_intersection(line1, line2, tolerance=1e-9):
        determinant = line1.A * line2.B - line2.A * line1.B
        if abs(determinant) < tolerance:
            return None  # Parallel or identical lines
        x = (line2.B * (-line1.C) - line1.B * (-line2.C)) / determinant
        y = (line1.A * (-line2.C) - line2.A * (-line1.C)) / determinant
        return Point(x, y)
    
    @staticmethod
    def compute_line_from_points(point1, point2):
        if point1.x == point2.x:
            return Line(1, 0, -point1.x)  # Vertical line x = constant
        slope = (point2.y - point1.y) / (point2.x - point1.x)
        intercept = point1.y - slope * point1.x
        return Line(-slope, 1, -intercept)
    
    @staticmethod
    def compute_triangle_altitude(triangle, opposite_point):
        if opposite_point == triangle.point1:
            point1c, point2 = triangle.point2, triangle.point3
        elif opposite_point == triangle.point2:
            point1c, point2 = triangle.point1, triangle.point3
        elif opposite_point == triangle.point3:
            point1c, point2 = triangle.point1, triangle.point2
        else:
            print("Error: opposite_point is not a vertex of the triangle.")
            return None
        line = GeomCalc.compute_line_from_points(point1c, point2)
        altitude = GeomCalc.compute_perpendicular_line(line, opposite_point)
        return altitude

    @staticmethod
    def compute_tangent_to_parabola(parabola, point):
        # Ensure the point lies on the parabola
        expected_y = parabola.a * point.x ** 2 + parabola.b * point.x + parabola.c
        if abs(expected_y - point.y) > 1e-9:
            print("Error: The given point does not lie on the parabola.")
            return None
        # Compute the derivative at x (dy/dx = 2ax + b)
        slope = 2 * parabola.a * point.x + parabola.b
        # Use the point-slope formula to get the equation: y - y1 = m(x - x1)
        C = point.y - slope * point.x
        return Line(-slope, 1, -C)  # Convert to Ax + By + C = 0 format
    
    @staticmethod
    def compute_parabola_line_intersection(parabola, line):
        # Express y in terms of x: y = (-Ax - C) / B
        if line.B == 0:
            print("Error: Vertical lines are not currently handled.")
            return None
        # Substitute into the parabola equation: ax^2 + bx + c = (-Ax - C) / B
        A, B, C = line.A, line.B, line.C
        a, b, c = parabola.a, parabola.b, parabola.c
        # Form a quadratic equation: ax^2 + bx + c = (-Ax - C) / B
        new_a = a
        new_b = b + (A / B)
        new_c = c + (C / B)
        # Solve the quadratic equation: new_a x^2 + new_b x + new_c = 0
        discriminant = new_b**2 - 4 * new_a * new_c
        if discriminant < 0:
            return []  # No real solutions, no intersection points
        elif discriminant == 0:
            x = -new_b / (2 * new_a)
            y = (-A * x - C) / B
            return [Point(x, y)]  # One intersection point (tangent)
        else:
            x1 = (-new_b + discriminant**0.5) / (2 * new_a)
            x2 = (-new_b - discriminant**0.5) / (2 * new_a)
            y1 = (-A * x1 - C) / B
            y2 = (-A * x2 - C) / B
            return [Point(x1, y1), Point(x2, y2)]  # Two intersection points
    
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
        line1_name = input("Enter the name of the first line: ")
        line2_name = input("Enter the name of the second line: ")
        line1 = self.get_line(line1_name)
        line2 = self.get_line(line2_name)
        if line1 is None:
            print(f"Line '{line1_name}' does not exist.")
            return None
        if line2 is None:
            print(f"Line '{line2_name}' does not exist.")
            return None
        intersection = self.compute_line_intersection(line1, line2)
        if intersection is None:
            print("The lines are parallel and do not intersect.")
        else:
            print(f"Intersection point: {intersection}")
        return intersection

    def construct_triangle_altitudes(self):
        triangle_name = input("Enter the name of the triangle: ")
        triangle = self.get_triangle(triangle_name)
        if triangle is None:
            print(f"Triangle '{triangle_name}' does not exist.")
            return None
        altitude1 = self.compute_triangle_altitude(triangle, triangle.point3)
        altitude2 = self.compute_triangle_altitude(triangle, triangle.point1)
        altitude3 = self.compute_triangle_altitude(triangle, triangle.point2)
        print(f"Altitude 1 equation: {altitude1}")
        print(f"Altitude 2 equation: {altitude2}")
        print(f"Altitude 3 equation: {altitude3}")
        return altitude1, altitude2, altitude3

    def tangent_to_parabola(self):
        parabola_name = input("Enter the name of the parabola: ")
        point_name = input("Enter the name of the point: ")
        parabola = self.get_parabola(parabola_name)
        point = self.get_point(point_name)
        if parabola is None or point is None:
            return
        tangent = self.compute_tangent_to_parabola(parabola, point)
        if tangent:
            print(f"Tangent line equation: {tangent.A}x + {tangent.B}y + {tangent.C} = 0")
            self.store_new_line_interactive(tangent)

    def parabola_line_intersection(self):
        parabola_name = input("Enter the name of the parabola: ")
        line_name = input("Enter the name of the line: ")
        parabola = self.get_parabola(parabola_name)
        line = self.get_line(line_name)
        if parabola is None or line is None:
            return
        intersections = self.compute_parabola_line_intersection(parabola, line)
        if not intersections:
            print("No real intersection points.")
        elif len(intersections) == 1:
            print(f"One intersection point: {intersections[0]}")
        else:
            print(f"Two intersection points: {intersections[0]} and {intersections[1]}")

    def see_created_objects(self):
        print("Points:")
        print(self.points)
        print("Lines:")
        print(self.lines)
        print("Parabolas:")
        print(self.parabolas)
        print("Triangles:")
        print(self.triangles)

