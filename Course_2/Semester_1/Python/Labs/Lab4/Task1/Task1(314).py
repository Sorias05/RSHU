# Напишіть програму, яка отримує три рядки: прізвище, ім’я і по батькові особи, а потім виводить на екран ініціали та прізвище.

surname = input("Enter surname: ")
first_name = input("Enter first name: ")
patronymic = input("Enter patronymic: ")
print(f"{first_name[0]}.{patronymic[0]}.{surname}")