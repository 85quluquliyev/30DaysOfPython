"""
lst = list()
lst = []
"""

"""
fruits = ['banana','orange','mango','lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print(len(fruits))
"""

"""
lst = ['Qulu', 250, True, {'country':'USA'}]
first, second, *rest = lst
print(rest)
"""

"""
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(rest)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(scandic)
"""
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion']
fruits.append('apple')
print(fruits)
fruits.insert(2,'lime')
print(fruits)
fruits.remove('orange')
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)
del fruits[1]
print(fruits)
fruits.clear()
print(fruits)
fruits_copy = fruits.copy()
print(fruits_copy)
fruits.insert(0,'apple')
fruits.append('banana')
all = fruits + vegetables
print(all)
fruits.extend(vegetables)
print(fruits)
fruits.append('apple')
fruits.append('apple')
print(fruits.count('apple'))
print(fruits.index('apple'))
fruits.reverse()
print(fruits)
"""
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort(reverse=True)
print(ages)

print(sorted(ages))

"""























