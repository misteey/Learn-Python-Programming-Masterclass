import random
lowest = 1
highest = 10
number = random.randint(lowest, highest)

name = input("Hello friend, welcome to the game, please enter your name: ")

guess = int(input("Hi, {}, please guess a number between {} and {} ".format(name, lowest, highest)))

if guess == number:
    print(f"Wow, {name}, you got it first time")

if guess == 0:
    print(f"Awww sorry to see you go, {name}, please come back soon")

while guess != number:
    if guess == 0:
        print(f"Awww sorry to see you go, {name}, please come back soon")
        break
    if guess > number:
        print("Please guess lower")
    if guess < number:
        print("Please guess higher")
    guess = int(input())
    if guess == number:
        print(f"YAY {name}, you finally got it")
