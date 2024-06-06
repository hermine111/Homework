# Exercise 3:
# Write a Python program that calculates the sum of all even numbers between 1 and 100
# using a while loop


# option 1
i = 0
sum_num = 0
while i <= 100:
    sum_num = sum_num + i
    i += 2
print(sum_num)

# option 2

i = 0
sum_num = 0
while i <= 100:
    if i % 2 == 0:
        sum_num = sum_num + i
    i += 1
print(sum_num)





