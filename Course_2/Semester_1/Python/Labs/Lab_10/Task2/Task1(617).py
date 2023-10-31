# Напишіть функцію, яка перевіряє, чи подана послідовність порожня чи ні.

from functions import task1 as is_empty

list = input("Enter sequence (Space-separated): ").split()
print(is_empty(list))  
