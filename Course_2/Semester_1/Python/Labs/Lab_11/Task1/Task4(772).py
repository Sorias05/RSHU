# Напишіть програму, яка визначає розмір файла в поточному каталозі і друкує значення в байтах. Якщо файла із вказаним ім’ям немає, генерується виняток.

import os

file_name = input("Enter file name: ")

try:
    file_size = os.path.getsize(os.path.join(os.getcwd(), file_name))
    print(f"{file_name}: {file_size} Bytes")
except FileNotFoundError as e:
    print(e)