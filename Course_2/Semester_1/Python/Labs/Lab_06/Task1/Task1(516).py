# Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів.

string = input("Enter string: ")
dictionary =  {}
for el in string:
    if el in dictionary:
        dictionary[el] += 1
    else:
        dictionary[el] = 1

print(dictionary)