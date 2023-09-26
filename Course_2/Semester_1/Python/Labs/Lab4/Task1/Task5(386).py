# Послідовності із символів 0 і 1 називаються бінарними. Вони широко застосовуються в інформатиці. Одне з незручностей бінарних послідовностей – їх важко запам’ятовувати. Для вирішення цієї проблеми був запропонований такий спосіб їх стиснення: переглядаючи послідовність зліва направо, виконується заміна 1 на a, 01 на b, 001 на c, ..., 00000000000000000000000001 на z. Напишіть програму, яка допоможе автоматизувати такий процес заміни.

string = input("Enter string(0/1): ")
isOk = True
for el in string: 
    if(el != '0' and el != '1'): isOk = False
while not isOk:
    string = input("Error! Enter string(0/1): ")
    isOk = True
    for el in string:
        if(el != '0' and el != '1'): isOk = False
    
result = ""
current_symbol = 'a'
for el in string:
    if(el == '1'):
        result += f"{current_symbol}"
        current_symbol = 'a'
    elif(el == '0'): 
        current_symbol = chr(ord(current_symbol) + 1)
        # if current_symbol > 'z': 
        #     current_symbol = 'a'
print("Result: ", result)

