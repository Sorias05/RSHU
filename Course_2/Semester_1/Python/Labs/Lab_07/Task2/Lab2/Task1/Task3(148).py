# Дано натуральное число. Визначити, чи закінчується число парною цифрою.

def result(n):
    return int(repr(n)[-1]) % 2 == 0

n = int(input("Enter natural number: "))
print(result(n))