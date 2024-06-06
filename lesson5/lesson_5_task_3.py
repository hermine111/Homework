#3.Smallest
#Write a Python program to get the smallest number from a list.
#Sample Input Sample Output
#[1, 2, 3, 4] 1
#[5, 7, 3, 9, 11] 3
#[25, 1,1, 13] 1
#[1, 2, 1, 1] 1

numbers = [56, 78, 14, 2, 45, 5, 8, -1, 0]
smallest = numbers[0]
for num in numbers:
     if num < smallest:
        smallest = num
print(smallest)


