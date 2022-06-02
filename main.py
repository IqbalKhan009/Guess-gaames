import random

print('you will have 3 tries')
upper_level = int(input("Enter Upper Level "))
Guess = int(input ("Guess a Number  "))
random_number = random.randint(0, upper_level)
guesses = 0


while Guess!= random_number:
    guesses += 1
    guess_limit = 2
    if Guess <= upper_level:
        print("Try Again ")
        Guess = int(input ("Guess a Number  "))
        if guesses == guess_limit:
            print('Unlucky ')
            break
    else:
        print('Your Guess is greater than upper limit')
        break
else:
    print('You Win')
