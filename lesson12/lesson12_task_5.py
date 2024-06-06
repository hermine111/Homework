# Exercise 5: Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n.


def square_sum(n):
    sum_num = 0
    for i in range(1, n+1):
        sum_num = sum_num+(i*i)
    return sum_num
print(square_sum(7))


