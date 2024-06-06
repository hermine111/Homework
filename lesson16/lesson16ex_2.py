# 2. Write a python program to catch error a num dividing by zero.

try:
    quantity = 10
    print(quantity/0)
except ZeroDivisionError as e:
    print(e)
