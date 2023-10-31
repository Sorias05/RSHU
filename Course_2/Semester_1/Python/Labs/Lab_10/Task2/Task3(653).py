# Напишіть функцію, яка приймає два списки та повертає True, якщо у них є щонайменше один спільний елемент.

from functions import task3 as has_same_element

list1 = input("Enter first sequence (Space-separated): ").split()
list2 = input("Enter second sequence (Space-separated): ").split()
print(has_same_element(list1, list2))