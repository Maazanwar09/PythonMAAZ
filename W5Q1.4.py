import math

def find_circumference_of_circle(radius):
    return 2 * math.pi * radius

radius = float(input("Enter radius of the circle: "))
print(f"Circumference of circle: {find_circumference_of_circle(radius)}")
