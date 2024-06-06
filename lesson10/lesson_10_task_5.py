#  Exercise 5:
# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.





n = int(input("Enter a number : "))
i = 1
a = 0
b = 1
sum_n = a + b
while i <= n:
    sum_n = a + b
    i += 1
    print(a, end="  ")
    a = b
    b = sum_n
    sum_n = a + b



