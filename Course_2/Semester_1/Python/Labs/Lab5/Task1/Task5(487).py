# Напишіть програму, на вхід якої подається список чисел одним рядком. Програма повинна для кожного елемента цього списку вивести суму двох його сусідів. Для елементів списку, які є крайніми, одним із сусідів вважається елемент, що знаходить на протилежному кінці цього списку. Якщо на вхід прийшло тільки одне число, треба вивести його ж. Виведення повинно містити один рядок з числами нового списку, розділеними пропусками. 

string = input("Enter elements (Space-Separated): ")
list = string.split() 
res = []
if(list.__len__() > 1):
    for el in list:
        if(list.index(el) == 0):
            res.append(int(list[list.__len__() - 1]) + int(list[list.index(el) + 1]))
        elif(list.index(el) == list.__len__() - 1):
            res.append(int(list[0]) + int(list[list.index(el) - 1]))
        else:
            res.append(int(list[list.index(el) - 1]) + int(list[list.index(el) + 1]))
else:
    res = list
string = ''
for el in res:
    string += f'{el} '
print(string)