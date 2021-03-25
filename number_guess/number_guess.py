import random

print('Welcome to the number guessing game!')
print('\nIn this game you will be guessing a random number between 1 and 10.')
print('\nYou will be given three tries to guess before you lose. ')
print('\nGuess correctly and you win!')

random_number = random.randint(1,10)
counter = 0

while counter < 3:
    user_number = input('Please enter a number between 1 and 10: ')

    if user_number == random_number:
        print('Congratulations! You guessed the correct number! YOU WIN!!!')
        break
    else:
        print('Sorry, you guessed incorrectly, please try again!')
        counter += 1


