# 5): Write a program that calculates the sum of
# numbers from 1 to a user-defined limit using a
# while loop.


num = input("Enter:")
sum_1 = 0
i = 1
while i <= int(num):
    sum_1 = sum_1+i
    i += 1
print(sum_1)
