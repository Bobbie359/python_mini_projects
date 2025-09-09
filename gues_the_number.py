import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    guess = None  # Ensure guess is always defined
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()