import random
import string

# Display your name and registration number
def display_info():
    print("Name: Faisal")
    print("Registration Number: ABC123456")
    print("-" * 50)

# Generate a secure password
def generate_password(length=12):
    if length < 12:
        raise ValueError("Password length must be at least 12 characters.")

    # Define character set: uppercase, lowercase, digits, special characters
    char_set = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(char_set, length))
    return password

# Main function
if __name__ == "__main__":
    display_info()
    print("Generating a secure password...")
    print("-" * 50)
    password = generate_password(16)  # Adjust the length as needed
    print(f"Generated Password: {password}")
    print("-" * 50)
    display_info()
