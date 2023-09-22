x = input("Enter x number: ") 
y = input("Enter y number: ") 
print(f"x = {x}")
print(f"y = {y}")
tuple1 = (x, y)
y, x = tuple1
print("Reverse")
print(f"x = {x}")
print(f"y = {y}")