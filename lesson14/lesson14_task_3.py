# File Concatenation:
# Write a Python script that takes multiple text files as input and concatenates their
# contents into a single text file.


with open("lesson14_3_f1.txt", "r") as file1:
    content1 = file1.read()
with open("lesson14_3_f2.txt", "r") as file2:
    content2 = file2.read()
with open("lesson14_3_f3.txt", "r") as file3:
    content3 = file3.read()

with open("lesson14_3_concatenated.txt", "w") as concatenated_file:
    concatenated_file.write(content1 + content2 + content3)



