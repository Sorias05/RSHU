c = bool(input("Enter True or False (1 or 0): "))
q = bool(input("Enter True or False (1 or 0): "))

if(not (c and q) == (not c) or (not q)):
    print("De Morgan's first law is fulfilled!")
else: 
    print("De Morgan's first law is not fulfilled!")
