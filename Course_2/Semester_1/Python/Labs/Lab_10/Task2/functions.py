from datetime import datetime, timedelta

def task1(sequence):
    return not bool(sequence)

def task2(sequence):
    return [sequence[0], sequence[len(sequence) - 1]]

def task3(list1, list2):
    flag = False
    for el1 in list1:
        for el2 in list2:
            if(el1 == el2):
                flag = True
    return flag

def task4(num):
    result = 1
    for i in range(num):
        result *= i + 1
    return result

def task5(date_str):
    try:
        date = datetime.strptime(date_str, '%d %m %Y')
    except ValueError:
        return "Incorrect data format. Enter in format 'dd mm YYYY'"

    return (date + timedelta(days=1)).strftime('%Y-%m-%d')