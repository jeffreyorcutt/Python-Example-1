import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    print('The first iteration of this game requires you to guess the random number.')
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print("Sorry, guess again, too low.")
        elif guess > random_number:
            print("Sorry, guess again, too high.")
    print("You chose the correct number!")

#guess(10)

def computer_guess(x):
    low = 1
    high = x
    user_feedback = ''

    while user_feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could be a case where there is only one number
        user_feedback = input(f'Is {guess} too high (h), too low (l), or correct (c)?').lower()
        if user_feedback == 'h':
            high = guess - 1
        elif user_feedback == 'l':
            low = guess + 1
    print(f'Your number was {guess}.')
print('The second iteration of this game you select a random positive number and keep it a secret. \n')
print('Then you give the computer a range that the computer starts to guess within.')
range_max = int(input('What is the high number in the range for the computer to guess? '))
computer_guess(range_max)