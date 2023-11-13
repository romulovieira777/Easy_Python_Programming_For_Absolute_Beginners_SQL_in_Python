import math


circle = input("Please enter the Radius of the Circle: ")
circle_float = float(circle)
area_of_circle = round(math.pi * pow(circle_float, 2), 2)

print(f"The Area of your Circle with the radius {circle} is: {area_of_circle}")
