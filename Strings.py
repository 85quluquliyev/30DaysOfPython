"""
letter = 'p'
print(len(letter))

greeting = 'Hello, World!'
sentence = 'I hope you are enjoying'
"""
# multiline_string = """I am Qulu Quliyev. I want to learn Python with this course."""

# space = ' '
"""
print('Py\nthon')
print('Py\tthon')
print('Py\\thon')
print('Py\'thon')

print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')

"""
"""
first_name = 'Qulu'
last_name = 'Quliyev'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius**2
formated_string = 'The area with radius: %d is %f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

"""
"""
first_name = 'Qulu'
last_name = 'Quliyev'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name,last_name,language)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a,b,a+b))
print('{} % {} = {}'.format(a,b,a%b))

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)
"""
"""
a = 4
b = 3

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
"""

"""
language = 'Qulu'
a,b,c,d = language
print(a)
print(b)
print(c)
print(d)

first_latter = language[0]
second_latter = language[1]
last_index = len(language)-1
last_latter = language[last_index]
print(last_latter)

last_alternative_letter = language[-1]
print(last_alternative_letter)
"""

"""
text = 'everything'
thing = text[5:10]
print(thing)

seven = text[-7:-5]
print(seven)
"""
"""
message = 'This is message'
reverse_message = message[::-1]
print(reverse_message)
two_step = message[0:15:3]
print(two_step)
"""

"""
message = 'this is text'
print(message.capitalize())
print(message.count('t',2,9))
print(message.endswith('exr'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(6)) # 'thirty    days      of        python'
print(challenge.expandtabs(15)) # 'thirty    days      of        python'

print(message.find('t'))
print(message.rfind('t'))
"""
"""
name = 'Qulu'
last_name = 'Quliyev'
age = 24
job = 'Python Developer'
country = 'USA'
state = 'MA'
city = 'Boston'

sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(name, last_name, job, age, country)
print(sentence)

"""
"""
radius = 10
pi = 3.14
area = pi * radius**2
result = 'The area with radius: {} is {}.'.format(str(radius), str(area))

print(result)
"""

text = 'abcdefcgh'
print(text.rindex('b'))





























































