import re

def is_valid_username(username):
    if len(username) < 5:
        return False
    if re.search(r'[^a-zA-Z0-9]', username):
        return False
    return True

def main():
    username = input("Enter a username: ").strip()
    
    if is_valid_username(username):
        print("Valid username.")
    else:
        print("Invalid username.")

if __name__ == "__main__":
    main()