import unittest
from calculators.geom_calc import GeomCalc, Point, Line, Parabola, Triangle


class TestGeomCalc(unittest.TestCase):
    def setUp(self):
        self.geometry = GeomCalc()
        self.p1 = Point(1, -2)
        self.p2 = Point(2, 2)
        self.line1 = Line(1, -1, -2)
        self.line2 = Line(2, -1, -4)
        self.parallel_line = Line(1, -1, -5)  # Parallel to line1
        self.coincident_line = Line(2, -2, -4)  # Coincident with line1
        self.test_point = Point(3, 5)
        self.triangle = Triangle(Point(0, 0), Point(4, 0), Point(2, 3))

    def test_add_valid_point(self):
        result = self.geometry.add_point("P1", 2, 3)
        assert result == "Created point 'P1' at coordinates (2, 3)."
        assert "P1" in self.geometry.points

    def test_add_duplicate_point(self):
        self.geometry.add_point("P1", 2, 3)
        result = self.geometry.add_point("P1", 4, 5)
        assert result == "A point named 'P1' already exists! Please use a different name."

    def test_add_point_invalid_x_coordinate(self):
        result = self.geometry.add_point("P1", "abc", 2)
        self.assertEqual(result, "Invalid coordinates. Please enter numeric values.")

    def test_add_point_invalid_y_coordinate(self):
        result = self.geometry.add_point("P1", 2, "xyz")
        self.assertEqual(result, "Invalid coordinates. Please enter numeric values.")

    def test_add_valid_line(self):
        result = self.geometry.add_line("L1", 2, -3, 4)
        assert result == "Created line 'L1': 2x + -3y + 4 = 0."
        assert "L1" in self.geometry.lines

    def test_add_duplicate_line(self):
        self.geometry.add_line("L1", 2, -3, 4)
        result = self.geometry.add_line("L1", 1, 1, -5)
        assert result == "A line named 'L1' already exists! Please use a different name."

    def test_add_line_invalid_A_coefficient(self):
        result = self.geometry.add_line("L1", "A", 3, 4)
        self.assertEqual(result, "Invalid coefficients. Please enter numeric values.")

    def test_add_line_invalid_B_coefficient(self):
        result = self.geometry.add_line("L1", 2, "B", 4)
        self.assertEqual(result, "Invalid coefficients. Please enter numeric values.")

    def test_add_line_invalid_C_coefficient(self):
        result = self.geometry.add_line("L1", 2, 3, "C")
        self.assertEqual(result, "Invalid coefficients. Please enter numeric values.")

    def test_add_valid_parabola(self):
        result = self.geometry.add_parabola("Parabola1", 1, -2, 3)
        assert result == "Created parabola 'Parabola1': y = 1x^2 + -2x + 3."
        assert "Parabola1" in self.geometry.parabolas

    def test_add_duplicate_parabola(self):
        self.geometry.add_parabola("Parabola1", 1, -2, 3)
        result = self.geometry.add_parabola("Parabola1", 2, 3, 4)
        assert result == "A parabola named 'Parabola1' already exists! Please use a different name."

    def test_add_parabola_invalid_a_coefficient(self):
        result = self.geometry.add_parabola("Parabola1", "not_a_number", 2, 3)
        self.assertEqual(result, "Invalid coefficients. Please enter numeric values.")

    def test_add_parabola_invalid_b_coefficient(self):
        result = self.geometry.add_parabola("Parabola1", 1, "not_a_number", 3)
        self.assertEqual(result, "Invalid coefficients. Please enter numeric values.")

    def test_add_parabola_invalid_c_coefficient(self):
        result = self.geometry.add_parabola("Parabola1", 1, 2, "not_a_number")  
        self.assertEqual(result, "Invalid coefficients. Please enter numeric values.")

    def test_add_valid_triangle(self):
        self.geometry.add_point("P1", 0, 0)
        self.geometry.add_point("P2", 3, 0)
        self.geometry.add_point("P3", 0, 4)
        result = self.geometry.add_triangle("T1", "P1", "P2", "P3")
        assert result == "Created triangle 'T1' from points (P1, P2, P3)."
        assert "T1" in self.geometry.triangles

    def test_add_duplicate_triangle(self):
        self.geometry.add_point("P1", 0, 0)
        self.geometry.add_point("P2", 3, 0)
        self.geometry.add_point("P3", 0, 4)
        self.geometry.add_triangle("T1", "P1", "P2", "P3")
        result = self.geometry.add_triangle("T1", "P1", "P2", "P3")
        assert result == "A triangle named 'T1' already exists! Please use a different name."

    def test_add_triangle_with_missing_point(self):
        self.geometry.add_point("P1", 0, 0)
        self.geometry.add_point("P2", 1, 1)
        result = self.geometry.add_triangle("T1", "P1", "P2", "P3")
        self.assertEqual(result, "One or more points do not exist. Please create them first.")

    def test_add_triangle_with_nonexistent_points(self):
        result = self.geometry.add_triangle("T1", "A", "B", "C")
        self.assertEqual(result, "One or more points do not exist. Please create them first.")

    def test_is_point_on_line_true(self):
        result = GeomCalc.is_point_on_line(self.p1, self.line2)
        self.assertTrue(result, "Point should be on the line.")

    def test_is_point_on_line_false(self):
        result = GeomCalc.is_point_on_line(self.p2, self.line2)
        self.assertFalse(result, "Point should not be on the line.")

    def test_is_point_on_line_within_tolerance(self):
        near_point = Point(1, -1.999999999)
        result = GeomCalc.is_point_on_line(near_point, self.line2, tolerance=1e-8)
        self.assertTrue(result, "Point should be considered on the line within tolerance.")

    def test_is_point_on_line_outside_tolerance(self):
        near_point = Point(1, -1.99999)
        result = GeomCalc.is_point_on_line(near_point, self.line2, tolerance=1e-10)
        self.assertFalse(result, "Point should be considered off the line outside tolerance.")

    def test_compute_parallel_line(self):
        parallel_line = GeomCalc.compute_parallel_line(self.line2, self.test_point)
        self.assertEqual(parallel_line.A, self.line2.A, "Parallel line should have the same A coefficient.")
        self.assertEqual(parallel_line.B, self.line2.B, "Parallel line should have the same B coefficient.")
        self.assertEqual(parallel_line.C, -(self.line2.A * self.test_point.x + self.line2.B * self.test_point.y), "Parallel line should have correct C coefficient.")

    def test_compute_perpendicular_line(self):
        perpendicular_line = GeomCalc.compute_perpendicular_line(self.line2, self.test_point)
        self.assertEqual(perpendicular_line.A, self.line2.B, "Perpendicular line should swap A and B.")
        self.assertEqual(perpendicular_line.B, -self.line2.A, "Perpendicular line should negate original A.")
        self.assertEqual(perpendicular_line.C, (self.line2.A * self.test_point.y) - (self.line2.B * self.test_point.x), "Perpendicular line should have correct C coefficient.")

    def test_parallel_line_through_origin(self):
        parallel_line = GeomCalc.compute_parallel_line(self.line2, self.test_point)
        expected_C = -(self.line2.A * self.test_point.x + self.line2.B * self.test_point.y)
        self.assertEqual(parallel_line.C, expected_C, "Parallel line should have correct C value for origin.")

    def test_perpendicular_line_through_origin(self):
        perpendicular_line = GeomCalc.compute_perpendicular_line(self.line2, self.test_point)
        expected_C = (self.line2.A * self.test_point.y) - (self.line2.B * self.test_point.x)
        self.assertEqual(perpendicular_line.C, expected_C, "Perpendicular line should have correct C value for origin.")

    def test_compute_line_intersection_normal_case(self):
        intersection = GeomCalc.compute_line_intersection(self.line1, self.line2)
        expected_point = Point(2, 0)  #x - y - 2 = 0 && 2x - y - 4 = 0
        self.assertAlmostEqual(intersection.x, expected_point.x)
        self.assertAlmostEqual(intersection.y, expected_point.y)

    def test_compute_line_intersection_parallel_lines(self):
        intersection = GeomCalc.compute_line_intersection(self.line1, self.parallel_line)
        self.assertIsNone(intersection, "Parallel lines should not intersect.")

    def test_compute_line_intersection_coincident_lines(self):
        intersection = GeomCalc.compute_line_intersection(self.line1, self.coincident_line)
        self.assertIsNone(intersection, "Coincident lines should not return an intersection point.")

    def test_compute_line_intersection_extreme_tolerance(self):
        near_parallel_line = Line(1.000000001, -1, -2)
        intersection = GeomCalc.compute_line_intersection(self.line1, near_parallel_line, tolerance=1e-8)
        self.assertIsNone(intersection, "Near-parallel lines should be considered parallel.")

    def test_compute_line_from_points_normal_case(self):
        computed_line = GeomCalc.compute_line_from_points(self.p2, self.p1)
        expected_line = Line(-4, 1, 6)
        self.assertAlmostEqual(computed_line.A, expected_line.A)
        self.assertAlmostEqual(computed_line.B, expected_line.B)
        self.assertAlmostEqual(computed_line.C, expected_line.C)

    def test_compute_line_from_points_vertical_case(self):
        p1 = Point(5, 1)
        p2 = Point(5, 10)
        computed_line = GeomCalc.compute_line_from_points(p1, p2)
        expected_line = Line(1, 0, -5)
        self.assertEqual(computed_line.A, expected_line.A)
        self.assertEqual(computed_line.B, expected_line.B)
        self.assertEqual(computed_line.C, expected_line.C)

    def test_compute_triangle_altitude_from_base(self):
        """Test altitude computation from base vertex."""
        altitude = GeomCalc.compute_triangle_altitude(self.triangle, self.triangle.point3)
        expected_altitude = Line(1, 0, -2)  # Perpendicular to x-axis at x = 2
        self.assertEqual(altitude.A, expected_altitude.A)
        self.assertEqual(altitude.B, expected_altitude.B)
        self.assertEqual(altitude.C, expected_altitude.C)

    def test_compute_triangle_altitude_from_side(self):
        """Test altitude from a side vertex (not base)."""
        altitude = GeomCalc.compute_triangle_altitude(self.triangle, self.triangle.point1)
        expected_altitude = Line(1, -1.5, 0)
        self.assertAlmostEqual(altitude.A, expected_altitude.A)
        self.assertAlmostEqual(altitude.B, expected_altitude.B)
        self.assertAlmostEqual(altitude.C, expected_altitude.C)

    def test_compute_triangle_altitude_invalid_point(self):
        """Test altitude when the given opposite point is not a triangle vertex."""
        fake_point = Point(10, 10)
        altitude = GeomCalc.compute_triangle_altitude(self.triangle, fake_point)
        self.assertIsNone(altitude, "Altitude should return None for a non-vertex point.")

    def test_compute_triangle_altitude_right_triangle(self):
        """Test altitude in a right triangle where the altitude is a direct perpendicular line."""
        triangle = Triangle(Point(0, 0), Point(6, 0), Point(3, 4))  # Right triangle
        altitude = GeomCalc.compute_triangle_altitude(triangle, triangle.point3)
        expected_altitude = Line(1, 0, -3)  # x = 3 (Vertical altitude)
        self.assertEqual(altitude.A, expected_altitude.A)
        self.assertEqual(altitude.B, expected_altitude.B)
        self.assertEqual(altitude.C, expected_altitude.C)