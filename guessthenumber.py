#This is a number guessing game
import random
secretnum = random.randint(1,20)
print('Hello what is your name?')
name = input()
print('Hello ' + name +" I'm thinking of a number between 1 and 20")

for guesstaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretnum :
        print('Sorry too low, try again.')
    elif guess > secretnum :
        print('Sorry too high, try again')
    else:
        break
if guess == secretnum :
    print('Good job you got it')
else :
    print('Sorry the answer was' + secretnum)
    
