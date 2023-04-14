from datetime import datetime

def read_dates_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        dates = [line.strip() for line in file.readlines()]
    return dates

def convert_to_datetime(dates, date_format='%Y-%m-%d'):
    return [datetime.strptime(date, date_format) for date in dates]

def sort_dates_by_difference(dates):
    today = datetime.now()
    return sorted(dates, key=lambda date: abs((date - today).days))

filename = 'dates_file.txt'
dates = read_dates_from_file(filename)

datetime_dates = convert_to_datetime(dates)
sorted_dates = sort_dates_by_difference(datetime_dates)

print(f'Отсортированный список дат в файле {filename}:')
for date in sorted_dates:
    print(date.strftime('%Y-%m-%d'))
