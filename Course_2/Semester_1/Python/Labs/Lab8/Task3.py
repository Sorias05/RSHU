# Напишіть функцію palindrome(string), яка повертає True, якщо її аргумент є паліндромом, і False в іншому випадку. Наприклад, виклик palindrome("kayak") має повертати True. У функції паліндром можна використати функцію з попереднього завдання. Перевірте її в основній функції робота функції паліндром.

def is_palindrome(str):
    str = str.replace(" ", "").lower()
    
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1

    return True

str = input("Input string: ")
print(is_palindrome(str))