import csv


def csvReaderLessons():
    with open('schles2324.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(row['num_of_lesson'], '|', row['time'], '|', row['name_of_lesson'], '|', row['num_of_classroom'])


def csvReaderHolidays():
    with open('schhol2324.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='')
    for row in reader:
        print(row['holiday'], '|', row['holiday_starts'], '|', row['holiday_ends'], '|', row['sum_of_days'])
