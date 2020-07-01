import random

lower_bound = 1
upper_bound = 20
secret_number = random.randint(lower_bound, upper_bound)
chances = 5

print("I am thinking of a number between {} and {}...".format(lower_bound, upper_bound))
for number_of_guess in range(1, chances+1):
    print("Number of guesses remaining: {}".format(chances+1 - number_of_guess))
    guess = int(input("Type your guess and press enter: "))
    if guess > secret_number and number_of_guess != chances:
        print("Try a lower value")
    elif guess < secret_number and number_of_guess != chances:
        print("Try a higher value")
    else:
        break

if guess == secret_number:
    print("You win!! You got it right in {} guesses".format(number_of_guess))
else:
    print("You loose!! My number was {}".format(secret_number))