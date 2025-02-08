a = int(input("enter the first nuber : "))
b = int(input("enter the second nuber : "))
while b:
    a,b = b,a%b
print(f" GCD is {a}")
