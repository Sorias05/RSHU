# Напишіть функцію, яка приймає два списки та повертає True, якщо у них є щонайменше один спільний елемент.

def has_same_element(list1, list2):
    flag = False
    for el1 in list1:
        for el2 in list2:
            if(el1 == el2):
                flag = True
    return flag

list1 = input("Enter first sequence (Space-separated): ").split()
list2 = input("Enter second sequence (Space-separated): ").split()
print(has_same_element(list1, list2))