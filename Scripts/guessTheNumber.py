#This is a guess game
import random

#generate random number between 1 and 20
number = random.randint(1,20)
print("I am thinking of a number between 1 and 20.You have 6 allowed guesses")

#Ask the player to guess 6 times
for guesses in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    else:
        break  #This condition is the correct guess

if guess == number:
    print("Good job!You guessed my number in " + str(guesses) + " guesses!")
else:
    print("Nope. The number i was thinking of was " + str(number))