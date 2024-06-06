# Character Frequency:
# ○ Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string.


my_str = "Fantastic"
my_dict = {x: my_str.count(x)for x in my_str}
print(my_dict)
