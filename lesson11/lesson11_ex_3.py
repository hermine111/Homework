# 3. Write a Python function to return the even numbers from a given list. Sample
# List
# : [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_even_numbers_from_a_list(list_ex):
    result = []
    for num in list_ex:
        if num % 2 == 0:
            result.append(num)
    return result
print(get_even_numbers_from_a_list( [4,8,7,9,6,55]))


