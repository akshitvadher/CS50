import random

def guess(x):
    random_number = random.randint( 1 , x )
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess  number between 1 and {x} : "))

        if guess < random_number:
            print("sorry, Guess some High again ...\n")
        elif guess > random_number:
            print("sorry, Guess some Low again ...\n")

    print(f"Yay, You guessed the number which is {random_number}. \n")


def guess_computer(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low
        feedback = input(f'Is {guess} too High type (H), too Low (L) and  is correct type (C) : ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback  == 'l':
            low = guess + 1

    print(f"Yay , Computer guess your number which is {guess}. \n")


guess_computer(20)