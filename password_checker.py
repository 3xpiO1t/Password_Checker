import re
#Define a function for checking the password length
def password_strength(password):
    # Check length
    if len(password) < 6:
        return "Weak"
    
    # Initialize criteria for a password
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Check password conditions
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif re.match(r'[!@#$%^&*(),.?":{}|<>]', char):
            has_special = True
    
    # Evaluate strength based on conditions
    if has_upper and has_lower and has_digit and has_special and len(password) >= 8:
        return "Strong"
    elif (has_upper or has_lower) and (has_digit or has_special) and len(password) >= 6:
        return "Moderate"
    else:
        return "Weak"

# Test the function
password = input("Enter a password: ")
strength = password_strength(password)
print(f"Password Strength: {strength}")
