import csv


def csvReaderLessons():  # считывание таблицы уроков
    with open('schles2324.csv', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';')
        message = ''
        for row in file_reader:
            message = '| '.join([message, row[0], row[1], row[2], row[3]]) + '\n'
    return message


def csvReaderHolidays():  # считывание таблицы каникул
    with open('schhol2324.csv', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';')
        message = ''
        for row in file_reader:
            message = '| '.join([message, row[0], row[1], row[2], row[3]]) + '\n'
    return message
