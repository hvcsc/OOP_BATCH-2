#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 10 - IN BETWEEN
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return int(float(input(prompt)))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program print all the numbers between the two given numbers.")
num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ")

print(f"\nNumbers in between of {num_1} and {num_2}: ")
if num_1 < num_2:
    for num in range(num_1 + 1, num_2):
        print(num, end=" ")
elif num_1 > num_2:
    for num in range (num_1 - 1, num_2, -1):
        print(num,end=" ")
else:
    print("No numbers in between.")
