# Дано два натуральних числа n і m. Якщо одне з них ділиться на інше без остачі, виведіть 1, інакше виведіть будь-яке інше ціле число.

n = int(input("Enter first natural number: "))
m = int(input("Enter first natural number: "))
print(int(n % m == 0 or m % n == 0))