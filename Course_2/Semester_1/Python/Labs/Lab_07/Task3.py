def decimal_to_binary(integer_part, fractional_part):
    binary_integer = format(integer_part, "08b")
    binary_fraction = format(fractional_part, "08b")
    
    return binary_integer + '.' + binary_fraction

decimal = (input("Enter decimal number: ")).split(".")
binary = 0
if(len(decimal) == 1):
    binary = decimal_to_binary(int(decimal[0]), 0)
elif(len(decimal) >= 2): 
    binary = decimal_to_binary(int(decimal[0]), int(decimal[1]))
else:
    binary = decimal_to_binary(0, 0)
print("Binary format:", binary)