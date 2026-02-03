# Import required modules
import string
import random

# Function to generate a random password
def generate_password(length=12):
     # Combine all possible characters
    char = string.ascii_letters +string.digits + string.punctuation
    # Generate password by randomly choosing characters
    password = ''.join(random.choice(char) for _ in range(length))
    return password

# Generate and print a 16-character password
print("Generated Password:", generate_password(16))
