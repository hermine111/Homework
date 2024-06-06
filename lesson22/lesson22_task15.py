# 15. Multiple Exceptions:
# Write a function that performs the following tasks:
# Accepts a list and an index as input.
# Attempts to access the element at the given index in the list.
# Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not.


def access_element(list_ex, index):
    try:
        element = list_ex[index]
        return element
    except IndexError:
        print("The index is out of range for the given list.")
    finally:
        print("Task completed")


print(access_element([45, 78, 25, 44, 12], 3))