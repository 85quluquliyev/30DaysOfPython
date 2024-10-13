"""
empty_tuple = ()
empty_tuple = tuple()
fruits = ('banana','orange','mango','lemon')
print(len(fruits))
first = fruits[1]
second = fruits[2]
last_index = len(fruits)-1
last_fruit = fruits[last_index]
print(last_fruit)
print(fruits[-3])
"""
"""
tpl = ('item1','item2','item3','item4')
middle_two_items = tpl[-3:-1]

print(middle_two_items)
"""
"""
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print(lst)
again = tuple(lst)
print(again)
"""

tpl = ('item1', 'item2', 'item3','item4')
print('item8' in tpl)

family = ('Qulu','Quliyev','Xaliq','Siqura','Atie')
print('Rauf' in family)

all_tpl = tpl + family
print(all_tpl)

del tpl
del family
