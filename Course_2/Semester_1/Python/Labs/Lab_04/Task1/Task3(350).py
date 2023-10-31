# Напишіть програму, яка отримує рядок і обчислює кількість цифр і букв у ньому.

string = input("Enter string: ")
letters = 0
digits = 0
for el in string:
    if el.isdigit(): digits += 1
    if el.isalpha(): letters += 1
print(f"Letters: {letters}")
print(f"Digits: {digits}")

        