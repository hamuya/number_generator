from number_generator import generate_number
from user_input import get_user_input

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    number_to_guess = generate_number()
    attempts = 0

    while True:
        guess = get_user_input()
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess < number_to_guess:
            print("Too low! Try a higher number.")
        elif guess > number_to_guess:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! The correct number was {number_to_guess}.")
            print(f"You guessed it in {attempts} attempts.")
            break
