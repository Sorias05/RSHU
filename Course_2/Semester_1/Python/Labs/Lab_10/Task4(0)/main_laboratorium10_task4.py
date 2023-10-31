from lab10_task4 import F10, rand

def check(L, K):
    if len(L) != len(K):
        return "Lists have different length"

    L_sorted = sorted(L)
    K_sorted = sorted(K)
    if L_sorted == K_sorted:
        return "Lists have the same elements in different order"

    return "Lists have different elements, but the same length"

def audit(L, K):
    print("First list", L)
    print("Second list", K)

    if(F10(L, K)):
        print("Lists have the same elements in the same order")
    else:
        print(check(L, K))

# 1
L = rand(10, 20)
K = rand(7, 20)

audit(L, K)

# 2
L = rand(10, 20)
K = rand(10, 20)

audit(L, K)

# 3
L = rand(10, 20)
K = sorted(L)

audit(L, K)

# 4
L = rand(10, 20)
K = L

audit(L, K)