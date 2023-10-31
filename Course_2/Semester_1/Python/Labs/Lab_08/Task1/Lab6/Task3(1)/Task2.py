import random

def rand_list():
    list = []
    for i in range(10):
        list.append(random.randrange(100))
    return list

def result(list1, list2):
    return sorted(list(set(list1) & set(list2)))

list1 = rand_list()
list2 = rand_list()
print(list1)
print(list2)
print(result(list1, list2))
