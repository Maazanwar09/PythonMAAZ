a = int(input("Enter the first integer : "))
b = int(input("Enter the Second integer : "))
a = a ^ b
b = a ^ b
a = a ^ b
print(f" after swapping : a={a}, b={b} ")
