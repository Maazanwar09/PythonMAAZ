def reverse_words_in_string(s):
    words = s.split()
    return ' '.join(reversed(words))

text = input("Enter a sentence: ")
print(reverse_words_in_string(text))
