from countries_data import data
from collections import Counter

def get_country_names():
    for country in data:
        print(country['name'],' - ',country['capital'])

get_country_names()

def len_country():
    print(len(data))

len_country()

def find_country_multiple_language():
    for country in data:
        if len(country['languages']) > 1:
            print(country['name'],' - ',len(country['languages']))
        else:
            continue

find_country_multiple_language()

def most_spoken_language(data):
    all_language = [language for country in data for language in country['languages']]
    print(all_language)
    language_count = Counter(all_language)
    print(language_count)
    max_count = max(language_count.values())
    print(max_count)
    return [language for language, count in language_count.items() if count == max_count]

print(most_spoken_language(data))

def average_population():
    total_population = sum(country['population'] for country in data)
    return total_population / len(data)

print(average_population())

def population_more(data,more):
    for country in data:
        if country['population'] > more:
            print(country['name'])
        else:
            continue

print(population_more(data,25000000))

def find_countries_by_word(data, word):
    return [country['name'] for country in data if word.lower() in country['name'].lower()]

print(find_countries_by_word(data, 'a')) 


def country_with_smallest_population(data):
    return min(data, key=lambda x: x['population'])['name']

print(country_with_smallest_population(data))
