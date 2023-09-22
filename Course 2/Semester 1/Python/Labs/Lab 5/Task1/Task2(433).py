string = input("Enter elements (Space-Separated): ")
list = string.split()
string = '['
for el in list:
    if (int(el) > 0):
        string += f"{el}"
        if(list.index(el) != list.__len__() - 1):
            string += ", "
string += "]"
print(string)