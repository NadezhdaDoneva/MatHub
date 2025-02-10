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
        quotient_str = self.format_polynomial(quotient)
        remainder_str = self.format_polynomial(dividend)
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
    
    def gcd_of_polynomials(self):
        print("Functionality: Find GCD of two polynomials")
    
    def vietas_formulas(self):
        print("Functionality: Vieta's formulas")
    
    def decompose_polynomial(self):
        print("Functionality: Polynomial decomposition and finding rational roots")