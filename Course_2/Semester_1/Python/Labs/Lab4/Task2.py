string = input("Enter string: ")
length = len(string)
while length < 5:
    string = input("String length must be not less than 5! Enter string: ")
    length = len(string)

print(string[2])

print(string[length - 2])

res = ""
for i in range(5):
    res += string[i]
print(res)

res = ""
for i in range(length):
    if(i % 2 != 0): res += string[i]
print(res)

res = ""
for i in range(length):
    if(i % 2 == 0): res += string[i]
print(res)

res = ""
for i in range(length):
    res += string[length - i - 1]
print(res)

res = ""
for i in range(length):
    if(i % 2 == 0): res += string[length - i - 1]
print(res)

print(length)