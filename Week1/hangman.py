import os
import random
import hangman_art
os.system('CLS')
print("Welcome to Hangman")
print(hangman_art.hangmanArt)
# those are the sample space from which the random word is chosen
#vocab = ["apple", "mango", "orange", "banana", "eggs", "beans", "aswan", "luxor", "oliver"]
from hangman_words import word_list
word = random.choice(word_list)
guesslist = []
for i in range(len(word)):
    guesslist.append('_')
print(guesslist)
#print(word)
lives = 7
while lives > 0:
    l = input("Choose a letter\n").lower()
    os.system('CLS') # really beautiful
    if l in guesslist:
        print("you guessed this correctly before")
        continue
    right_choice = False
    for i in range(len(word)):
        if l == word[i].lower():
            right_choice = True
            guesslist[i] = l
    print(guesslist)
    if not right_choice:
        print("You guessed a letter that is not in the word. You lose a life.")
        lives -= 1
    if '_' not in guesslist: # Important
        print("YOU WON 😀")
    elif lives == 0:
        print("Game over 😔")
        print(f"The correct word is {word}")
    if lives < 7:
        print(hangman_art.stages[lives])