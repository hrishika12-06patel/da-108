import string

def check_password_strength(password):
    # Boolean checks
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Integer checks
    length = len(password)

    # Categorize password strength
    if length < 6:
        return "Weak", "Password is too short. Try using at least 6 characters."
    elif has_upper and has_lower and has_digit and has_special:
        return "Strong", "Strong password! Great job!"
    elif has_upper or has_lower and has_digit:
        return "Medium", "Medium password. Try adding a special character for a stronger password."
    else:
        return "Weak", "Weak password. Try using numbers and special characters."

# Feedback loop
def password_feedback_loop():
    passwords = []  # List to store previously entered passwords
    while True:
        password = input("Enter a password: ")
        passwords.append(password)
        
        strength, feedback = check_password_strength(password)
        print(feedback)
        
        if strength == "Strong":
            break

if __name__ == "__main__":
    password_feedback_loop()