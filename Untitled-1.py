def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter operation (1/2/3/4): ")

if operation == '1':
    print(f"The result is: {add(num1, num2)}")
elif operation == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif operation == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif operation == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid operation")
