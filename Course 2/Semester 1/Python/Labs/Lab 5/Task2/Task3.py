cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong', 'Varshava']
string = ''
for el in cities:
    if cities.index(el) < (cities.__len__() - 2):
        string += f'{el}, '
    elif cities.index(el) == (cities.__len__() - 2):
        string += f'{el} and '
    elif cities.index(el) == (cities.__len__() - 1):
        string += f'{el}.'
print(string)
