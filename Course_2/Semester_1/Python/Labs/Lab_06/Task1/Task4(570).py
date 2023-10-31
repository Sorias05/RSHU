# Дано послідовність цілих чисел. Для кожного числа надрукуйте слово YES (в окремому рядку), якщо це число вже зустрічалось в послідовності, і надрукуйте NO, якщо воно ще не було виявлено. Для зберігання значень використайте множину

string = input("Enter numbers: ")
lst = string.split()
dictionary = []
for el in lst:
    if el in dictionary:
        print("YES")
    else:
        print("NO")
    dictionary.append(el)
print(dictionary)