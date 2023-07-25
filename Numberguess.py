import random

def number_guess():
    print("Welcome to the Number Guessing Game!")
    print("The numbers valid here are between 1 and 100.")
    target_number = random.randint(1, 100)

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts!")
            break

