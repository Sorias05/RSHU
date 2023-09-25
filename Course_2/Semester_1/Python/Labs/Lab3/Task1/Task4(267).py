n = int(input("Input number: "))
for i in range(n):
    row = ""
    for j in range(i):
        row += "-1\t"
    row += " 0\t"
    for j in range(n - i - 1):
        row += " 1\t"
    print(row)