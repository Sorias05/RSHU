# Напишіть програму, на вхід якої подається два цілих числа - вік Сашка і вік Тетянки. Програма має вивести повідомлення про те, хто є старшим серед них.

x = int(input("Enter first age: "))
y = int(input("Enter second age: "))
if(x > y):
    print(f"{x} > {y}")
elif(x == y):
    print(f"{x} = {y}")
else:
    print(f"{x} < {y}")