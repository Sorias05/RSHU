import random
r = random.randrange(3, 6)
matrix = []
for i in range(r):
    row = []
    for j in range(r):
        row.append(random.randrange(0, 10))
    matrix.append(row)
    print(row)

k = int(input("Enter index of column: "))
res = sorted(matrix, key=lambda row: row[k])
for row in res:
    print(row)