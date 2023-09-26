# Дано натуральное число. Визначити, чи закінчується число парною цифрою.

n = int(input("Enter natural number: "))
print(int(repr(n)[-1]) % 2 == 0)