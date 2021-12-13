'''Generate a random number between 1 and 9 (including 1 and 9). 
   Ask the user to guess the number, then tell them whether they 
   guessed too low, too high, or exactly right'''

import random

number = random.randrange(1, 10)
guess = 0
count = 0

while guess != number:
    guess = int(input("Please guess a number between 1 and 9: "))
    count += 1
    if guess not in range(1, 10):
        print("You have to guess a number between 1 and 9!")
    elif guess < number:
        print("You've guessed too low!")
    elif guess > number:
        print("You've guessed too high!")
    else:
        if count == 1:
            print("You rock! You've got it at the first try!")
        elif count <= 3:
            print("Well done! You've got it in just {} tries".format(count))
        elif count > 3:
            print("You've got it! It took you {} tries!".format(count))
