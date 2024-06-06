# 2)Get the same items in two ranges using
# nested loop.(0, 10), (5,15)


list_res = []
for x in range(0, 11):
    for y in range(5, 16):
        if x == y:
            list_res.append(x)
print(list_res)


