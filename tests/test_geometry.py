import unittest
from calculators.geom_calc import GeomCalc


class TestGeomCalc(unittest.TestCase):
    def setUp(self):
        self.geometry = GeomCalc()

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
        """Test adding a triangle where none of the points exist."""
        result = self.geometry.add_triangle("T1", "A", "B", "C")  # None of these exist
        self.assertEqual(result, "One or more points do not exist. Please create them first.")