# Змоделюйте аркуш елетронної таблиці на основі словника. Створіть порожній словник для зберігання значень комірок аркушу електронної таблиці. Заповніть словник кількома значеннями: в одному рядку вводиться адреса комірки у форматі A1, де A - назва стовпця, 1 - номер рядка, і, через пропуск, значення, яке необхідно зберегти в комірці. Надрукуйте «комірки» словника з їхніми значеннями.

dictionary = {}

while True:
    string = input("Input cell adress (A1): ")
    if not string:
        break 
    lst = string.split(' ')
    address = lst[0]
    value = lst[1]
    
    dictionary[address] = value

for address, value in dictionary.items():
    string = list(address)
    print(f"('{string[0]}', '{string[1]}') {value}")