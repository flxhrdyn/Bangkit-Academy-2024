# creating a module to calculate areas
import math # import math module 

# function to calculate area of a triangle
def triangle(base, height):
    return base*height/2

# function to calculate area of a rectangle
def rectangle(base, height):
    return base*height

# function to calculate area of a circle
def circle(radius):
    return math.pi*(radius**2)
