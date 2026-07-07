a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Enter the operation you want to perform")
operation = input()
if operation == "add":
    print(a+b)
elif operation == "subtract":
    print(a-b)
elif operation == "multiply":
    print(a*b)
elif operation == "divide":
    print(a/b)