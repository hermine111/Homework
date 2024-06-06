# Find and Replace:
# Implement a Python program that reads a text file (input.txt), prompts the user
# for a word to find, and another word to replace it with. Replace all occurrences of
# the first word with the second word and save the modified text to a new file
# (output.txt).


with open("lesson14_2_input.txt", "r") as file:
    content = file.read()
    search_word = "more"
    replace_word = "less"
    content = content.replace(search_word, replace_word)

with open("lesson14_2_output.txt", "w") as file:
    file.write(content)

