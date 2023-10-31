import random

def rand(n, r):
    lst = []
    for i in range(n):
        lst.append(random.randrange(r))
    return lst

def F10(L, K):
    return L == K
