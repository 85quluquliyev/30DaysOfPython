"""
user_age = int(input('Enter your age: '))

if user_age >= 18:
    print('You are old enough to drive')
else:
    print('You need {} more years to learn to drive.'.format(18-user_age))
"""
"""
my_age = 24
your_age = int(input('Enter your age: '))

if my_age > your_age:
    print('I am older than you, {} year difference in age'.format(my_age-your_age))
elif my_age == your_age:
    print('We are the same age')
else:
    print('You are older than me, {} year difference in age'.format(your_age-my_age))
"""
"""
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print('Number one is greater than number two')
elif a < b:
    print('Number two is greater than number one')
else:
    print('Both numbers are equal')
"""
"""
your_grade = int(input('Your Grade: '))
if your_grade >= 80 and your_grade <= 100:
    print('A')
elif your_grade >= 70 and your_grade <= 89:
    print('B')
elif your_grade >= 60 and your_grade <= 69:
    print('C')
elif your_grade >= 50 and your_grade <= 59:
    print('D')
elif your_grade >=0 and your_grade <= 49:
    print('F')
else:
    print('Invalid grade')
"""
"""
Autumn = ['September','October','November']
Winter = ['December','January','February']
Spring = ['March','April','May']
Summer = ['June','July','August']
season = input('Enter a month: ')
if season in Autumn:
    print('Autumn')
elif season in Winter:
    print('Winter')
elif season in Spring:
    print('Spring')
elif season in Summer:
    print('Summer')
else:
    print('Invalid month')
"""
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruit = input('Enter fruit: ')
lower_value = add_fruit.lower()
if lower_value not in fruits:
    fruits.append(lower_value)
else: 
    print('Fruit already exists')
"""
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
"""
if 'skills' in person and person['skills']:
    len_skills = len(person['skills'])
    middle = len_skills // 2  
    print("Middle skill: {}".format(person['skills'][middle]))  
else:
    print('There are no skills')

if 'skills' in person and person['skills']:
    if 'Python' in person['skills']:
        print("I checked")
else:
    print('There are no skills')
"""
"""
if 'skills' in person and person['skills']:
    if 'Javascript' and 'React' and "Node" and "Python" and "MongoDB" in person['skills']:
        print('He is a  full stack developer')
    elif 'Javascript' and 'React' in person['skills']:
        print('He is a front end developer')
    elif "Node" and "Python" and "MongoDB" in person['skills']:
        print('He is a back end developer')
    else:
        print('He is not a developer')
"""

if person['is_marred'] == True and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married'.format(person['first_name'],person['last_name'],person['country']))


























