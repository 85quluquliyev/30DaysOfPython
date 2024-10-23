# 1 
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <=0])

# 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([number for row in list_of_lists for row2 in row for number in row2])

# 3
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] 
for sublist in countries for country, capital in sublist]

print(flattened_countries)

# 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country':country.upper(),'city':capital.upper()}
for sublist in countries for country, capital in sublist
]

print(output)

#5
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
outputa = ['{} {}'.format(first,last) for sublist in names for first, last in sublist]

print(outputa)
