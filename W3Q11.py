import math
def is_perfect_squar(n):
    return math.sqrt(n)**2==n
def is_fibonacci(num):
    return is_perfect_squar(5*num*num+4) or is_perfect_sqaur(5*num*num-4)
num = int(input("enter a number : "))
if is_fibonacci(num):
   print(f"{num} is fibonacci number")
else:
     print(f"{num} is not a fibonacci number ")
