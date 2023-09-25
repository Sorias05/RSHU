n = int(input("Input number: "))
for i in range(n):
    str = "#"
    for j in range(i):
        str += " "
    str += "#"
    print(str)