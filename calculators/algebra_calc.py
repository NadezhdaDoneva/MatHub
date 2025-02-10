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

    def format_polynomial(self, polynomial: dict) -> str:
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
                polynomial[d] = float(eval(coeff))  # Allow fractional inputs like "3/2"
            except Exception:
                print("Invalid input. Please enter a numeric value.")
                return self.input_polynomial(prompt)  # Restart input on invalid entry
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
        result_str = self.format_polynomial(result)
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
        result_str = self.format_polynomial(result)
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
        result_str = self.format_polynomial(result)
        print(f"Resulting Polynomial: {result_str}")
    
    def divide_polynomials(self):
        poly1 = self.input_polynomial("Enter the dividend polynomial:")
        poly2 = self.input_polynomial("Enter the divisor polynomial:")
        quotient, remainder = self.polynomial_div(poly1, poly2)

        # Ако 'poly2' е нулев (или близък до нулев) полином, polynomial_div ще върне ( {}, dividend )
        # и тогава това означава делене на 0
        if not poly2 or all(abs(c) < 1e-14 for c in poly2.values()):
            print("Error: Division by zero polynomial is not allowed.")
            return

        quotient_str = self.format_polynomial(quotient)
        remainder_str = self.format_polynomial(remainder)
        print(f"Quotient: {quotient_str}")
        print(f"Remainder: {remainder_str}")

    
    def multiply_polynomial_by_int(self):
        poly = self.input_polynomial("Enter the polynomial you want to multiply:")
        scalar_str = input("Enter the rational (or integer) scalar you want to multiply by >> ")
        
        try:
            scalar = float(eval(scalar_str))
        except Exception:
            print("Invalid input. Please enter a valid rational or integer number.")
            return
        
        # Умножаваме всеки коефициент по скалара
        result = {}
        for degree, coeff in poly.items():
            result[degree] = coeff * scalar
        result_str = self.format_polynomial(result)
        print(f"Resulting Polynomial: {result_str}")

    
    def evaluate_polynomial(self):
        poly = self.input_polynomial("Enter the polynomial you want to evaluate:")
        x_str = input("Enter the value of x (can be e.g. 2, 1/2, 2.5) >> ")

        try:
            x_val = float(eval(x_str))
        except Exception:
            print("Invalid input. Please enter a valid number for x.")
            return
        
        result = 0.0
        for degree, coeff in poly.items():
            result += coeff * (x_val ** degree)
        #ако ст-та е много близо до цяло число я закръгляме
        if abs(result - round(result)) < 1e-14:
            result = int(round(result))
        print(f"P({x_val}) = {result}")
    
    # We will be using Euclidean algorithm. gcd(A,B)=gcd(B,R), where R is the reminder of A / B. 
    # We stop when one of the polynomials is 0. Than the other is the GCD
    def gcd_of_polynomials(self):
        poly1 = self.input_polynomial("Enter the first polynomial: ")
        poly2 = self.input_polynomial("Enter the second polynomial: ")
        
        # If both poly are zero, gcd is 0.
        if (not poly1 or all(abs(c) < 1e-14 for c in poly1.values())) and \
        (not poly2 or all(abs(c) < 1e-14 for c in poly2.values())):
            print("Both polynomials are 0; GCD: 0")
            return
        
        # The Euclidean loop
        a = poly1
        b = poly2
        while True:            
            if not b or all(abs(c) < 1e-14 for c in b.values()):
                # b is the zero polynomial => gcd is a
                gcd_poly = a
                gcd_str = self.format_polynomial(gcd_poly)
                print(f"GCD: {gcd_str}")
                return
            
            # else, compute remainder of a / b
            _, remainder = self.polynomial_div(a, b)
            a = b
            b = remainder
    
    def vietas_formulas(self):
        poly = self.input_polynomial("Enter the polynomial (degree >= 1) to apply Vieta's formulas:")
        if not poly or max(poly.keys()) == 0:
            print("The polynomial has degree 0. Vieta's formulas are not applicable.")
            return
        
        # Find the highest degree n
        n = max(poly.keys())
        # Build a coefficient list: a_n, a_{n-1}, ..., a_0
        # For degrees that don't appear in the dictionary, the coefficient is 0.
        # We'll store them in a list such that coeffs[i] = a_i, 
        # so that a_n = coeffs[n], a_0 = coeffs[0].
        coeffs = []
        for deg in range(n + 1):
            coeffs.append(poly.get(deg, 0.0))
        
        # Leading coefficient a_n
        a_n = coeffs[n]
        if abs(a_n) < 1e-14:
            print("The leading coefficient is 0 (or near 0). Please re-check your polynomial.")
            return
        # Print out each Vieta’s relation
        # For k from 1 to n, the sum of products of the roots taken k at a time is:
        # (-1)^k * (a_{n-k} / a_n)
        # We can loop k in [1..n].
        print(f"Polynomial degree: {n}\n")
        print("Vieta's Formulas relations:")
        for k in range(1, n + 1):
            # a_{n-k} means coeffs[n-k]
            a_n_minus_k = coeffs[n - k] if (n - k) >= 0 else 0
            # sign factor is (-1)^k
            sign_factor = (-1)**k
            # value of the sum/product
            vieta_value = sign_factor * (a_n_minus_k / a_n)
            if abs(vieta_value - round(vieta_value)) < 1e-14:
                vieta_value = int(round(vieta_value))
            if k == 1:
                description = "Sum of the roots"
            elif k == n:
                description = f"Product of all {n} roots"
            else:
                description = f"Sum of products of the roots taken {k} at a time"            
            print(f"  - {description} (k={k}): {vieta_value}")
        print()


    
    def decompose_polynomial(self):
        print("Functionality: Polynomial decomposition and finding rational roots")