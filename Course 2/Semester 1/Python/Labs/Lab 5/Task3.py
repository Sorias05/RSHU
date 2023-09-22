import random
list = []
for i in range(10):
    list.append(random.randrange(0, 100))
print(list)
k = int(input("Enter index of element in list to remove: "))
del list[k]
print(list)