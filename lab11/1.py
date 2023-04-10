import datetime
import numpy as np

# Функция для вычисления дня недели
def get_weekday(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    weekday = date_obj.strftime('%A')
    return weekday

def get_age(birthdate_str):
    birthdate_obj = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.datetime.today()
    age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))
    return age

def get_delta(date_str, birthdate_str):
    birthdate_obj = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    delta = birthdate_obj - datetime.timedelta(days = date_obj.day)
    return delta

def generate_numbers(date_str, birthdate_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    birthdate_obj = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')
    size = np.arange(1, 10, 1)
    numbers = np.random.randint(low=birthdate_obj.year, high=date_obj.year, size=size[5])
    return numbers

def sort_numbers(numbers):
    sort_numbers = np.sort(numbers)
    return sort_numbers

def get_size(numbers):
    size = np.size(numbers)
    return size

def get_mean(numbers):
    mean = np.mean(numbers)
    return mean

def print_results(weekday, age, delta, numbers, sort_numbers, size, mean):
    print('Today is', weekday)
    print('You are', age, 'years old')
    print('Delta:', delta)
    print('Generated numbers:', numbers)
    print('Sort numbers:', sort_numbers)
    print('The size of the numbers is', size)
    print('The mean of the numbers is', mean)

date_str = '2023-04-03'
birthdate_str = '2002-04-10'
weekday = get_weekday(date_str)
age = get_age(birthdate_str)
delta = get_delta(date_str, birthdate_str)
numbers = generate_numbers(date_str, birthdate_str)
sort_numbers = sort_numbers(numbers)
size = get_size(numbers)
mean = get_mean(numbers)
print_results(weekday, age, delta, numbers, sort_numbers, size, mean)
