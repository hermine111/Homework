# 1
#Character Count:
#Write a Python script that reads a text file (input.txt) and counts the
#occurrences of each character (including spaces and punctuation). Output the
#character frequency to another text file (output.txt)



with open("lesson14_1_input.txt","r") as file:
    content = file.read()
    frequency = dict()
    for char in content:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for key, value in frequency.items():
        print(f"Character {key} occurs {value} times")

with open("lesson14_1_output.txt", "w") as file:
    for key, value in frequency.items():
        file.write(f"Character {key} occurs {value} times \n")





