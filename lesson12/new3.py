# Exercise 3:
# List Comprehension Write a Python function called square_even_numbers that takes a list of
# integers as an argument and returns a new list containing the squares of only the even numbers
# from the input list.
def square_even_numbers(list_ex):
    list_res = []
    for x in list_ex:
        if x % 2 == 0:
            list_res.append(x**2)
    return list_res
print(square_even_numbers([2,8,7,5]))
