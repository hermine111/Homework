#You are given three lists, list1, list2, and list3. Your task is to implement a
#programm that takes these lists and prints the following:
#The set of elements that are common to all three lists.
#The set of elements that are present in at least two of the three lists, but not in all
#three.
#The set of elements that are unique to each list (present in only one list)



list1 = [1, 2, 3, 4, 10]
list2 = [1, 2, 56, 5, 10, 89, 45, 9]
list3 = [5, 2, 8, 10, 78, 77, 45, 62]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

common_to_all = set1 & set2 & set3
at_least_two = (set1 & set2 | set1 & set3 | set2 & set3) - common_to_all
unique_to_list1 = set1 - set2 - set3
unique_to_list2 = set2 - set1 - set3
unique_to_list3 = set3 - set1 - set2

print(common_to_all)
print(at_least_two)
print(unique_to_list1 | unique_to_list2 | unique_to_list3)

















