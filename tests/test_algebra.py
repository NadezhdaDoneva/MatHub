import unittest
from calculators.algebra_calc import AlgebraCalc


class TestAlgebraCalc(unittest.TestCase):

    def setUp(self):
        self.algebra = AlgebraCalc()

    def test_format_polynomial_simple(self):
        """ straightforward polynomial x^2 - 3x + 2"""
        poly = {2: 1, 1: -3, 0: 2}
        formatted = self.algebra.format_polynomial(poly)
        self.assertEqual(formatted, "x^2 - 3x + 2")

    def test_format_polynomial_all_zero_coeffs(self):
        """ all coefficients 0 or near-zero -> "0" """
        poly = {2: 0, 1: 0, 0: 0}
        formatted = self.algebra.format_polynomial(poly)
        self.assertEqual(formatted, "0")

    def test_format_polynomial_leading_negative(self):
        """-x^3 + x + 5 => {3:-1, 1:1, 0:5}"""
        poly = {3: -1, 1: 1, 0: 5}
        formatted = self.algebra.format_polynomial(poly)
        self.assertEqual(formatted, "-x^3 + x + 5")

    def test_format_polynomial_abs_coeff_one_no_degree(self):
        """ x^1 with coeff=1 = "x" and x^0 with coeff=1 = "1" => "x + 1" """
        poly = {1: 1, 0: 1}
        formatted = self.algebra.format_polynomial(poly)
        self.assertEqual(formatted, "x + 1")

    def test_format_polynomial_float_integer_coeff(self):
        """float coefficient (2.0) is replaced by int(2)."""
        poly = {2: 2.0, 1: -1.0, 0: 0.0}
        formatted = self.algebra.format_polynomial(poly)
        self.assertEqual(formatted, "2x^2 - x")

    def test_int_divisors_positive(self):
        """ int_divisors(6) => [1,2,3,6,-1,-2,-3,-6]"""
        result = self.algebra.int_divisors(6)
        expected_divs = {1, 2, 3, 6, -1, -2, -3, -6}
        self.assertEqual(set(result), expected_divs)

    def test_int_divisors_zero(self):
        """If num=0"""
        result = self.algebra.int_divisors(0)
        self.assertIsInstance(result, list)

    def test_is_zero_poly_true(self):
        """ {2: 0, 1: 0, 0: 0} => True && empty dict => True"""
        poly_zero = {2:0, 1:0, 0:0}
        self.assertTrue(self.algebra.is_zero_poly(poly_zero))
        self.assertTrue(self.algebra.is_zero_poly({}))

    def test_is_zero_poly_false(self):
        """ x^2 => {2:1} => False """
        poly_non_zero = {2:1}
        self.assertFalse(self.algebra.is_zero_poly(poly_non_zero))
    
    def test_is_constant_poly_true(self):
        """ A polynomial {0:5} => True (just 5) && An empty dict => True """
        poly_const = {0:5}
        self.assertTrue(self.algebra.is_constant_poly(poly_const))
        self.assertTrue(self.algebra.is_constant_poly({}))

    def test_is_constant_poly_false(self):
        """ x^2 + 3 => degree=2 => not constant """
        poly_non_const = {2:1, 0:3}
        self.assertFalse(self.algebra.is_constant_poly(poly_non_const))

    def test_find_and_factor_out_one_root_simple(self):
        """ (x^2 + x - 2) => roots 1, -2 """
        poly = {2:1, 1:1, 0:-2}
        roots_list = []
        # The first found root should be 1 or -2
        found = self.algebra.find_and_factor_out_one_root(poly, roots_list)
        self.assertTrue(found)
        self.assertEqual(len(roots_list), 1, "Should have found exactly one root so far.")
        # If it found root 1, the new poly should be x+2 => {1:1, 0:2}
        # If it found root -2, the new poly should be x-1 => {1:1, 0:-1}
        # check we can detect one of these:
        if roots_list[0] == 1:
            # Then poly is now x+2
            self.assertEqual(poly, {1:1, 0:2})
        elif roots_list[0] == -2:
            # Then poly is now x-1
            self.assertEqual(poly, {1:1, 0:-1})
        else:
            self.fail(f"Unexpected root found: {roots_list[0]}")
        
    def test_find_and_factor_out_one_root_no_root(self):
        """ x^2 + 2x + 2 => no real rational root => function should return False """
        poly = {2:1, 1:2, 0:2}
        roots_list = []
        found = self.algebra.find_and_factor_out_one_root(poly, roots_list)
        self.assertFalse(found)
        self.assertEqual(len(roots_list), 0)
        self.assertEqual(poly, {2:1, 1:2, 0:2})

    def test_add_polynomials_logic(self):
        p1 = {2: 1, 1: -1, 0: 3}   # x^2 - x + 3
        p2 = {1: 5, 0: -2}        # 5x - 2
        result = self.algebra.add_polynomials_logic(p1, p2)
        # Expect x^2 + 4x + 1 => {2: 1, 1: 4, 0: 1}
        expected = {2: 1, 1: 4, 0: 1}
        self.assertEqual(result, expected)

    def test_subtract_polynomials_logic(self):
        p1 = {2: 1, 1: 3, 0: 5}
        p2 = {2: 1, 1: -1, 0: 2}
        result = self.algebra.subtract_polynomials_logic(p1, p2)
        expected = {2: 0, 1: 4, 0: 3}
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_multiply_polynomials_logic(self):
        p1 = {2: 1, 0: 2}
        p2 = {1: 2, 0: -3}
        result = self.algebra.multiply_polynomials_logic(p1, p2)
        expected = {3: 2, 2: -3, 1: 4, 0: -6}
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_divide_polynomials_logic_no_remainder(self):
        # (x^3 - 1) / (x - 1) => quotient: x^2 + x + 1, remainder: 0
        p1 = {3: 1, 0: -1} # x^3 - 1
        p2 = {1: 1, 0: -1} # x - 1
        quotient, remainder = self.algebra.divide_polynomials_logic(p1, p2)
        # x^2 + x + 1 => {2:1, 1:1, 0:1}, remainder => {}
        expected_quotient = {2: 1, 1: 1, 0: 1}
        expected_remainder = {}
        self.assertEqual(quotient, expected_quotient)
        self.assertEqual(remainder, expected_remainder)

    def test_divide_polynomials_logic_with_remainder(self):
        # (x^3 + 1) / (x - 1) => quotient: x^2 + x + 1, remainder: 2
        p1 = {3: 1, 0: 1}      # x^3 + 1
        p2 = {1: 1, 0: -1}     # x - 1
        quotient, remainder = self.algebra.divide_polynomials_logic(p1, p2)
        # quotient => x^2 + x + 1 => {2:1,1:1,0:1}
        # remainder => 2 => {0:2}
        expected_quotient = {2: 1, 1: 1, 0: 1}
        expected_remainder = {0: 2}
        self.assertEqual(quotient, expected_quotient)
        self.assertEqual(remainder, expected_remainder)

    def test_divide_polynomials_logic_div_by_zero(self):
        # Divisor is zero => returns (None, None)
        p1 = {2: 1}  # x^2
        p2 = {}      # zero polynomial
        quotient, remainder = self.algebra.divide_polynomials_logic(p1, p2)
        self.assertIsNone(quotient)
        self.assertIsNone(remainder)
    
    def test_multiply_polynomial_by_scalar_logic(self):
        # (x^2 + x + 1) * 2 => 2x^2 + 2x + 2
        poly = {2: 1, 1: 1, 0: 1}
        scalar = 2
        result = self.algebra.multiply_polynomial_by_scalar_logic(poly, scalar)
        expected = {2: 2, 1: 2, 0: 2}
        self.assertEqual(result, expected)

    def test_evaluate_polynomial_logic(self):
        # Evaluate x^2 + x + 1 at x=2 => 4 + 2 + 1 = 7
        poly = {2: 1, 1: 1, 0: 1}
        val = self.algebra.evaluate_polynomial_logic(poly, 2)
        self.assertEqual(val, 7)

    def test_gcd_of_polynomials_logic_no_remainder(self):
        # x^2 -1 = (x-1)(x+1)
        # x^3 - x = x(x-1)(x+1)
        # gcd => x^2 -1 => {2:1, 1:0, 0:-1}
        p1 = {2: 1, 0: -1}
        p2 = {3:1, 1:-1}
        gcd_poly = self.algebra.gcd_of_polynomials_logic(p1, p2)
        expected = {2: 1, 0: -1}
        self.assertEqual(gcd_poly, expected)

    def test_vietas_formulas_logic_quadratic(self):
        # x^2 + 5x + 6
        # roots: -2, -3
        # sum_of_roots = -5, product = 6
        # sum = -a1/a2=-5, product= a0/a2=6
        poly = {2:1, 1:5, 0:6}
        vieta_vals = self.algebra.vietas_formulas_logic(poly)
        self.assertEqual(vieta_vals[1], -5)
        self.assertEqual(vieta_vals[2], 6)

    def test_decompose_polynomial_logic_simple(self):
        poly = {2:1, 1:1, 0:-2}   # x^2 + x - 2 = (x-1)(x+2)
        roots, leftover = self.algebra.decompose_polynomial_logic(poly)
        self.assertIn(1, roots)
        self.assertIn(-2, roots)
        self.assertTrue(len(roots) == 2)
        if leftover:
            self.assertTrue(len(leftover) == 1 and 0 in leftover)

if __name__ == "__main__":
    unittest.main()