import os

with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
    file2.write(file1.read())

with open('file2.txt', 'r') as file2: 
    print("Copied data:\n", file2.read())

os.remove('file1.txt')
