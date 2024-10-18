"""
while condition:
    print(code)
"""
"""
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)
"""
"""
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 4:
        break
"""
"""
count = 0
while count < 5:
    if count == 3:
        count +=1
        continue
    print(count)
    count += 1
"""
"""
while True:
    password = input('Enter Password: ')
    if password == '1234':
        print('Success')
        break
    else:
        print('Your password is wrong')
"""
'''
while True:
    print("\nMenü:")
    print("1. Toplama")
    print("2. Çıkartma")
    print("3. Çıkış")    
    
    choice = input('Select: ')

    if choice == "1":
        num_1 = input('Enter Number: ')
        num_2 = input('Enter Number: ')
        print(int(num_1) + int(num_2))
    elif choice == "2":
        num_1 = input('Enter Number: ')
        num_2 = input('Enter Number: ')
        print(int(num_1) - int(num_2))
    elif choice == '3':
        print('Goodbye')
        break
    else:
        print('Invalid choice. Please select a valid option.')
'''
"""
numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

text = 'Python'
for letter in text:
    print(letter)

for i in range(len(text)):
    print(text[i])
"""
"""
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key, value in person.items():
    print(key, value)

"""

"""
numbers = [0,1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        continue
"""
"""
lst = list(range(11))
print(lst)

st = set(range(1,8))
print(st)

tp = tuple(range(1,100,5))
print(tp)
"""
"""
for x in y:
    for t in x:
        print(t)
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
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for key in person:
    if key == 'address':
        for k, v in person['address'].items():
            print(f"{k}: {v}")
"""