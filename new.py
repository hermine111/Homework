list1 = [1, 2, 3, 4, 10]
list2 = [1, 2, 56, 5, 10, 89, 45, 9]
list3 = [5, 2, 8, 10, 78, 77, 45, 62]
common_el1 = list(set(list1).intersection(list2, list3))
print(common_el1)
common_el2 = list(set(list1).intersection(list2))
print(common_el2)
r_list1 = []
r_list2 = []
r_list3 = []
for x in list1:
    if x not in list2:
        r_list1.append(x)
for x in list2:
    if x not in list3:
        r_list2.append(x)
for x in list3:
    if x not in list1:
        r_list3.append(x)
print(set(r_list1))
print(set(r_list2))
print(set(r_list3))







