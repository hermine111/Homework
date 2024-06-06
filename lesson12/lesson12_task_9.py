#  Exercise 9: Print Prime Numbers Function
# Write a function that prints all prime numbers up to a given limit.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)


print_primes(99)



