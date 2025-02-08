def isPerfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    return sum==n

n=int(input("Enter a number:"))
if(isPerfect(n)):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a not perfect number")
