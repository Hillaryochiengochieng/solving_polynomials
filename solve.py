import numpy as np
from scipy.optimize import fsolve

# Function to evaluate the polynomial
def evaluate_polynomial(coefficients, x):
    result = sum(c * (x ** i) for i, c in enumerate(coefficients))
    return result

# Function to solve the polynomial given user guesses
def solve_polynomial():
    # Step 1: User inputs the polynomial coefficients
    print("Enter the coefficients of the polynomial (from constant to highest degree term).")
   
    coefficients = list(map(float, input("Enter coefficients: ").split()))

    # Step 2: User inputs guesses for the roots
    print("\nEnter your initial guesses for the real zeros (separated by spaces).")
    guesses = list(map(float, input("Enter guesses: ").split()))

    # Step 3: Solve using fsolve
    print("\nSolving polynomial...")
    roots = [fsolve(lambda x: evaluate_polynomial(coefficients, x), guess)[0] for guess in guesses]

    # Step 4: Print results
    print("\nInitial guesses provided:")
    print(guesses)
    print("\nReal zeros found:")
    print(np.unique(np.round(roots, decimals=5)))

# Main program
solve_polynomial()
