#2.Largest
#Write a Python program to get the largest number from a list.
#Sample Input Sample Output
#[1, 2, 3, 4] 4
#[5, 7, 3, 9, 11] 11
#[25, 1,1, 13] 25
#[1, 2, 1, 1] 2



numbers = [5, 4, 96, 55, 77, 105]
largest = numbers[0]
for num in numbers:
        if  num > largest:
            largest = num
print(largest)

























