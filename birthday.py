import datetime

def calculate_age_and_birthday_countdown():
    # Get current date
    current_date = datetime.datetime.now()
    
    # Prompt the user to enter their birth year, month, and day
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (MM): "))
    birth_day = int(input("Enter your birth day (DD): "))
    
    # Create a datetime object for the birth date
    birth_date = datetime.datetime(birth_year, birth_month, birth_day)
    
    # Calculate age
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    # Calculate next birthday
    next_birthday_year = current_date.year if (current_date.month, current_date.day) < (birth_date.month, birth_date.day) else current_date.year + 1
    next_birthday = datetime.datetime(next_birthday_year, birth_month, birth_day)
    
    # Calculate days until next birthday
    days_until_birthday = (next_birthday - current_date).days
    
    # Display the results
    print(f"\nYour current age is: {age} years old")
    print(f"Your next birthday is on: {next_birthday.strftime('%Y-%m-%d')}")
    print(f"Days remaining until your next birthday: {days_until_birthday} days")

if __name__ == "__main__":
    calculate_age_and_birthday_countdown()