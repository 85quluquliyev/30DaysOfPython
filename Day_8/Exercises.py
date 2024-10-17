dog ={
    'name':'Babi',
    'color':'Yellow',
    'legs':4,
    'age':2,
}

student = {
    'first_name' : 'Murad',
    'last_name' : 'Aliyev',
    'gender' : 'Male',
    'age' : 20,
    'marital_status' : 'Single',
    'skills' : ['Math','Law','Language','History'],
    'country' : 'Azerbaijan',
    'city' : 'Baku',
    'address' : {
        'street' : 'Istiglaliyyat',
        'house_number' : 123,
    }
}

print(len(student))
print(student['skills'])
student['skills'].append('Chemistry')
print(student['skills'])
keys = student.keys()
values = student.values()
tp = student.items()
print(tp) 
del student['last_name']
print(student.items())
del student

