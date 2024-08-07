def get_user_input():
    while True:
        try:
            guess = int(input("Your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")
