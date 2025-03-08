#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 3 - DIFFERENCE
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Enter a numeric value.")

print("This program prints the difference between two entered numbers.")
num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ")

print(f"\nThe difference of {num_1} and {num_2} is {num_1 - num_2: .2f}")