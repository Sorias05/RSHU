price = 2700
a = int(input("Enter the amount of complects you want to buy: "))
while(a < 1):
    a = int(input("Error! The amount can't be less than 1.\n Enter the amount of complects you want to buy: "))
if(1 <= a < 10):
    print(f"The amount of discount is 0%, total amount of the purchase after the discount is UAH {(price / 100 * 100) * a}")
elif(10 <= a < 20):
    print(f"The amount of discount is 10%, total amount of the purchase after the discount is UAH {(price / 100 * 90) * a}")
elif(20 <= a < 50):
    print(f"The amount of discount is 20%, total amount of the purchase after the discount is UAH {(price / 100 * 80) * a}")
elif(50 <= a < 100):
    print(f"The amount of discount is 30%, total amount of the purchase after the discount is UAH {(price / 100 * 70) * a}")
else:
    print(f"The amount of discount is 40%, total amount of the purchase after the discount is UAH {(price / 100 * 60) * a}")
