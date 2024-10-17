# if condition:
"""
a = 3
if a > 0:
    print("a is greater than 0")
"""

"""
if a < 0:
    print("a is less than 0")
else:
    print("a is equal to 0 or greater than 0")
"""
"""
a = 5
if a > 0:
    print("a is greater than 0")
elif a < 0:
    print("a is less than 0")
else:
    print("a is equal to 0")
"""
"""
a=3
print('a is greater than 0') if a > 0 else print("a is less than 0")

b=5
print('a=b') if a==b else print('a!=b')
"""
"""
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive and odd integer')
elif a == 0:
    print('A is equal to 0')
else:
    print('A is a negative number')
"""

"""
a = 0
if a > 0 and a % 2 == 0:
    print('A is a positive and even integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive and odd integer')
elif a == 0:
    print('A is equal to 0')
else:
    print('A is a negative number')
"""   

user = 'Qulu'
access_level = 3

if user == 'admin' or access_level >=4:
    print("Access granted!")
else:
    print("Access denied!")