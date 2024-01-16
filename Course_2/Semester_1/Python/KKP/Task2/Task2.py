num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

operation = ""
while (operation != "max" and operation != "min" and operation != "avg"):
    operation = input("Виберіть операцію (max, min, avg): ").lower()
    
if operation == "max":
    result = max(num1, num2, num3)
    print(f"Maximum: {result}")
elif operation == "min":
    result = min(num1, num2, num3)
    print(f"Minimum: {result}")
elif operation == "avg":
    result = (num1 + num2 + num3) / 3
    print(f"Arithmetic average: {result}")      
