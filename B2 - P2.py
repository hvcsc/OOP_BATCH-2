#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 2 - NOT EQUAL
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints 'Not Equal' when two entered numbers are not the same.")
num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ")

if num_1 != num_2:
    print("\nNot Equal.")