# 4)Count how many uppercase and lowercase characters are in this sentence.(“The Quick
# Brown Fox”)


sentence = "The Quick Brown Fox"
upper_count = 0
lower_count = 0
for x in sentence:
    if x.isupper():
        upper_count += 1
    if x.islower():
        lower_count += 1
print(upper_count)
print(lower_count)

