language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

numbers = [i for i in range(1,11,2)]
print(numbers)

squares = [i*i for i in range(11)]
print(squares)

even_num = [i for i in range(11) if i % 2 == 0]
print(even_num)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i > 0 and i % 2 == 0]
negative_odd_numbers = [i for i in numbers if i < 0 and i % 2 == 1]

print(positive_even_numbers)
print(negative_odd_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)


x = lambda param1, param2, param3: param1+param2+param3
print(x(1,2,3))

def add_two_nums(a,b):
    return a + b
print(add_two_nums(5,7))

v = lambda a,b: a+b
print(v(5,7))

def squeare_num(a,b):
    return a**b

print(squeare_num(5,7))

k = lambda a,b: a**b
print(k(10,10))

def power(x):
    return lambda n: x**n
print(power(2)(3))

def make_full_name(name):
    return lambda surname: name + " " + surname

print(make_full_name('Qulu')('Quliyev'))





















