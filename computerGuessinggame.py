import random 
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = input(f'Guess a number between and {x}')
        if guess < random_number:
            print ('Sorry, guess again, too low.')
        elif guess > random_number:
            print ('Sorry, guess again, too high')
            
    print(f'Yay, congrats. You have guess the number {random_number}')

