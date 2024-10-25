def square(x):
    return x ** 2

def cube(x):
    return x ** 3


def absolute(x):        
    if x >= 0:
        return x
    else:
        return -(x)
    

def higher_order_function(type,num):
    if type == "square":
        return square(num)
    elif type == "cube":
        return cube(num)
    elif type == "absolute":
        return absolute(num)
    

print(higher_order_function('cube',3))

# Decorators
def greeting():
    return 'welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)

@uppercase_decorator
def greeting():
    return 'welcome'

print(greeting())

# Map

numbers = [1,2,3,4,5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_squared = map(lambda x: x**2,numbers)
print(list(numbers_squared))

numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int,numbers_squared)
print(list(numbers_int))  


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] 

def change_to_upper(name):
    return name.upper()

names_upper = map(change_to_upper, names)
print(list(names_upper))

names_upper = map(lambda name: name.upper(),names)
print(list(names_upper))

# Filter

numbers = [1, 2, 3, 4, 5]
def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

def is_odd(num):
    if num % 2 == 1:
        return True
    return False


def decorator_function(original_function):
    def wrapper_function():
        print("Before executing the function")
        original_function()
        print("After executing the function")
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()