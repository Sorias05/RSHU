import random

def analyze_numbers(list):
    even = 0
    odd = 0
    positive = 0
    negative = 0

    for num in list:
        if num % 2 == 0: even += 1
        else: odd += 1
        if num > 0: positive += 1
        elif num < 0: negative += 1
    
    return {
        'even': even,
        'odd': odd,
        'positive': positive,
        'negative': negative
    }

list = [random.randint(-100, 100) for i in range(10)]
print(list)

print(f"Even numbers number: {analyze_numbers(list)['even']}")
print(f"Odd numbers number: {analyze_numbers(list)['odd']}")
print(f"Positive numbers number: {analyze_numbers(list)['positive']}")
print(f"Negative numbers number: {analyze_numbers(list)['negative']}")
