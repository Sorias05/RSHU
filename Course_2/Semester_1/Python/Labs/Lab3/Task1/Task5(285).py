# Послідовність складається з різних натуральних чисел і завершується числом 0. Визначте значення другого за величиною елемента в цій послідовності. Вводиться послідовність цілих чисел, що закінчується числом 0 (саме число 0 в послідовність не входить, а використовується як ознака її закінчення). Гарантується, що в послідовності є хоча б два елементи.

n = -1
max = n
max2 = max
count = 0
while n != 0:
    n = int(input("Input number: "))
    while n == 0 and count < 2:
        n = int(input("Error! Try again: "))
    count += 1
    if(n > max2 and n < max):
        max2 = n
    elif(n > max):
        max2 = max 
        max = n

print(max2)
