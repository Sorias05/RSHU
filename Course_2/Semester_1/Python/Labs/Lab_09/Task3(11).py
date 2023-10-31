def f(fibonacci_list, i, index):
    if(i > 0):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i])
    if(i < n):
        f(fibonacci_list, i+1, index)

def fibonacci(index):
    fibonacci_list = [1, 1]
    f(fibonacci_list, 0, index)
    return fibonacci_list[index]

n = int(input("Enter index: "))
print(fibonacci(n))