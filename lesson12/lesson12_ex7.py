
# 7 Exercise 7:
# Password Strength Checker: Write a function that takes a password as input and returns a
# string indicating its strength. For simplicity, assume a password is strong if it has at least 8
# characters, contains both uppercase and lowercase letters, and at least one special character.



def check_password_strength(password):
    length_ = len(password) >= 8
    uppercase_ = False
    lowercase_ = False
    special_char = False

    special_characters = set('!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?`~')
    for char in password:
        if char.isupper():
            uppercase_ = True
        elif char.islower():
            lowercase_ = True
        elif char in special_characters:
            special_char = True

    if length_ and uppercase_ and lowercase_ and special_char:
        return "Strong: Password meets all criteria."
    else:
        strength = "Weak: Password is missing the following criteria:"
        if not length_:
            strength += " At least 8 characters."
        if not uppercase_:
            strength += " Uppercase letter(s)."
        if not lowercase_:
            strength += " Lowercase letter(s)."
        if not special_char:
            strength += " Special character(s)."
        return strength
print(check_password_strength("789piiuyYT*^&"))

















