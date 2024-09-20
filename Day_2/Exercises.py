import math

# The radius of a circle is 30 meters.
radius = 30
pi = 3.14

area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius

print("Area: ", area_of_circle)
print("Circumference: ", circum_of_circle)

user_radius = float(input('Enter the radius of the circle: '))

user_area = pi * user_radius**2

print("User Area: ",user_area)