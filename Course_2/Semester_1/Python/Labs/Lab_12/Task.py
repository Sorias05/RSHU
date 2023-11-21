import csv
import os
import glob

painters_str = 'painters.csv'

painters_file = open(painters_str, 'r')
print(list(csv.DictReader(painters_file)))

imdb = [
    {'title': 'Lord of the Rings: Two towers', 'year': 2002, 'rating': 8.7},
    {'title': 'Matrix', 'year': 1999, 'rating': 8.7},
    {'title': 'Interstellar', 'year': 2014, 'rating': 8.5},
    {'title': 'Back to the Future', 'year': 1985, 'rating': 8.5},
    {'title': 'Logan: Wolverine', 'year': 2017, 'rating': 8.1}
]
fieldnames = ['title', 'year', 'rating']

imdb_file = open('imdb.csv', 'w')
writer = csv.DictWriter(imdb_file, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(imdb)

current_directory = os.getcwd()
file_list = os.listdir(current_directory)
print("Current Directory:", current_directory)
print("Files in Directory:", file_list)

file_path = os.path.join(current_directory, painters_str)
file_size = os.path.getsize(file_path)
print(f"Size of {painters_str}: {file_size} bytes")

file_pattern = '*.csv' 
files_matching_pattern = glob.glob(file_pattern)
print(f"Files matching pattern '{file_pattern}':", files_matching_pattern)