import string
import random

class PasswordGenerator:
    def __init__(self, length=8, uppercase=False, digits=False, special_chars=False):
        self.length = length
        self.uppercase = uppercase
        self.digits = digits
        self.special_chars = special_chars

    def generate_password(self):
        characters = string.ascii_lowercase

        if self.uppercase:
            characters += string.ascii_uppercase

        if self.digits:
            characters += string.digits

        if self.special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

def generate_password_simple():
    print("Welcome to the Password Generator!")
    print("This tool will generate a random password for you.")

    while True:
        try:
            length = int(input("Enter the length for the password: "))
            password_generator = PasswordGenerator(length=length)
            generated_password = password_generator.generate_password()
            print(f"Generated password: {generated_password}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the length.")

if __name__ == "__main__":
    generate_password_simple()
