# 5)Write a Python program that prints all
# the numbers from 0 to 7 except 3 and 6.


for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    print(i, end='')
