# Напишіть програму, яка друкує наступний день для певної дати як у вихідних даних у форматі рррр-мм-дд. Напишіть окремі функції для обробки даних, які вводить користувач і використайте їх у програмі.

# from datetime import datetime, timedelta

from functions import task5 as get_next_day

date = input("Enter date (dd mm YYYY): ")
print(get_next_day(date))