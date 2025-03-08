#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 6 - [1ST - SUM(#)]
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the result of the first number minus all of the remaining numbers.")

first = number("\nEnter the first number: ")
nums = [number(f"Enter number {i + 2}: ") for i in range(9)]
print(f"\nThe result of {first} minus the all the remaining number is {first - sum(nums)}")

