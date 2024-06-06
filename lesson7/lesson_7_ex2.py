#2)Write a Python script that takes a list of words and return the longest word and the
#length of the longest one.


items = ["price", "quantity", "value"]
longest = items[0]
for word in items:
    if len(word) > len(longest):
        longest = word
print(longest)
print(len(longest))

