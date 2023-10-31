# Напишіть функцію, яка перевіряє, чи подана послідовність порожня чи ні.

def is_empty(sequence):
    return not bool(sequence)

list = input("Enter sequence (Space-separated): ").split()
print(is_empty(list))  
