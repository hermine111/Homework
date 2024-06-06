# Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.



# option 1
my_dict1 = {"January": 30, "February": 28, "March": 31}
my_dict2 = {"April": 30, "May": 31, "_June": "30"}
merged_dict = {k: v for k, v in my_dict1.items() | my_dict2.items() if not k.startswith("_")}
print(merged_dict)


# option 2
merged_dict = {k: v for k, v in my_dict1.items() if not k.startswith("_")}
merged_dict.update({k: v for k, v in my_dict2.items() if not k.startswith("_")})
print(merged_dict)
