string = input("Enter elements (Space-Separated): ")
list = string.split() 
print('The list is:', list)
res = []
for i in range(0, list.__len__()):
    res.append(list[list.__len__() - i - 1])
print('Result: ', res)