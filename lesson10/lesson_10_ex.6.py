#6): Sum of Digits
#Write a Python program that takes a positive integer as input and calculates the sum
#of its digits. For example, if the input is 12345, the output should be 15 (1 + 2 + 3 + 4
#+ 5 = 15). Use a while loop to perform this task.

num = int(input("Enter a number :"))
sum_digit = 0
i = 1
while i <= num:
    if num != 0:
        sum_digit = sum_digit + num % 10
        num = num//10
print(sum_digit)






