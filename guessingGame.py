import random

no = random.randint(1, 100)
chance = 0

print('Guess a number between 1 and 100')

while chance < 5:
    guessing = int(input('Enter your guess'))
    if (guessing == no):
        print('You win!!!!!!!!!!!!!!!!! :)')
        break
    elif (guessing < no):
        print('Your guess was too low!Think Big!Guess higher than ', guessing)
    else:
        print('Your number was too high! Please lower your expectations! Guess a lower number than', guessing)
    chance = chance + 1
if(not chance <5):
    print('You lose!... You tried at least :). The number is......', no )


input('Enter to exit')