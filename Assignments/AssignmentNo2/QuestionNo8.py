# Q:8 Take two int values from user and print greatest among them.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))


if num1 > num2:
    print(f"{num1} is greater.")

elif num2 > num1:
    print(f"{num2} is greater.")

else:
    print("Both numbers are equal.")
