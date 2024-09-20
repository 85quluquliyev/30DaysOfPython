# Variables in Python

first_name = 'Qulu'
last_name = 'Quliyev'
country = 'USA'
state = 'MA'
city = 'Boston'
age = 24
is_married = False
skills = ['HTML',"CSS","Python","Django"]
person_info = {
    'firstname':'Qulu',
    'lastname':'Quliyev',
    'country':'USA',
    'state':'MA',
    'city':'Boston',
    'age': age,
    'is_married': is_married,
    'skills': skills
}

print(first_name, last_name, country, state, city, age, is_married)
print('First Name: ', first_name)
print('Last Name: ', last_name)
print('Country: ', country)
print('Are You Married?: ', is_married)

# INPUT

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# CONVERT

num_int = 10
print(num_int)
num_float=float(num_int)
print(num_float)

# ----------------

gravity = 9.81
print(int(gravity))

# -----------------

first_name_to_list = list(first_name)
print(first_name_to_list)