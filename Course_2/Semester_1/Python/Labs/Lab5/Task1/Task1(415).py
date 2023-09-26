# Виведіть всі елементи списку з непарними індексами. Вводиться список чисел, елементи якого розділені комами без пропусків. Всі числа списку знаходяться на одному рядку. Необхідно вивести список в одному рядку і елементи списку мають бути розділені комами без пропусків.

string = input("Enter elements (Comma-Separated): ")
list = string.split(',') 
string = ''
for el in list:
    if (list.index(el) % 2 == 0):
        string = string + f"{el}"
        if(list.index(el) != list.__len__() - 1):
            string = string + ","
print(string)
