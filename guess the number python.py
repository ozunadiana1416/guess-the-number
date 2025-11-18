import random

print("Hello, welcome to the game! This is a number guessing game.")
print("You have 7 chances to guess the number. Let's start!\n")

number_to_guess = random.randrange(100)  # 0 to 99
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    try:
        my_guess = int(input('Please enter your guess: '))
    except ValueError:
        print("Please enter a valid number.")
        guess_counter -= 1  # don't count invalid input
        continue

    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right in attempt {guess_counter}!')
        break  # exit loop if correct

    elif my_guess > number_to_guess:
        print('Your guess is higher.')

    elif my_guess < number_to_guess:
        print('Your guess is lesser.')

    # Only print this if it's the last attempt
    if guess_counter == chances and my_guess != number_to_guess:
        print(f'Oops, the number is {number_to_guess}. Better luck next time!')


