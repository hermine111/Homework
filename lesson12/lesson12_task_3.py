#  Exercise 3: Average Function
# Write a function that calculates the average of a list of numbers.


def average_of_list_numbers(list_ex):
    sum_num = 0
    for i in range(len(list_ex)):
        sum_num += list_ex[i]
    result = sum_num / len(list_ex)
    return result
print(average_of_list_numbers([5,4,0.5,7]))
