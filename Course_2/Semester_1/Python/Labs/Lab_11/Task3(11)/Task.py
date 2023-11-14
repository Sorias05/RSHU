names_phones = {}

input_file = open('Lab_11\Task3(11)\input_file.txt', 'r')
output_file = open('Lab_11\Task3(11)\output_file.txt', 'w')

for line in input_file:
    names, phones = line.strip().split()
    names_phones[names] = phones

for name in sorted(names_phones.keys()):
    if name[0] == 'J' or name[0] == 'j' or name[0] == 'K' or name[0] == 'k':
        res = f'{name} {names_phones[name]}'
        print(res)
        output_file.writelines(f'{res}\n')
        