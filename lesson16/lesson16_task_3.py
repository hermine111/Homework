# URL Validator
# 3. Write a function that validates a URL string. Handle the ValueError by raising a custom
# exception if the URL format is invalid.Write a function that removes an element at a
# specified index from a list. Handle the IndexError by raising a custom exception if the
# index is out of range.


def is_string_an_url(url_string):
    if "http://" or "https://" in url_string:
        return True
    else:
        return False


print(is_string_an_url("https://elt.oup.com/student/englishfile/"))




