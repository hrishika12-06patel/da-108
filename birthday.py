from datetime import datetime

def calculate_age_and_birthday(birth_year, birth_month, birth_day):
    today = datetime.today()
    birth_date = datetime(birth_year, birth_month, birth_day)
    
    # Calculate age
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_month, birth_day))
    
    # Determine next birthday
    next_birthday = datetime(today.year, birth_month, birth_day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birth_month, birth_day)
    
    # Calculate days until next birthday
    days_until_birthday = (next_birthday - today).days
    
    return age, days_until_birthday

# Get user input
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_day = int(input("Enter your birth day (DD): "))

# Compute age and countdown
age, days_until_birthday = calculate_age_and_birthday(birth_year, birth_month, birth_day)

# Display results
print(f"You are {age} years old.")
print(f"There are {days_until_birthday} days left until your next birthday.")
