def letterCount(s):
    lcount=0
    ucount=0
    for c in s:
        if(c.isupper()):
            ucount+=1
        elif(c.islower()):
            lcount+=1
    print(f"Number of lower case letters= {lcount}")
    print(f"Number of upper case letters= {ucount}")

s=input("Enter a string:")
letterCount(s)
