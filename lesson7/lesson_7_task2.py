#2.Count
#Count all letters, digits, and special symbols from a given string
#Sample Input Sample Output
#P@#yn26at^&i5ve Total counts of chars, digits, and
#symbols
#chars = 8
#digits = 3
#symbol = 4



txt = input("Enter:")
letters = 0
digits = 0
symbols = 0
for x in txt:
    if ord(x)>= 65 and ord(x)<=90 or ord(x) >= 97 and ord(x)<=122:
        letters += 1
    elif ord(x) >= 48 and ord(x)<=57:
            digits += 1
    else:
            symbols += 1
print(letters)
print(digits)
print(symbols)















