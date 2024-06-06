# 1. Write a python program to read the whole text of a file and catch the
# error if files does not exists.




try:
    with open("text1.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(e)