import string

# Function to evaluate the strength of a password
def evaluate_password(password):
    """Evaluate the strength of a password."""
    # Check for the presence of different character types
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    length = len(password)
    
    # Categorizing password strength based on criteria
    if length < 6:
        return "Weak", "Password too short. Use at least 6 characters."
    elif has_upper and has_lower and has_digit and has_special:
        return "Strong", "Great job! Your password is strong."
    elif (has_upper or has_lower) and has_digit:
        return "Medium", "Consider adding special characters to strengthen your password."
    else:
        return "Weak", "Use a mix of uppercase, lowercase, numbers, and special characters."

# Function to continuously prompt user until a strong password is entered
def password_checker():
    """Continuously prompt user until a strong password is entered."""
    password_attempts = []  # List to store previously entered passwords
    
    while True:
        password = input("Enter a password: ")  # Prompt user for password input
        password_attempts.append(password)  # Store the entered password
        strength, message = evaluate_password(password)  # Evaluate password strength
        print(message)  # Provide feedback to the user
        
        if strength == "Strong":  # Exit loop if password is strong
            break
    
    print("Passwords entered:", password_attempts)  # Display password history

# Entry point of the program
if __name__ == "__main__":
    password_checker()
