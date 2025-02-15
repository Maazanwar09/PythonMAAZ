def check_consecutive(lst):
    lst.sort()

    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1] + 1:
            return False
    return True

my_list = list(map(int, input("Enter numbers (comma-separated): ").split(',')))
if check_consecutive(my_list):
    print("The list contains consecutive integers.")
else:
    print("The list does not contain consecutive integers.")
