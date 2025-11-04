import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters  # A-Z + a-z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters

    # Combine all characters
    all_characters = letters + digits + symbols

    # Ensure at least one of each type if length allows
    if length < 4:
        print("Password length should be at least 4 characters for good security.")
        return None

    # Randomly select characters
    password = (
        random.choice(string.ascii_lowercase) +
        random.choice(string.ascii_uppercase) +
        random.choice(string.digits) +
        random.choice(string.punctuation)
    )

    # Fill the rest randomly
    password += ''.join(random.choices(all_characters, k=length - 4))

    # Shuffle to avoid predictable pattern
    password = ''.join(random.sample(password, len(password)))

    return password


# === Main Program ===
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print(f"\nYour generated password is: {password}")
except ValueError:
    print("Please enter a valid number.")
