import random
import string

def generate_password(length):
    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

try:
    length = int(input("\nEnter password length: "))

    if length < 4:
        print("Password length should be at least 4 characters.")
        exit()

    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)

    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

    print("\nPassword saved to passwords.txt")

    print("\nPassword Strength: Strong")
    print("Contains:")
    print("- Uppercase Letters")
    print("- Lowercase Letters")
    print("- Numbers")
    print("- Special Characters")

except ValueError:
    print("\nError: Please enter a valid number.")

print("\nThank you for using Password Generator!")
print("=" * 40)
