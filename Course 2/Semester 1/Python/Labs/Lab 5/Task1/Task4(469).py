string = input("Enter elements (Space-Separated): ")
list = string.split() 
res = []
for i in range(0, list.__len__()):
    res.append(list[list.__len__() - i - 1])
string = ''
for el in res:
    string += el
print(string)