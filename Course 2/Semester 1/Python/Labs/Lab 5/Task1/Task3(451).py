x = int(input("Enter number: "))
res = x
squares = x*x
while(res != 0):
    x = int(input("Enter number: "))
    res += x
    squares += x*x
print(squares)
