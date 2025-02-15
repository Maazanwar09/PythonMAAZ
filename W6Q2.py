num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
smallest = num1  
if num2 < smallest:
    smallest = num2
else:
    smallest = smallest
if num3 < smallest:
    smallest = num3
else:
    smallest = smallest
print("The smallest number is:", smallest)
