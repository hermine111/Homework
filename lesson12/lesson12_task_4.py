# Exercise 4: Find Index Function
# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.

def index_of_element(list_ex, search_element):
    result = -1
    for i in range(len(list_ex)):
        if list_ex[i] == search_element:
            result = i
    return result
print(index_of_element(["bread","butter","sugar","coffee"], "coffee"))
