#1) Check if a value exists in a dictionary

diction = {"Mariam": "20", "Ani": "25", "Marta": "10"}
res = False
val = "20"
for x in diction:
    if diction[x] == val:
        res = True
        break
print(res)