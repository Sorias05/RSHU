input_file = open('numbers.txt', 'r')
output_file = open('sum_numbers.txt', 'w')

sum_of_numbers = sum([int(line.strip()) for line in input_file])
print("Summary of numbers: ", sum_of_numbers)

output_file.write(str(sum_of_numbers))