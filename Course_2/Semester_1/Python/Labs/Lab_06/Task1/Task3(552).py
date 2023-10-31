# Дано словник, у якому ключами є назви 10 карпатських вершин, а значеннями - їх висота у метрах. Елементи у словнику невпорядковані. Напишіть програму для виведення висоти трьох найвищих гір. Примітка. При використанні метода sorted, можна застосувати як ключ лямбда-функцію на зразок key=lambda x: x[1].

import random
dictionary = {
    'Hoverla': 2061,
    'Brebeneskul': 2035,
    'Pip Ivan Chornohirskyi': 2028,
    'Petros': 2020,
    'Gutin Tomnatyk': 2016, 
    'Ribs': 2001,
    'Menchul': 1998,
    'Pip Ivan Marmaroskyi': 1936,
}

lst = list(dictionary.items())
random.shuffle(lst)
dictionary = dict(lst)
print("Dictionary: ")
for mountain, height in dictionary.items():
    print(f"{mountain}: {height} m")

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
print("\nSorted dictionary: ")
for mountain, height in sorted_dictionary.items():
    print(f"{mountain}: {height} m")