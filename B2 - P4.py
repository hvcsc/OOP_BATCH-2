#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 4 - INT QUOTIENT
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

print("This program prints the quotient of the two numbers without the decimal point.")

num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ", zero = True)

print(f"\nThe quotient of {num_1} and {num_2} is equal to {int(num_1 // num_2)}")
