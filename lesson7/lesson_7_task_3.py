# 3.Balance
# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter.
# Sample Input Sample Output
# s1 = "Yn"
# s2 = "PYnative"
# True
# s1 = "Ynf"
# s2 = "PYnative"
# False


s1 = input("Enter:")
s2 = input("Enter:")
res = True
for x in s1:
    if x not in s2:
        res = False
        break
print(res)












































