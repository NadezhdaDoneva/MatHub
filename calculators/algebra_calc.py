# Algebra Calculator Class
class AlgebraCalc:
    def menu(self):
        while True:
            print("\nAlgebra Calculator")
            print("Choose functionality:")
            print("1. Add two polynomials P(x) + Q(x)")
            print("2. Subtract two polynomials P(x) - Q(x)")
            print("3. Multiply two polynomials P(x) * Q(x)")
            print("4. Divide two polynomials P(x) / Q(x)")
            print("5. Multiply polynomial by an integer P(x) * (int)")
            print("6. Find the value of polynomial by given x")
            print("7. Find GCD of two polynomials")
            print("8. Vieta's formulas")
            print("9. Polynomial decomposition")
            print("10. Return to Main Menu")
            choice = input("Enter your choice (1-10): ")
            if choice == '1':
                self.add_polynomials()
            elif choice == '2':
                self.subtract_polynomials()
            elif choice == '3':
                self.multiply_polynomials()
            elif choice == '4':
                self.divide_polynomials()
            elif choice == '5':
                self.multiply_polynomial_by_int()
            elif choice == '6':
                self.evaluate_polynomial()
            elif choice == '7':
                self.gcd_of_polynomials()
            elif choice == '8':
                self.vietas_formulas()
            elif choice == '9':
                self.decompose_polynomial()
            elif choice == '10':
                return
            else:
                print("Invalid choice. Please try again.")

    #HELPER FUNCTIONS
    def format_polynomial(self, polynomial):
        """Връща стринг от полинома, който му е бил подаден, форматиран првилно"""
        # Празен речник
        if not polynomial or all(abs(coeff) < 1e-14 for coeff in polynomial.values()):
            return "0"
        # Сортираме по низходяща степен
        sorted_terms = sorted(polynomial.items(), key=lambda x: -x[0])
        result_parts = []
        for i, (degree, coeff) in enumerate(sorted_terms):
            # Пропускаме много малки коеф
            if abs(coeff) < 1e-14:
                continue
            # Форматиране на знака: 
            # първият термин го пишем без водещ '+' ако е положителен
            sign_str = ""
            if i > 0:
                # Ако не сме на първия термин, слагаме +/-
                sign_str = " + " if coeff >= 0 else " - "
            else:
                # Първи термин е отрицателен
                if coeff < 0:
                    sign_str = "-"
            # Взимаме абсолютната стойност, защото вече сме показали знака горе (ако трябва)
            abs_coeff = abs(coeff)
            # Строим частта, която отговаря на коефициента и степента
            if degree == 0:
                # Свободен член
                term_str = f"{abs_coeff}"
            # Ако степента е 1, не пишем 1; 2.5 -> 2.5x, а не 2.5x^1
            elif degree == 1:
                # За да не пишем 1х, а само х
                if abs_coeff == 1:
                    term_str = "x"
                else:
                    term_str = f"{abs_coeff}x"
            # x^n (n>=2)
            else:
                if abs_coeff == 1:
                    term_str = f"x^{degree}"
                else:
                    term_str = f"{abs_coeff}x^{degree}"
            # Ако имаме integer стойност в abs_coeff (2.0), да го покажем като int (2)
            if isinstance(abs_coeff, float) and abs_coeff.is_integer():
                term_str = term_str.replace(f"{abs_coeff}", str(int(abs_coeff)))
            # Добавяме знака и термина към общия списък
            result_parts.append(sign_str + term_str)
        # Съединяваме result_parts. Те съдържат вече в себе си " + " или " - ", форматираме и връщаме.
        polynomial_str = "".join(result_parts)
        polynomial_str = polynomial_str.strip()
        return polynomial_str

    def input_polynomial(self, prompt):
        print(prompt)
        degree = int(input("Enter degree of your polynomial >> "))
        polynomial = {}
        for d in range(degree, -1, -1):
            coeff = input(f"Enter coefficient before x^{d} >> ")
            try:
                polynomial[d] = float(eval(coeff))
            except Exception:
                print("Invalid input. Please enter a numeric value.")
                return self.input_polynomial(prompt)  # Restart input if invalid
        return polynomial
    
    def polynomial_div(self, dividend: dict, divisor: dict):
        """ Returns (quotient, remainder) of dividend / divisor using polynomial long division"""
        dividend = dividend.copy()
        divisor = divisor.copy()
        # If the divisor is the zero polynomial
        if not divisor or all(abs(c) < 1e-14 for c in divisor.values()):
            return {}, dividend  # quotient={}, remainder=dividend
        quotient = {}
        # While degree(dividend) >= degree(divisor) and dividend is not the zero poly:
        while dividend and max(dividend.keys()) >= max(divisor.keys()):
            # Leading term of dividend
            deg_dvd = max(dividend.keys())
            coeff_dvd = dividend[deg_dvd]
            # Leading term of divisor
            deg_dvs = max(divisor.keys())
            coeff_dvs = divisor[deg_dvs]
            # Compute the factor that will cancel out the leading term of dividend
            deg_diff = deg_dvd - deg_dvs
            coeff_factor = coeff_dvd / coeff_dvs
            # Add that factor to the quotient
            quotient[deg_diff] = quotient.get(deg_diff, 0) + coeff_factor
            # Subtract (divisor * factor) from dividend
            for d, c in divisor.items():
                # new term degree
                new_deg = d + deg_diff
                # multiply c by factor
                sub_val = c * coeff_factor
                # update the dividend
                dividend[new_deg] = dividend.get(new_deg, 0) - sub_val
                # if near 0, remove
                if abs(dividend[new_deg]) < 1e-14:
                    del dividend[new_deg]
        remainder = dividend
        return quotient, remainder
    
    def int_divisors(self, num):
        """Return all integer divisors of 'num', including negative ones."""
        num = abs(num)
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(-i)
        return list(set(divisors))
    
    def evaluate_poly(self, poly, x_val):
        result = 0.0
        for degree, coeff in poly.items():
            result += coeff * (x_val ** degree)
        return result
    
    def is_zero_poly(self, poly):
        """Check if polynomial is effectively 0 (all near-zero coefficients)."""
        if not poly:
            return True
        return all(abs(c) < 1e-14 for c in poly.values())

    def is_constant_poly(self, poly):
        """(degree 0)."""
        if not poly:
            return True
        if len(poly) == 1 and 0 in poly:
            # Only key is 0 => a constant
            return True
        return False
    
    def clean_zero_terms(self, poly: dict):
        """Remove near-zero coefficient terms from a polynomial dict."""
        to_delete = []
        for d, c in poly.items():
            if abs(c) < 1e-14:
                to_delete.append(d)
        for d in to_delete:
            del poly[d]
    
    def find_and_factor_out_one_root(self, poly: dict, roots_list: list) -> bool:
        """
        Attempts to find a single rational root of 'poly'. 
        If found, factors out (x - root) (possibly multiple times),
        appends 'root' to 'roots_list' for each repetition,
        and returns True. If no root is found, returns False.
        """
        # Clean up zero coef
        self.clean_zero_terms(poly)
        if not poly or all(abs(c) < 1e-14 for c in poly.values()):
            return False
        
        # Leading degree and coefficient
        leading_degree = max(poly.keys())
        leading_coeff = poly[leading_degree]
        if abs(leading_coeff) < 1e-14:
            # Not valid
            return False
        # Constant term
        const_coeff = poly.get(0, 0.0)
        # If the polynomial is of degree 0
        if leading_degree == 0:
            return False
        # Generate candidate rational roots using the Rational Root Theorem:
        # possible roots = (divisors of const_coeff) / (divisors of leading_coeff)
        possible_p = self.int_divisors(int(round(const_coeff)))  # divisors of a0
        possible_q = self.int_divisors(int(round(leading_coeff))) # divisors of a_n
        tested_roots = set()  # to avoid re-testing the same candidate
        
        for p in possible_p:
            for q in possible_q:
                if q == 0:
                    continue
                candidate = p / q
                if candidate in tested_roots:
                    continue
                tested_roots.add(candidate)
                val = self.evaluate_poly(poly, candidate)
                if abs(val) < 1e-14:
                    # It's a root, Factor out (x - candidate)
                    while True:
                        # Check again in case of repeated root
                        val_check = self.evaluate_poly(poly, candidate)
                        if abs(val_check) < 1e-14:
                            # Factor out
                            divisor = {1: 1.0, 0: -candidate}  # (x - candidate)
                            quotient, remainder = self.polynomial_div(poly, divisor)
                            # Update poly to the quotient
                            poly.clear()
                            poly.update(quotient)
                            roots_list.append(candidate)
                        else:
                            # candidate no longer divides
                            break
                    return True  # We found at least one root, so return
        # no root found amongst the candid
        return False
    
    #MAIN LOGIC OF ALGEBRA CALC
    def add_polynomials_logic(self, poly1, poly2):
        """Adds two polynomials (dict: degree -> coeff) and returns a new dict with the result."""
        result = {}
        for degree, coeff in poly1.items():
            result[degree] = result.get(degree, 0) + coeff
        for degree, coeff in poly2.items():
            result[degree] = result.get(degree, 0) + coeff
        return result

    def add_polynomials(self):
        print("\nAdding Two Polynomials")
        poly1 = self.input_polynomial("Enter the first polynomial:")
        poly2 = self.input_polynomial("Enter the second polynomial:")
        # Add polynomials
        result_poly = self.add_polynomials_logic(poly1, poly2)
        # Format result
        result_str = self.format_polynomial(result_poly)
        print(f"Resulting Polynomial: {result_str}")

    def subtract_polynomials_logic(self, poly1, poly2):
        """ Subtract two polynomials: poly1 - poly2. Returns a dict: degree -> coefficient. """
        result = {}
        for degree, coeff in poly1.items():
            result[degree] = result.get(degree, 0) + coeff
        for degree, coeff in poly2.items():
            result[degree] = result.get(degree, 0) - coeff
        return result
    
    def subtract_polynomials(self):
        print("\nSubtracting Two Polynomials")
        poly1 = self.input_polynomial("Enter the first polynomial:")
        poly2 = self.input_polynomial("Enter the second polynomial:")
        # Subtract polynomials
        result_dict = self.subtract_polynomials_logic(poly1, poly2)
        # Format result
        result_str = self.format_polynomial(result_dict)
        print(f"Resulting Polynomial: {result_str}")

    def multiply_polynomials_logic(self, poly1: dict, poly2: dict) -> dict:
        """ Multiply two polynomials: poly1 * poly2. Returns a dict: degree -> coefficient."""
        result = {}
        for degree1, coeff1 in poly1.items():
            for degree2, coeff2 in poly2.items():
                new_degree = degree1 + degree2
                new_coeff = coeff1 * coeff2
                result[new_degree] = result.get(new_degree, 0) + new_coeff
        return result
    
    def multiply_polynomials(self):
        print("\nMultiplying Two Polynomials")
        poly1 = self.input_polynomial("Enter the first polynomial:")
        poly2 = self.input_polynomial("Enter the second polynomial:")
        # Multiply polynomials
        result_dict = self.multiply_polynomials_logic(poly1, poly2)
        # Format result
        result_str = self.format_polynomial(result_dict)
        print(f"Resulting Polynomial: {result_str}")

    def divide_polynomials_logic(self, poly1: dict, poly2: dict):
        """ Returns (quotient_dict, remainder_dict) after dividing poly1 by poly2"""
        if not poly2 or all(abs(c) < 1e-14 for c in poly2.values()):
            return None, None  #division by zero
        quotient, remainder = self.polynomial_div(poly1, poly2)
        return quotient, remainder
    
    def divide_polynomials(self):
        poly1 = self.input_polynomial("Enter the dividend polynomial:")
        poly2 = self.input_polynomial("Enter the divisor polynomial:")
        quotient, remainder = self.divide_polynomials_logic(poly1, poly2)
        if not poly2 or all(abs(c) < 1e-14 for c in poly2.values()):
            print("Error: Division by zero polynomial is not allowed.")
            return
        quotient_str = self.format_polynomial(quotient)
        remainder_str = self.format_polynomial(remainder)
        print(f"Quotient: {quotient_str}")
        print(f"Remainder: {remainder_str}")

    def multiply_polynomial_by_scalar_logic(self, poly: dict, scalar: float) -> dict:
        """ Returns a new polynomial dict with every coefficient multiplied by 'scalar'."""
        result = {}
        for degree, coeff in poly.items():
            result[degree] = coeff * scalar
        return result

    def multiply_polynomial_by_int(self):
        poly = self.input_polynomial("Enter the polynomial you want to multiply:")
        scalar_str = input("Enter the rational (or integer) scalar you want to multiply by >> ")
        try:
            scalar = float(eval(scalar_str))
        except Exception:
            print("Invalid input. Please enter a valid rational or integer number.")
            return
        result_dict = self.multiply_polynomial_by_scalar_logic(poly, scalar)
        result_str = self.format_polynomial(result_dict)
        print(f"Resulting Polynomial: {result_str}")

    def evaluate_polynomial_logic(self, poly, x_val):
        """ Evaluates the polynomial dict at x_val and returns the result."""
        val = self.evaluate_poly(poly, x_val)
        #round near-integers:
        if abs(val - round(val)) < 1e-14:
            val = int(round(val))
        return val

    def evaluate_polynomial(self):
        poly = self.input_polynomial("Enter the polynomial you want to evaluate:")
        x_str = input("Enter the value of x (can be e.g. 2, 1/2, 2.5) >> ")
        try:
            x_val = float(eval(x_str))
        except Exception:
            print("Invalid input. Please enter a valid number for x.")
            return
        result = self.evaluate_polynomial_logic(poly, x_val)
        print(f"P({x_val}) = {result}")

    def gcd_of_polynomials_logic(self, poly1, poly2):
        """We will be using Euclidean algorithm. gcd(A,B)=gcd(B,R), where R is the reminder of A / B. We stop when one of the polynomials is 0. Than the other is the GCD"""
        # If both are zero:
        if (not poly1 or all(abs(c) < 1e-14 for c in poly1.values())) and \
        (not poly2 or all(abs(c) < 1e-14 for c in poly2.values())):
            return {}  # GCD is 0 => empty polynomial
        a = poly1.copy()
        b = poly2.copy()
        while True:
            if not b or all(abs(c) < 1e-14 for c in b.values()):
                # b is zero => gcd is a
                return a
            _, remainder = self.polynomial_div(a, b)
            a, b = b, remainder
    
    def gcd_of_polynomials(self):
        poly1 = self.input_polynomial("Enter the first polynomial: ")
        poly2 = self.input_polynomial("Enter the second polynomial: ")
        gcd_poly = self.gcd_of_polynomials_logic(poly1, poly2)
        if not gcd_poly:
            print("GCD: 0")
        else:
            gcd_str = self.format_polynomial(gcd_poly)
            print(f"GCD: {gcd_str}")

    def vietas_formulas_logic(self, poly: dict):
        """ Returns a dict mapping k -> the sum of products of the roots taken k at a time for k in [1..n], where n = max degree. """
        if not poly or max(poly.keys()) == 0:
            return None
        n = max(poly.keys())
        coeffs = []
        for deg in range(n + 1):
            coeffs.append(poly.get(deg, 0.0))
        a_n = coeffs[n]
        if abs(a_n) < 1e-14:
            return None
        vieta_dict = {}
        # for k in 1..n:
        for k in range(1, n + 1):
            a_n_minus_k = coeffs[n - k] if (n - k) >= 0 else 0
            sign_factor = (-1) ** k
            value = sign_factor * (a_n_minus_k / a_n)
            # optional rounding
            if abs(value - round(value)) < 1e-14:
                value = int(round(value))
            vieta_dict[k] = value
        return vieta_dict

    def vietas_formulas(self):
        poly = self.input_polynomial("Enter the polynomial (degree >= 1) to apply Vieta's formulas:")
        vieta_dict = self.vietas_formulas_logic(poly)
        if vieta_dict is None:
            print("The polynomial is degree 0 or leading coeff near 0. Not applicable.")
            return
        n = max(poly.keys())
        print(f"Polynomial degree: {n}\n")
        print("Vieta's Formulas relations:")
        for k in range(1, n + 1):
            value = vieta_dict[k]
            if k == 1:
                description = "Sum of the roots"
            elif k == n:
                description = f"Product of all {n} roots"
            else:
                description = f"Sum of products of the roots taken {k} at a time"
            print(f"  - {description} (k={k}): {value}")
        print()
    
    def decompose_polynomial_logic(self, poly: dict):
        """ Returns (roots_list, leftover_poly) after factoring out all rational roots. If no rational root is found, roots_list is empty and leftover_poly = original. """
        if not poly or all(abs(c) < 1e-14 for c in poly.values()):
            return [], {}
        roots = []
        current_poly = poly.copy()
        while True:
            root_found = self.find_and_factor_out_one_root(current_poly, roots)
            if not root_found:
                break
        return roots, current_poly

    def decompose_polynomial(self):
        poly = self.input_polynomial("Enter the polynomial you want to factor:")
        if not poly or all(abs(c) < 1e-14 for c in poly.values()):
            print("No factorization.")
            return
        # Find all rational roots and factor them out
        # We'll store found roots in a list, e.g. [1, 1, -2] if (x-1)^2*(x+2) are factors, etc.
        roots, current_poly = self.decompose_polynomial_logic(poly)
        if roots:
            # Build a factor string from the found roots: (x - r1)(x - r2)...
            factor_str = ""
            for r in roots:
                # watch the sign
                if r >= 0:
                    factor_str += f"(x - {r})"
                else:
                    factor_str += f"(x + {-r})"
            leftover_str = self.format_polynomial(current_poly)
            if self.is_zero_poly(current_poly):
                # If leftover is 0 or constant 0 => the entire polynomial is factored
                print(f"\nFactorization over rationals: {factor_str}")
            elif self.is_constant_poly(current_poly):
                # If leftover is a nonzero constant, we can factor it out or just show it
                print(f"\nFactorization over rationals: {factor_str} * ({leftover_str})")
            else:
                # leftover has degree >= 1 but no further rational roots
                print(f"\nPartial factorization over rationals: {factor_str} * ({leftover_str})")
        else:
            print("\nNo rational roots were found.")
            print("Polynomial remains unfactored over rationals:")
            print(self.format_polynomial(current_poly))
