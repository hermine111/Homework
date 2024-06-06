# Exercise 3:
# Print a right-angled triangle pattern using a nested for loop. The pattern should have 5
# rows.


# option 1

rows = 5
for i in range(1, rows + 1):
    print("* " * i)



# option 2

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()























