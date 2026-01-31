import string
import random

def generate_password(length=12):
    char = string.ascii_letters +string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password

print("Generated Password:", generate_password(16))
