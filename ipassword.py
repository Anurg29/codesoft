import random
import string

def generate_password(length):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets into one
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Check if the length is at least 6 characters
    if length < 4:
        print("Password length should be at least 6 characters.")
        return None

    # Generate a password with random characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Main code
if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the length of the password: "))
            password = generate_password(password_length)

            if password:
                print("Generated Password:", password)
            break
        except ValueError:
            print("Please enter a valid integer for password length.")
