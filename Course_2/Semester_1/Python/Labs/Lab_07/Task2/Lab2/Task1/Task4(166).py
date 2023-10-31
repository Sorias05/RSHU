# Дано два натуральних числа n і m. Якщо одне з них ділиться на інше без остачі, виведіть 1, інакше виведіть будь-яке інше ціле число.

def result(n, m):
    return int(n % m == 0 or m % n == 0)

n = int(input("Enter first natural number: "))
m = int(input("Enter first natural number: "))

print(result(n, m))