# Exercise 9:
# Reverse Words in a Sentence: Write a function that takes a sentence as input and returns the
# sentence with the words reversed. For example, "Hello world" should become "world Hello". Use
# string slicing to accomplish this task.

def reverse_words(sentence):
    words = sentence.split()
    reversed_sent = " ".join(words[::-1])
    return reversed_sent
print(reverse_words("I love life"))
