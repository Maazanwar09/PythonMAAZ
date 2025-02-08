def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


sentence = input("Enter a sentence: ")
print(count_word_occurrences(sentence))
