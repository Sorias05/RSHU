# Цілі числа (додатні і від’ємні) вводяться через пропуск в одному рядку. Напишіть програму для друку списку лише із введених додатних чисел.

string = input("Enter elements (Space-Separated): ")
list = string.split()
string = '['
for el in list:
    if (int(el) > 0):
        string += f"{el}"
        if(list.index(el) != list.__len__() - 1):
            string += ", "
string += "]"
print(string)