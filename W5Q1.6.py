import math

def find_distance_between_two_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
print(f"Distance between points: {find_distance_between_two_points(x1, y1, x2, y2)}")
