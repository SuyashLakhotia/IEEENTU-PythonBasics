from random import randint

answer = randint(1, 10)

guess = int(input("Enter your guess: "))

while guess != answer:
    print("Wrong!")

    if answer > guess:
        print("Higher")
    else:
        print("Lower")

    guess = int(input("Enter another guess: "))

print("Correct!")
