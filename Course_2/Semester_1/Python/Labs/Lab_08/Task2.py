# Напишіть програму, яка використовує функцію для обчислення суми виразу 1 ∗ 2 + 2 ∗ 3 + 3 ∗ 4 + ... + n ∗ (n + 1) для будь-якого n.

def result(n):
    res = 0
    str = ""
    for i in range(1, n+1):
        res += i * (i + 1)
        if(i == 1):
            str += f"{i} * {i + 1}"
        else:
            str += f" + {i} * {i + 1}"
    print(str)
    return res

n = int(input("Enter number: "))
print(result(n))