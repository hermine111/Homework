# 7): Prime number checker
# Develop a program that checks if a given number is prime using a while loop. Ask
# the user for input and print whether the number is prime or not.



num = int(input("Enter a number :"))
i = 2
res = False
while   i <= int(num/2):
    if num % i == 0:
        res = True
        break
    else:
        i += 1
if num == 1:
    print(num, "is not a prime number")
elif res == False:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")













