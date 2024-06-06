# Vowels in a Word:
# ○ Create a list of vowels present in a given word.

vowels = ["a", "e", "o", "u", "i"]
word = "Motherland"
lst = [x for x in word.lower() if x in vowels]
print(lst)
