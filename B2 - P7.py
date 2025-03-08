#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 7 - EVEN
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the total of even numbers from the given values.")
nums = [number(f"\nEnter number {i + 2}: ") for i in range(10)]
even = sum(1 for num in nums if num % 1 == 0)

print(f"The total of even numbers in the given value is {even}.")
