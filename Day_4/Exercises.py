
# Ex1
strings = ['Thirty', 'Days', 'Of', 'Python']
concatenation = ' '.join(strings) 

print(concatenation)

# Ex2
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Ex3
first_space_index = company.find(' ')
sliced_string = company[first_space_index+1:]
print(sliced_string)

# Ex4
print(company.rindex('Coding'))

# Ex5
print(company.replace('Coding', 'Python'))

#Ex6
print(company.split())

#Ex7
big_companies = ["Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"]
print(big_companies[0].split(', '))

#Ex8
print(company.__getitem__(0))

#Ex9
print(company[-1])

#Ex10
print(company[10:])

#Ex11
sentence = 'Python For Everyone'
words = sentence.split()
acronym = ''.join([word[0] for word in words])
print(acronym)

#Ex12
print(company.startswith('Coding'))
print(company.endswith('Coding'))

#Ex13
example = '   Coding For All      '
print(example.strip())

#Ex14
text = "I am enjoying this challenge.\nI just wonder what is next."
print(text)

#Ex15
word_text = 'Name Age Country City \nAsabeneh 250 Finland Helsinki'
print(word_text.expandtabs(25))

#Ex16
radius = 10
area = int(3.14 * radius**2)
print('The area of a circle with radius {} is {} meters square'.format(radius, area))
