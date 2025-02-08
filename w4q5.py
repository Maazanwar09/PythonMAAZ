def sumDigits(n):
    sum=0
    while(n>0):
        sum+=n%10
        n//=10
    return sum

n=int(input("Enter number:"))
print(f"Sum of digits of {n} is",sumDigits(n))
