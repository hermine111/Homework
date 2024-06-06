#4.Second smallest
#Write a Python program to find the second smallest number in a list.
#Sample Input Sample Output
#[1, 2, 3, 4] 2
#[5, 7, 3, 9, 11] 5
#[25, 1,1, 13] 1

numbers = [1, 5,2, 7, 10, 56, 78, 99]
smallest = numbers[0]
second_smallest = numbers[1]

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num


print(second_smallest)






