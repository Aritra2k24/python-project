import random
def choice():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(u_score,c_score):
    if u_score == c_score:
        print("draw")
    elif u_score == 0 :
        print("user loose")
    elif c_score == 0:
        print("user win")
    elif u_score > 21:
        print("user loose")
    elif c_score > 21:
        print("user win, dealer loose")
    elif u_score > c_score:
        print("user win")
    elif u_score < c_score:
        print("dealer win")

def play_game():
    from art import logo
    print(logo)

    user_choice = []
    computer_choice = []
    user_score = -1
    computer_score = -1
    for _ in range(2):
        user_choice.append(choice())
        computer_choice.append(choice())
    user_score = sum(user_choice)
    computer_score = sum(computer_choice)
    is_game_over = False
    while not is_game_over:
        print(f"your cards:{user_choice} and score is {user_score}")
        print(f"computer's first card : {computer_choice[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            decision = input("type 'y' to continue and type 'n' to stop").lower()
            if decision == 'y':
                user_choice.append(choice())
                user_score = sum(user_choice)
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_choice.append(choice())
        computer_score = sum(computer_choice)
    print(f"user's final hand:{user_choice} and final score: {user_score}")
    print(f"computer's final hand:{computer_choice} and final score:{computer_score}")
    compare(user_score,computer_score)
play = input("type 'y' to continue the game or type 'n' for stop the game").lower()
if play == "y":
    play_game()

else:
    exit()
