def sum_numbers_from_list(input_list):
    total = 0
    for item in input_list:
        if isinstance(item, (int, float)):
            total += item
    return total

my_list = [1, 'a', 3, 'hello', 5.5, 7]
result = sum_numbers_from_list(my_list)
print(result)
