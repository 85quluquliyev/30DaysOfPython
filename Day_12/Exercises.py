# Ex1
"""
import random
import string
def random_user_id():
    user_id = ''.join(random.choices(string.ascii_letters, k=6))
    return user_id
    
print(random_user_id())

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
"""
# Ex2
"""
import random

def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hex_colors.append(color)
    return hex_colors

number_of_colors = 5  
colors = list_of_hexa_colors(number_of_colors)
print(colors)


def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"rgb({r}, {g}, {b})"
        rgb_colors.append(color)
    return rgb_colors

number_of_colors = 5  
colors = list_of_rgb_colors(number_of_colors)
print(colors)
"""

# Ex3

import random

def shuffle_list(original_list):
    shuffle_list = original_list.copy()
    random.shuffle(shuffle_list)
    return shuffle_list

my_list = ['Qulu','Abdul','Ruslan',"Erto"]
shuffled = shuffle_list(my_list)
print("Orijinal liste:", my_list)
print("Karıştırılmış liste:", shuffled)
print(random.choice(shuffled))


def unique_random_numbers():
    unique_numbers = random.sample(range(10),7)
    return unique_numbers

numbers = unique_random_numbers()
print("Benzersiz rastgele sayılar:", numbers)

    