# Character ASCII Values:
# ○ Given a string, create a dictionary where keys are characters, and values are
# their ASCII values.

my_str = "Dictionary"
my_dict = {x: ord(x) for x in my_str}
print(my_dict)
