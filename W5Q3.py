def remove_odd_index_characters(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)

text = input("Enter a string: ")
print(remove_odd_index_characters(text))
