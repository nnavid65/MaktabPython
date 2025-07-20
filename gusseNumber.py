# Mode 1 the user guesses the number

import random

machine_number_to_guess = 0
user_feedback = ''  
first_guess = 0
second_guess = 0
third_guess = 0

def user_guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

def machine_guess_number():
    global machine_number_to_guess, user_feedback, first_guess, second_guess, third_guess,attempts
    machine_number_to_guess = random.randint(1, 100)
    attempts = 1
    print(f'Is your number {machine_number_to_guess}?  (yes/no)')
    print("If the guess is too high, type 'lower'. If the guess is too low, type 'higher'. If correct, type 'yes'.")
    user_feedback = input("Enter your feedback: ").strip().lower()
    while user_feedback != 'yes':
        if user_feedback == 'lower':
            attempts += 1
            choose_lower()
        elif user_feedback == 'higher':
            attempts += 1
            choose_higher()
        elif user_feedback == 'yes':
            print(f"Machine guessed your number {machine_number_to_guess} in {attempts} attempts.")
            return
        else:
            print("Invalid input. Please enter 'lower', 'higher', or 'yes'.")
            user_feedback = input("Enter your feedback: ").strip().lower()  


            
def choose_lower():
    global first_guess, second_guess, third_guess, user_feedback, machine_number_to_guess, attempts
    attempts += 1
    upper_bound = machine_number_to_guess
    while user_feedback != 'yes':
        if user_feedback == 'lower':
            machine_number_to_guess = random.randint(1, upper_bound - 1)
            print(f"LOWWWER Is Machine guesses lower than? {machine_number_to_guess}.")
            user_feedback = input("Enter your feedback: ").strip().lower()
            attempts += 1
        elif user_feedback == 'higher':
            lower_bound = machine_number_to_guess
            machine_number_to_guess = random.randint(lower_bound + 1, upper_bound)
            print(f"LOWWWER Is Machine guesses higher than? {machine_number_to_guess}.")
            user_feedback = input("Enter your feedback: ").strip().lower()
            attempts += 1
            if user_feedback == 'lower':
                upper_bound = machine_number_to_guess - 1
                machine_number_to_guess = random.randint(lower_bound + 1, upper_bound)
                print(f"LOWWWER Is Machine guesses lower than? {machine_number_to_guess}.")
                user_feedback = input("Enter your feedback: ").strip().lower()
                attempts += 1
        elif user_feedback == 'yes':
            print(f"LOWWWER Machine guessed your number {machine_number_to_guess} in {attempts} attempts.")
            return attempts
        
        
def choose_higher():
    global first_guess, second_guess, third_guess, user_feedback, machine_number_to_guess, attempts
    attempts += 1
    lower_bound = machine_number_to_guess
    while user_feedback != 'yes':
        if user_feedback == 'higher':
            lower_bound = machine_number_to_guess
            machine_number_to_guess = random.randint(lower_bound + 1, 100)
            print(f"HIGHER Is Machine guesses higher than? {machine_number_to_guess}.")
            user_feedback = input("Enter your feedback: ").strip().lower()
            attempts += 1
        elif user_feedback == 'lower':
            upper_bound = machine_number_to_guess
            machine_number_to_guess = random.randint(lower_bound, upper_bound - 1)
            print(f"HIGHER Is Machine guesses lower than? {machine_number_to_guess}.")
            user_feedback = input("Enter your feedback: ").strip().lower()
            attempts += 1
            if user_feedback == 'higher':
                lower_bound = machine_number_to_guess + 1
                machine_number_to_guess = random.randint(lower_bound, upper_bound)
                print(f"HIGHER Is Machine guesses higher than? {machine_number_to_guess}.")
                user_feedback = input("Enter your feedback: ").strip().lower()
                attempts += 1
        elif user_feedback == 'yes':
            print(f"HIGHER Machine guessed your number {machine_number_to_guess} in {attempts} attempts.")
            return attempts

def main():
    # Insert the mode selection here
    print("Select a mode:")
    print(" Preess 1 for Mode 1: Guess the Number")
    print(" Press 2 for Mode 2: Machine guess the number")
    mode = int(input("Enter your choice (1 or 2): "))
    if mode == 1:
        user_guess_number()
    elif mode == 2:
        machine_guess_number()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
