# Ex1
empty_tuple = tuple()
sisters = ('sister1','sister2','sister3')
brothers = ('brother1','brother2','brother3')
siblings = sisters + brothers
print(len(siblings))
parents = ('mother','father')
family_members = parents + siblings
print(family_members)
parent1, parent2, *siblings = family_members
print(parent1)
print(parent2)

# Ex2
fruits = ('apple','orange')
vegetables = ('onion','cucumber')
animal_product = ('meat','milk')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[2:5])
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)
del food_stuff_tp

# Ex3
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)