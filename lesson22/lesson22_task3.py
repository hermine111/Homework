# 3. List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.

def sum_nums_div_by_7(numbers):
    count = 0
    for num in numbers:
        if num % 7 == 0:
            count += num
    return count
print(sum_nums_div_by_7([78,7,5,77,21,280]))
