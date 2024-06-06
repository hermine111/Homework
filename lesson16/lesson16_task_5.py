# Type Conversion:
# Write a function that prompts the user to enter a number and tries to convert it to an
# integer. Handle the TypeError exception by printing a message indicating that the input
# is not a valid number. Use a finally block to print "Type conversion process completed."




def my_fun(n):
    try:
        n = int(n)
    except TypeError as e:
        print("Input is not a valid number!")
    finally:
        print("Type conversion process completed.")
    return n
print(my_fun(78.89))


