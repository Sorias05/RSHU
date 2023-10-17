def result(string):
    return len(set(string))

string = input("Enter string: ").split()
print(result(string))