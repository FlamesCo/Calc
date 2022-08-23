## Metaversal Calculator
print("Flames' Calculator")
print("Version 1.0")

print("--------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
# make a variable to store the user's choice
choice = int(input("Enter your choice: "))
# make a variable to store the first number
if choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 - num2)
elif choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 * num2)
elif choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 / num2) 
elif choice == 5:
    print("Thank you for using the calculator")
else:
    print("Invalid choice")
    print("Exiting...")
    exit()