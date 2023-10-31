# Напишіть програму, яка друкує наступний день для певної дати як у вихідних даних у форматі рррр-мм-дд. Напишіть окремі функції для обробки даних, які вводить користувач і використайте їх у програмі.

from datetime import datetime, timedelta

def get_next_day(date_str):
    try:
        date = datetime.strptime(date_str, '%d %m %Y')
    except ValueError:
        return "Incorrect data format. Enter in format 'dd mm YYYY'"

    return (date + timedelta(days=1)).strftime('%Y-%m-%d')

date = input("Enter date (dd mm YYYY): ")
print(get_next_day(date))