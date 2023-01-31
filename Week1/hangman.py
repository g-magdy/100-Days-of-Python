import random
print("Welcome to Hangman")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# those are the sample space from which the random word is chosen
vocab = ["apple", "mango", "orange", "banana", "eggs", "beans", "aswan", "luxor", "oliver"]
word = random.choice(vocab)
letters_to_guess = len(word)
guesslist = []
for i in range(len(word)):
    guesslist.append('_')
print(guesslist)
#print(word)
lives = 7
while lives > 0 and letters_to_guess > 0:
    l = input("Choose a letter\n").lower()
    right_choice = False
    for i in range(len(word)):
        if l == word[i].lower():
            right_choice = True
            letters_to_guess -= 1
            guesslist[i] = l
    print(guesslist)
    if not right_choice:
        lives -= 1
    if letters_to_guess == 0:
        print("YOU WON 😀")
    elif lives == 0:
        print("Game over 😔")
    if lives < 7 and letters_to_guess > 0:
        print(stages[lives])
