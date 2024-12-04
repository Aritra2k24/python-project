import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["capital", "deaf", "insert", "mutual"]
word = random.choice(word_list)
print(word)
space = ""
for letter in word:
    space += "_"
print(space)
random.seed(word)
print(word)
choose_word = []
game_over = False
lives = 6
while not game_over:
    user_choice = input("user's choice: ").lower()
    display = ""
    for letter in word:
        if user_choice == letter:
            display += user_choice
            choose_word.append(user_choice)
        elif letter in choose_word:
            display += letter
        else:
            display += "_"
    print(display)
    if user_choice not in choose_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you loose")
    if "_" not in display:
        game_over = True
        print("congratulations you win")