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

    # Placeholder methods for functionalities
    def add_polynomials(self):
        print("Functionality: Add two polynomials")
    
    def subtract_polynomials(self):
        print("Functionality: Subtract two polynomials")
    
    def multiply_polynomials(self):
        print("Functionality: Multiply two polynomials")
    
    def divide_polynomials(self):
        print("Functionality: Divide two polynomials")
    
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