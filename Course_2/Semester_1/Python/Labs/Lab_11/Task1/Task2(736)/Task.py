# Запишіть увесь вміст вхідного файла в зворотному порядку у інший файл. Останній рядок вхідного файлу обов’язково закінчується символом \n.

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

output_file.write(input_file.read()[::-1])