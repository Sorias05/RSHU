string = input("Enter string: ")
res = ""
for i in range(len(string)):
    if((i + 1) % 3 != 0):
        res += string[i]
string = res
print(string)
