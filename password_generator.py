import random

print("====================================")
print("      NUMBER GUESSING GAME")
print("====================================")

print("\nChoose Difficulty Level:")
print("1. Easy (1 - 50)")
print("2. Medium (1 - 100)")
print("3. Hard (1 - 200)")

choice = input("\nEnter your choice (1/2/3): ")

if choice == "1":
    limit = 50
elif choice == "2":
    limit = 100
elif choice == "3":
    limit = 200
else:
    print("\n❌ Error: Invalid Choice!")
    print("Please run the program again and enter only 1, 2, or 3.")
    exit()

secret_number = random.randint(1, limit)
attempts = 0

print(f"\nI have selected a number between 1 and {limit}.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > limit:
            print(f"⚠ Please enter a number between 1 and {limit}.")
        elif guess < secret_number:
            print("📉 Too Low! Try Again.")
        elif guess > secret_number:
            print("📈 Too High! Try Again.")
        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the correct number: {secret_number}")
            print(f"Total Attempts: {attempts}")
            print("Thanks for playing!")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")