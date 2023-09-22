import random
list = []
for i in range(1, 21):
    list.append(random.randrange(-100, 100))
print(list)
count = 0
res = 0
for el in list:
    if el >= 0:
        count += 1
        if count == 2 or count == 4 or count == 6:
            res += el
print(res)