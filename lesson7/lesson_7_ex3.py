#3)Write a Python program that input a sentence and return the longest word and the length
#of the longest one.


sentence = "My heart is in the highlands."
sent1 = sentence.split()
longest = sent1[0]
for word in sent1:
    if len(word) > len(longest):
        longest = word
print(longest)
print(len(longest))



