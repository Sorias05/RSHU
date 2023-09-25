n = -1
max = n
max2 = max
count = 0
while n != 0:
    n = int(input("Input number: "))
    while n == 0 and count < 2:
        n = int(input("Error! Try again: "))
    count += 1
    if(n > max2 and n < max):
        max2 = n
    elif(n > max):
        max2 = max 
        max = n

print(max2)
