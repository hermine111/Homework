# 3.Factorial
# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
# Sample Input Sample Output
# factorial(5)
# 120

# option 1
def factorial(number):
    if number == 0:
        return 1
    else:
        return number*(factorial(number - 1))


print(factorial(8))


# option 2
def factorial(number):
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1
    return result


print(factorial(4))
