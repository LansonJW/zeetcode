
import random

print('----------------------------')
print('Guess That Number Game')
print('----------------------------')

print()


the_number = random.randint(0, 100)
guess = -1
name = input('player what is your name? ')

while guess != the_number:
    guess_text = input('guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry {}, Your guess of {} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, Your guess of {} was too High.'.format(name, guess))
    else:
        print('Excellent work {}, you won, it was {}.'.format(name, guess))


print('done')