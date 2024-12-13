import random

def guess_my_number():
    number_to_guess = random.randint(1, 100)
    print("I have a number between 1 and 100... can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your number: "))
            if user_guess < number_to_guess:
                print("Too low!")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess}.")
                break
        except ValueError:
            print("Invalid input. Please enter a number")

guess_my_number()