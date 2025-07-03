import random
import string

def generate_password(length):
    if length < 4:
        print("Password should be at least 4 characters long for good complexity.")
        return None

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure minimum complexity: one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices
    password += random.choices(all_chars, k=length - 4)

    # Shuffle for true randomness
    random.shuffle(password)

    return ''.join(password)

# Prompt user
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    if password:
        print(f"🛡️ Your generated password: {password}")
except ValueError:
    print("❌ Please enter a valid number.")