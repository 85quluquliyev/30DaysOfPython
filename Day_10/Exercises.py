# Ex1
"""
count = 0
while count < 10:
    print(count)
    count += 1

count = 9
while 0 <= count < 10 :
    print(count)
    count -= 1

count = 1
while count < 8:
    print(count * '#')
    count += 1

count = 1
while count < 9:
    print(8 * '#')
    count += 1

count = 0
while count < 11:
    count_alt = 0
    while count_alt < 11:
        print(f'{count} * {count_alt} = ',count * count_alt)
        count_alt += 1
    else:
        print(' ')
        count += 1

for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(i)
"""

# Ex2
"""
even = 0
odd = 0
for i in range(101):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(odd)
print(odd)
"""

# Ex3
"""
from Countries import countries

land = []

for country in countries:
    if 'land' in country:
        land.append(country)

print("Countries containing 'land':", land)
"""
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed list:", reversed_fruits)
    
"""

from countries_data import data
"""
all_language = set()
for country in data:
    all_language.update(country['languages'])

for i in all_language:
    print(i)
print("Total number of unique languages:", len(all_language))
"""

populated_countries = []

for country in data:
    populated_countries.append((country["name"], country["population"]))

sorted_countries = sorted(populated_countries, key=lambda x: x[1], reverse=True)
top_10_populated = sorted_countries[:10]

print("Top 10 most populated countries:")
for country, population in top_10_populated:
    print(f"{country}: {population}")



