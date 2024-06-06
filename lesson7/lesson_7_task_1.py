# 1.Arrange
# Arrange string characters such that lowercase letters should come first
# Sample Input Sample Output
# PyNaTive
# yaivePNT


word = input("Enter:")
lower_case = []
upper_case = []
for x in word:
    if x.islower():
        lower_case.append(x)
    else:
        upper_case.append(x)
word_res = "".join(lower_case + upper_case)
print(word_res)
















































