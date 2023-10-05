# Дано список країн і міст кожної країни. Потім дані назви міст. Для кожного міста вкажіть, в якій країні воно знаходиться.

dictionary = {
    'Ukraine': ['Kyiv', 'Lviv', 'Rivne'],
    'USA': ['Washington', 'New York', 'California'],
    'Japan': ['Tokyo', 'Kyoto'],
    'Germany': ['Berlin'],
    'Poland': ['Warsaw', 'Krakow', 'Lublin']
}

city = input("Enter city name: ")
for country, cities in dictionary.items():
    if city in cities:
        print(country)