import random
list1 = []
list2 = []
for i in range(10):
    list1.append(random.randrange(100))
    list2.append(random.randrange(100))
print(list1)
print(list2)
common_numbers = sorted(list(set(list1) & set(list2)))
print(common_numbers)
