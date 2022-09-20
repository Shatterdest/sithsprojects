import random
import time
import sys

try:


    numbers = ['1','2','3','4','5','6','7','8','9','10']
    correctnum = int((random.choice(numbers)))
    guess = int(0)
    count = int(1)
    incorrectguesses = []
    new_line = '\n'

    correct = False 
    while correct == False:
        guess = int(input('Input a number guess here between 1 and 10: '))
        print('Processing.... Please wait.')
        time.sleep(0.7)

        if guess == correctnum: 
            print(f'You have guessed the correct number! Good Job!{new_line}Your incorrect guesses will now be printed.')
            time.sleep(2)
            for index in incorrectguesses:
                print(f'Incorrect guess #{count}: {index}')
                time.sleep(1)
                count = count + 1
            print('Thank you for using the Number Guess program!')
            correct = True
            
        elif guess < correctnum:
            print(f'Your guess "{guess}" is below the correct number. Try again!')
            incorrectguesses.append(guess)

        elif guess > correctnum:
            print(f'Your guess "{guess}" is above the correct number. Try again!')
            incorrectguesses.append(guess)



except Exception:
    e = sys.exc_info()[1]
    print('Oops, an error occured! Please run the code again! Error: ' + e.args[0])
