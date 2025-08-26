# Simple calculator 


import math
import string
num = int(input("Enter how many numbers: "))
n = []     # creates an empty list
for i in range(num):
    a = float(input(f"Enter number {i+1}: "))
    n.append(a)      #stores values of a as [1, 2, 3]

   




print("Choice 1: Addition")
print("Choice 2: Multiplication")
print("Choice 3: Subtractions")
print("Choice 4: Division")
print("Which opereation would you like to choose? ")
choice = int(input("Enter your choice: "))

if choice == 1:
    add = sum(n)
    print(f"The sum of the numbers you entered is : {add}")

elif choice == 2:
    multi = math.prod(n)
    print(f"The multiplication of the numbers you entered is: {multi}")

elif choice == 3:
    result = n[0]    # takes the 1st value 
    for num in n[1:]:     # starts from the second value
        result -= num
    print(f"The subtraction of the numbers you entered is: {result}")

elif choice == 4:
    result = n[0]
    for num in n[1:]:
        result /= num
    print(f"The divison of the numbers you entered is: {result}")

else:
    print("Invalid choice")

