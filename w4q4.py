def factorial(n):
    fact=1
    for i in range(n,1,-1):
        fact*=i
    print(f"Factorial of {n} is: {fact}")

n=int(input("Enter a number: "))
factorial(n)
