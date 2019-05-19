import random

games = ''

while games == '':
    try:
        games = int(input('how many games would you like to play?'))
    except:
        print('Please enter a number')

for game in range(0, games):
    pick = random.randint(1, 26)
    guess = None
    attempts = 1

    while pick != guess:
        try:
            guess = int(input('Guess a number'))
        except:
            print('Select a number')
            continue

        if guess != pick:
            attempts += 1
            if guess > pick:
                print('Your guess is high')
            else:
                print('Your guess is low')
        else:
            print('Correct ! it took you this many attempts %s', attempts)
