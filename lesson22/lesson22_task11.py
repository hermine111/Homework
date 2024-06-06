# 11. Function Exercise:
# Write a function that checks if a given string is a valid email address.


import re


def valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print(valid_email("gdasffg.haeruu4@5645.ilru"))