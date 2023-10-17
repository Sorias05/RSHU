# Плитка шоколаду має вигляд прямокутника, розділеного на n × m частинок. Плитку шоколаду можна один раз розламати по прямій на дві частини. Визначте, чи можна таким чином відламати від плитки шоколаду шматок, що складається рівно з k частин. Програма отримує на вхід три числа: n, m, k і повинна вивести Yes або No.

def result(n, m, k):
    a = ''
    for i in range(n):
        if(i * m < k):
            a = "No"
        elif(i * m == k):
            a = "Yes"
            break
    if(a != "Yes"):
        for i in range(m):
            if(i * n < k):
                a = "No"
            elif(i * n == k):
                a = "Yes"
                break
    return a

n = int(input("Enter length of bar of chocolate (the amount of pieces): "))
m = int(input("Enter width of bar of chocolate (the amount of pieces): "))
k = int(input("Enter number of pieces: "))

print(result(n, m, k))