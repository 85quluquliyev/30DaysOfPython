def fonction_name():
    print('code')

def generate_full_name(first,last):
    full_name = first + ' ' + last
    return full_name

print(generate_full_name('Qulu','Quliyev'))

def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(90))

def area_0f_circle(r):
    PI = 3.14
    return PI * r * r

print(area_0f_circle(23))


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(sum_of_numbers(3))

def square_number(x):
    return x * x
print(square_number(5))

def sum(a,b):
    return a + b

print(sum(2,4))


def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


def add_2(num):
    two = 2
    return num + two

print(add_2(num = 5))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print(calculate_age(2024, 2000))


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(10))


def find_even_numbers(n = 5):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers())


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(3,4,5,6,7,8,1,2))


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

