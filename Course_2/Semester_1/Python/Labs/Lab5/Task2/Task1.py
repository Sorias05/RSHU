string = input("Enter elements (Space-Separated): ")
list = string.split() 
print('The list is:', list)
res = 0
for item in list:
    res+=int(item)
print('Result: ', res)