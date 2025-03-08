#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 9
#DATE: MARCH 2025

print("This program print numbers from 0 to 100 excluding"
      "numbers ending in zero or five.")

for num in range(101):
    if num % 10 != 0 and num % 10 != 5:
        print(num)


