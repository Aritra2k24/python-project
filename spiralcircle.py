
import random
number = random.randint(1,100)
no_of_turns = 0

def set_difficulty(level):
    global no_of_turns
    if level == "Hard":
        no_of_turns = 5
        print(f"you have{no_of_turns} number of turns")
    if level == "Easy":
        no_of_turns = 10
        print(f"you have {no_of_turns} number of turns")
    for i in range((no_of_turns)):
        guess = int(input("enter your number:"))
        if guess > number:
            no_of_turns =-1
            print("too high")

        if guess < number:
            no_of_turns =-1
            print("too low")

        if guess == number:
            print("you guessed right!")
            exit()
    print("you lose your turn")

level_of_game = input("enter the difficulty level:")
set_difficulty(level_of_game)