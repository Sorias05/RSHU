# Напишіть функцію для обчислення факторіала заданого числа.

def factorial(num):
    result = 1
    for i in range(num):
        result *= i + 1
    return result

num = int(input("Enter number: "))
print(factorial(num))