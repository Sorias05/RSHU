# Компанія-виробник програмного забезпечення у сфері інформаційної безпеки реалізує один комплект програм за 2700 гривень. Якщо відбувається купівля декількох одиниць товару, працює система знижок: 10-19 одиниць товару - 10%, 20-49 - 20%, 50-99 - 30%, 100 або більше - 40%. Напишіть програму, яка отримує від користувача ціле число - кількість придбаних комплектів програмного забезпечення і виводить повідомлення про суму знижки (якщо така є) та загальну суму при купівлі зі знижкою.

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
