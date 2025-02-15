num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
greatest = num1  
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
print("The greatest number is:", greatest)
