def result(c, q):
    if(not (c and q) == (not c) or (not q)):
        return "De Morgan's first law is fulfilled!"
    else: 
        return "De Morgan's first law is not fulfilled!"

c = bool(input("Enter True or False (1 or 0): "))
q = bool(input("Enter True or False (1 or 0): "))

print(result(c, q))
