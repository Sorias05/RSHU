import random

U = set(range(1, 26))

power_A = 12
power_B = 14
power_C = 9

A = set(random.sample(list(U), power_A))
B = set(random.sample(list(U), power_B))
C = set(random.sample(list(U), power_C))

result = (A.union(B.difference(U - A))).union(U.difference(A).union(B.intersection(U - C)))

elements_result = sorted(list(result))
power_result = len(result)

print("A:", A)
print("B:", B)
print("C:", C)
print("Result: ", elements_result)
print("Result power: ", power_result)
