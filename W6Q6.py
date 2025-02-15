a = float(input("Enter first side of the triangle: "))
b = float(input("Enter second side of the triangle: "))
c = float(input("Enter third side of the triangle: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"The area of the triangle is: {area:.2f}")
   
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")
