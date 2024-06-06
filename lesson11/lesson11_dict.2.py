# 2.Write a python program which concat 2 dicts.


dict1 = {"Country": "Artsakh", "Birthplace": "Stepanakert"}
dict2 = {"favourite place": "Katarot", "Favourite book": "La Peau de Chagrin"}
concatenated_dict = {}

for key, value in dict1.items():
    concatenated_dict[key] = value

for key, value in dict2.items():
    concatenated_dict[key] = value

print(concatenated_dict)


