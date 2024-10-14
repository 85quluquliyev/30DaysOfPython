# Ex1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['MSI',"Intel"])
it_companies.remove('Twitter')
it_companies.discard('MSI')
print(it_companies)

# remove - Raises a KeyError if the element does not exist in the set.
# discard - Does not raise an error if the element does not exist in the set.

# Ex2

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.union(b))
print(a.update(b))
print(a.intersection(b))
print(a.issubset(b))
print(a.isdisjoint(b))
print(a.symmetric_difference(b))

del a,b 

# Ex3

age = {24,25,87,95,24,85,74,65,95,74,25,35,15,64,52}
lst = list(age)
print(len(age))
print(len(lst))

"""
Data Type	Ordered	Mutable	Allows Duplicates	Indexed	Unique Elements
String	Yes	No	Yes	Yes	No
List	Yes	Yes	Yes	Yes	No
Tuple	Yes	No	Yes	Yes	No
Set	No	Yes	No	No	Yes
"""

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
words_count = len(unique_words)

print(unique_words,' ',words_count)