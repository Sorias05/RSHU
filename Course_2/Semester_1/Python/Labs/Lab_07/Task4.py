def symbol_count(str):
    lst = list(str.replace(" ", ""))
    dictionary = {}
    for el in lst:
        if el in dictionary:
            dictionary[el] += 1
        else:
            dictionary[el] = 1
    
    return dictionary

str = input("Input string: ")
print(symbol_count(str))