string = input("Enter elements (Comma-Separated): ")
list = string.split(',') 
string = ''
for el in list:
    if (list.index(el) % 2 == 0):
        string = string + f"{el}"
        if(list.index(el) != list.__len__() - 1):
            string = string + ","
print(string)
