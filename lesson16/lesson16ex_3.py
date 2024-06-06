#3. Write a python program that will raise an exception (Invalid
# File) if text file contents first symbol is starting with number


with open("text.txt", "r") as file:
    if file.read(1).isdigit():
        raise Exception("Invalid file")
