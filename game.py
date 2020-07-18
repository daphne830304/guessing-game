"""A number-guessing game."""
import random
# Put your code here
name = input('enter name:')
print('hi')
guess = random.randint(0,101) 
while True:
    userinput = int(input('quess my number:'))
    if userinput < guess:
        print('guess is too small')
    elif userinput > guess:
        print('guess is too big')
    else:
        print(f"you've guessed the number {guess}")
        break
