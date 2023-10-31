# Напишіть функцію, яка приймає послідовність чисел як у вхідних даних і створює список лише з першого та останнього елементів.

def new_list(sequence):
    return [sequence[0], sequence[len(sequence) - 1]]

list = input("Enter sequence (Space-separated): ").split()
print(new_list(list))