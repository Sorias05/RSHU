import random

def rand_list():
    list = []
    for i in range(10):
        list.append(random.randrange(0, 100))
    return list

list = rand_list()
print(list)
k = int(input("Enter index of element in list to remove: "))
del list[k]
print(list)