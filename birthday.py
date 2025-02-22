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
    
    return age, next_birthday.strftime('%Y-%m-%d'), days_until_birthday

# Example usage
if __name__ == "__main__":
    birth_year = 1995  # Replace with actual values
    birth_month = 12
    birth_day = 25
    
    age, next_birthday, days_until_birthday = calculate_age_and_birthday(birth_year, birth_month, birth_day)
    
    print(f"You are {age} years old.")
    print(f"Your next birthday is on {next_birthday}.")
    print(f"Days remaining until your next birthday: {days_until_birthday}")
