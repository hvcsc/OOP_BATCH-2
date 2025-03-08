#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 5 - REMAINDER
#DATE: MARCH 2025

def number(prompt, zero = False):
    while True:
        try:
            num = float(input(prompt))
            if zero and num == 0:
                print("Second number cannot be zero.")
            else:
                return num
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the remainder when the first number is divided by the second number.")

num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ", zero = True)
print(f"\nThe remainder when {num_1} is divided by {num_2} is {num_1 % num_2}")

