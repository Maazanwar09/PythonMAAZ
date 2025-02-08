num = int(input(" Enter an Integer ; "))
if num < 2:
    print(f"{num} is not a prime number")
else:
    for i in range (2,int(num**0.5)+1):
        if num % i ==0:
           print(f"{num} is not a prime number , first factor:{i}")
           break
    else:
                   print(f"{num} is prime number")
