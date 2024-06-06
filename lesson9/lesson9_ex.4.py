# 4)Count how many even and odd numbers
# are in given range (10,35).

count_odd = 0
count_even = 0
for x in range(10, 35):
    if x % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(count_odd)
print(count_even)



