import random

def rand(n, r):
    lst = []
    for i in range(n):
        lst.append(random.randrange(r))
    return lst

def F1(L):
    count = 0
    for el in L:
        if el % 2 == 0:
            count += 1
    return count