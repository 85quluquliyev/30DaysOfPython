empty_dict = {}
dct = {'key1':'value1','key2':'value2'}

person = {
    'name':'Qulu',
    'last_name':'Quliyev',
    'age': 24,
    'country':'USA',
    'city':'Boston',
    'is_married': False,
    'skills': ['python', 'java', 'c++'],
    'address': {
        'country':'USA',
        'city':'Boston',
        'street':'123 Main St',
        'apartment':'123'
    }
}

print(len(person))
print(person['name'])
person['name'] = 'Dale'
print(person['name'])
print(person['skills'][2])
print(person['address']['city'])
print(person.get('age'))

person['was_born'] = '03.05.2000'
person['skills'].append('HTML')
print(person['was_born'])
print(person['skills'][-1])

print('name' in person)
person.pop('name')
print('name' in person)
person.popitem()
del person['skills']
print(dct.items())
dct.clear()
print(dct.items())


dct_copy = dct.copy()
print(dct_copy.items())

keys = person.keys()
print(keys)
value = person.values()
print(value)


