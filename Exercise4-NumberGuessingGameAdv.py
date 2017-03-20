from random import randint

def makeGuess(low, high):
    return randint(low, high)

lowerLimit = 1
upperLimit = 10

answer = randint(lowerLimit, upperLimit)

guess = makeGuess(lowerLimit, upperLimit)
print(guess)

while guess != answer:
    print("Wrong!")

    if answer > guess:
        print("Higher")
        lowerLimit = guess + 1
    else:
        print("Lower")
        upperLimit = guess - 1

    guess = makeGuess(lowerLimit, upperLimit)
    print(guess)

print("Correct!")
