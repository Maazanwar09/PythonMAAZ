def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = {vowel: text.count(vowel) for vowel in vowels if vowel in text}
    return vowel_count

text = input("Enter a text: ")
vowel_counts = count_vowels(text)
print(f"Vowel counts: {vowel_counts}")
