import math

def get_number():
    number = input("Введите число: ")
    return float(number)

def calculate_square(number):
    return number ** 2

def calculate_sqrt(number):
    return math.sqrt(number)

def calculate_sin(number):
    return math.sin(number)

def calculate_cos(number):
    return math.cos(number)

def calculate_tan(number):
    return math.tan(number)

def calculate_factorial(number):
    return math.factorial(int(number))

def calculate_log(number):
    return math.log(number)

def calculate_sum(elements):
    total = 0
    for item in elements:
        total += item
    return total


def print_result(result):
    print("Результат: ", result)

number = get_number()
square = calculate_square(number)
sqrt = calculate_sqrt(square)
sin = calculate_sin(sqrt)
cos = calculate_cos(sin)
tan = calculate_tan(cos)
factorial = calculate_factorial(tan)
log = calculate_log(factorial)

elements = [square, sqrt, sin, cos, tan, factorial, log]
result = calculate_sum(elements)
print_result(result)

