# Напишіть програму, яка обчислює і друкує час виконання (у секундах) для деякого фрагменту коду на Python, наприклад, для сумування чисел від 1 до n. Використайте модуль time.

import time

n = int(input("Enter number: "))
result = 0

start_time = time.time()

for i in range(1, n + 1):
    result += i

end_time = time.time()

print(f"Required time to calculate sum of 1 to {n} (sum = {result}) is:    {end_time - start_time} seconds.")