r1 = int(input("Enter the starting number (r1) : "))
r2 = int(input("Enter the ending number (r2): "))

if r1 < r2:
    num_list = list(range(r1, r2 + 1))
    print("The list of numbers in the given range is:", num_list)
else:
    print("Invalid input: Ensure that r1 is less than r2.")
