# Ex1
"""
def add_two_numbers(num1,num2):
    return num1+num2

def area(r):
    return 3.14*r**2

def add_all_nums(n):
    total = 0
    total_odd = 0
    total_even =0
    for i in range(n+1):
        total += i
        if i % 2 == 0:
            total_even += i
        else:
            total_odd += i
    return total, total_even, total_odd

def convert_celsius_to_fahrenheit(degree):
    return (degree * 9/5) + 32

def convert_fahrenheit_to_celsius(degree):
    return (degree - 32) * 5/9

print(convert_fahrenheit_to_celsius(70))


def check_season(month):
    Autumn = ['September','October','November']
    Spring = ['March','April','May']
    Summer = ['June','July','August']
    Winter = ['December','January','February']
    if month in Autumn:
        return "Autumn"
    elif month in Spring:
        return "Spring"
    elif month in Summer:
        return "Summer"
    elif month in Winter:
        return "Winter"
    else:
        return "Invalid month"
    
# a = input('Enter a month: ')
# print(check_season(a))

def calculate_slope(x1=2,y1=3,x2=4,y2=5):
    slope = (y2 - y1) / (x2 - x1)
    return slope

def solve_quadratic_eqn(a,b,c):
    a = 1
    b = -5
    c = 6
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        return root1, root2
    
def reverse_list(my_list):
    my_list.reverse()
    return my_list

print(reverse_list([1,2,3,4,5]))

def capitalize_list_items():
    my_list = ['apple', 'banana', 'cherry']
    capitalized_list = [item.capitalize() for item in my_list]
    return capitalized_list
print(capitalize_list_items())

def remove_item(a,b):
    a.remove(b)
    return a

print(remove_item(['a','b','c'],'c'))



print(add_all_nums(200))
"""
# Ex2

def evens_add_odds(n):
    even = 0
    odd = 0
    for i in range(n+1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(evens_add_odds(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(fac(3))

def is_empty(data):
    if not data:
        return True
    else:
        return False
    
def calculate_mean(n):
    return sum(n) / len(n)

def calculate_median(n):
    n.sort()
    if len(n) % 2 == 0:
        return (n[len(n)//2 - 1] + n[len(n)//2]) 
    else:
        return n[len(n)//2]
# Ex3  
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    
def check_all_unique_item_list(n):
    return len(n) == len(set(n))






