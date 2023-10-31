# Користувач вводить рядок і певний символ. Напишіть програму, яка друкує місця розташування (індекси) першої та останньої появи введеного символа. Якщо символ зустрічається лише один раз, то виведіть його індекс. Якщо символ не зустрічається, надрукуйте missing. У цьому завданні не можна використовувати цикли.

string = input("Enter string: ")
symbol = input("Enter symbol you want to find: ")
result = ''
for i in range(len(string)):
    if string[i] == symbol: result += f"{i} "
if len(result) <= 0: print("Missing")
else: print(result)