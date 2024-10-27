try:
    print(10 + '5')
except:
    print('Something went wrong')


try:
    name = input('Name: ')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('Zero division error occured')
