import cmath

print("Welcome to the Quadratic Equation Solver.")
print("\nA quadratic equation is of the form ax^2 + bx + c = 0\nYour solutions can be real or complex numbers.\nA complex number has two parts: a + bj\nWhere a is the real portion and bj is the imaginary portion.")

num_of_equations = int(input("\nHow many equations would you want to solve today: "))

# Adding a loop for number of equations we need to solve
for i in range(1,num_of_equations+1):
    print(f"\nSolving equation {num_of_equations}")
    print("------------------------------------------")
    # input the values of variables to be used for solving equation
    a = float(input("\nPlease enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    print(f"\nThe solutions to the equation  {a}x^2 + {b}x + {c} are: ")
    # Logic for finding the 2 roots of the equation 
    x1 = (-b + cmath.sqrt((b**2)-4*a*c))/2*a
    x2 = (-b - cmath.sqrt((b**2)-4*a*c))/2*a
    print(f"\n\t\t{x1}")
    print(f"\t\t{x2}")

print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")