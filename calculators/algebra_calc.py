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
            print("9. Polynomial decomposition and finding rational roots")
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

    def input_polynomial(self, prompt):
        print(prompt)
        degree = int(input("Enter degree of your polynomial >> "))
        polynomial = {}
        for d in range(degree, -1, -1):
            coeff = input(f"Enter coefficient before x^{d} >> ")
            try:
                polynomial[d] = float(eval(coeff))  # Allow fractional inputs like "3/2"
            except Exception:
                print("Invalid input. Please enter a numeric value.")
                return self.input_polynomial(prompt)  # Restart input on invalid entry
        return polynomial
    
    def add_polynomials(self):
        print("\nAdding Two Polynomials")
        poly1 = self.input_polynomial("Enter the first polynomial:")
        poly2 = self.input_polynomial("Enter the second polynomial:")

        # Add polynomials
        result = {}
        for degree, coeff in poly1.items():
            result[degree] = coeff
        for degree, coeff in poly2.items():
            result[degree] = result.get(degree, 0) + coeff

        # Format result
        sorted_result = sorted(result.items(), key=lambda x: -x[0])  # Sort by degree descending
        result_str = " + ".join(f"{'' if abs(coeff) == 1 and degree != 0 else int(coeff) if coeff.is_integer() else coeff}x^{degree}" if degree != 0 else f"{int(coeff) if coeff.is_integer() else coeff}"
                                 for degree, coeff in sorted_result if coeff != 0).replace("+ -", "- ").replace("1x", "x").replace("-1x", "-x")
        print(f"Resulting Polynomial: {result_str}")
    
    def subtract_polynomials(self):
        print("\nSubtracting Two Polynomials")
        poly1 = self.input_polynomial("Enter the first polynomial:")
        poly2 = self.input_polynomial("Enter the second polynomial:")

        # Subtract polynomials
        result = {}
        for degree, coeff in poly1.items():
            result[degree] = coeff
        for degree, coeff in poly2.items():
            result[degree] = result.get(degree, 0) - coeff

        # Format result
        sorted_result = sorted(result.items(), key=lambda x: -x[0])  # Sort by degree descending
        result_str = " + ".join(f"{'' if abs(coeff) == 1 and degree != 0 else int(coeff) if coeff.is_integer() else coeff}x^{degree}" if degree != 0 else f"{int(coeff) if coeff.is_integer() else coeff}"
                                 for degree, coeff in sorted_result if coeff != 0).replace("+ -", "- ").replace("1x", "x").replace("-1x", "-x")
        print(f"Resulting Polynomial: {result_str}")
    
    def multiply_polynomials(self):
        print("\nMultiplying Two Polynomials")
        poly1 = self.input_polynomial("Enter the first polynomial:")
        poly2 = self.input_polynomial("Enter the second polynomial:")

        # Multiply polynomials
        result = {}
        for degree1, coeff1 in poly1.items():
            for degree2, coeff2 in poly2.items():
                new_degree = degree1 + degree2
                new_coeff = coeff1 * coeff2
                result[new_degree] = result.get(new_degree, 0) + new_coeff

        # Format result
        sorted_result = sorted(result.items(), key=lambda x: -x[0])  # Sort by degree descending
        result_str = " + ".join(f"{'' if abs(coeff) == 1 and degree != 0 else int(coeff) if coeff.is_integer() else coeff}x^{degree}" if degree != 0 else f"{int(coeff) if coeff.is_integer() else coeff}"
                                 for degree, coeff in sorted_result if coeff != 0).replace("+ -", "- ").replace("1x", "x").replace("-1x", "-x")
        print(f"Resulting Polynomial: {result_str}")
    
    def divide_polynomials(self):
        print("\nDividing Two Polynomials")
        poly1 = self.input_polynomial("Enter the dividend polynomial:")
        poly2 = self.input_polynomial("Enter the divisor polynomial:")

        # Ensure divisor is not zero
        if all(coeff == 0 for coeff in poly2.values()):
            print("Error: Division by zero polynomial is not allowed.")
            return

        # Division algorithm
        dividend = poly1.copy()
        divisor = poly2.copy()
        quotient = {}

        while dividend and max(dividend.keys()) >= max(divisor.keys()):
            lead_degree_dividend = max(dividend.keys())
            lead_coeff_dividend = dividend[lead_degree_dividend]

            lead_degree_divisor = max(divisor.keys())
            lead_coeff_divisor = divisor[lead_degree_divisor]

            degree_diff = lead_degree_dividend - lead_degree_divisor
            coeff_quotient = lead_coeff_dividend / lead_coeff_divisor

            quotient[degree_diff] = coeff_quotient

            # Subtract the product of divisor and current term of quotient from dividend
            for degree, coeff in divisor.items():
                term_degree = degree + degree_diff
                term_coeff = coeff * coeff_quotient
                dividend[term_degree] = dividend.get(term_degree, 0) - term_coeff
                if abs(dividend[term_degree]) < 1e-10:  # Clean up near-zero values
                    del dividend[term_degree]

        # Format quotient and remainder
        sorted_quotient = sorted(quotient.items(), key=lambda x: -x[0])
        quotient_str = " + ".join(f"{'' if abs(coeff) == 1 and degree != 0 else int(coeff) if coeff.is_integer() else coeff}x^{degree}" if degree != 0 else f"{int(coeff) if coeff.is_integer() else coeff}"
                                    for degree, coeff in sorted_quotient if coeff != 0).replace("+ -", "- ").replace("1x", "x").replace("-1x", "-x")

        sorted_remainder = sorted(dividend.items(), key=lambda x: -x[0])
        remainder_str = " + ".join(f"{'' if abs(coeff) == 1 and degree != 0 else int(coeff) if coeff.is_integer() else coeff}x^{degree}" if degree != 0 else f"{int(coeff) if coeff.is_integer() else coeff}"
                                    for degree, coeff in sorted_remainder if coeff != 0).replace("+ -", "- ").replace("1x", "x").replace("-1x", "-x")

        print(f"Quotient: {quotient_str if quotient else '0'}")
        print(f"Remainder: {remainder_str if dividend else '0'}")
    
    def multiply_polynomial_by_int(self):
        print("Functionality: Multiply polynomial by an integer")
    
    def evaluate_polynomial(self):
        print("Functionality: Evaluate polynomial by given x")
    
    def gcd_of_polynomials(self):
        print("Functionality: Find GCD of two polynomials")
    
    def vietas_formulas(self):
        print("Functionality: Vieta's formulas")
    
    def decompose_polynomial(self):
        print("Functionality: Polynomial decomposition and finding rational roots")