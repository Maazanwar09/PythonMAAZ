def exchange_values(a, b):
    return b, a

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
a, b = exchange_values(a, b)
print(f"After exchange, first number is: {a}, second number is: {b}")
