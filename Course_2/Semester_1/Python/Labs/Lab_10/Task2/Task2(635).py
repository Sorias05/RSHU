# Напишіть функцію, яка приймає послідовність чисел як у вхідних даних і створює список лише з першого та останнього елементів.

from functions import task2 as new_list

list = input("Enter sequence (Space-separated): ").split()
print(new_list(list))