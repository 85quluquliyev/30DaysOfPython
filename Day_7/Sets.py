"""
st = set()
st = {'item1','item2','item3'}
"""
"""
fruits = {'banana','orange','mango','lemon'}
fruits.add('apple')
print(len(fruits))
print('orange' in fruits)
print(fruits)
fruits.remove('banana')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)
del fruits
"""
"""
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)
"""
"""
lst = ['item1','item2','item3']
st = set(lst)
print(st)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.union(st2)
st1.update(st2)
print(st1)
print(st1)
"""
"""
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item7'}

print(st1.intersection(st2))

whole_number = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_number.intersection(even_numbers))
print(even_numbers.issuperset(whole_number))


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))
print(st1.issuperset(st2))
"""
"""
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item7', 'item8','item9'}
print(st1.difference(st2))
print(st1.symmetric_difference(st2))
print(st2.isdisjoint(st1))

"""
