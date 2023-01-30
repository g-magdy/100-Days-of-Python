import random
print("Welcome to Hangman")
# those are the sample space from which the random word is chosen
vocab = ["Apple", "Mango", "Orange", "Bannana", "Eggs", "Beans"]
word = random.choice(vocab)
guesslist = []
for letter in word:
    guesslist.append('_')
lives = 7
while lives > 0:
    l = input("Choose a letter\n").lower()
    n  = 0
    for i in range(len(word)):
        if l == word[i]:
            guesslist[i] = l
        else:
            lives -= 1

    #print(f"{word} {n}")
    print(guesslist)
'''
for letter in word:
        if letter == l:
            n += 1
            print("True")
        else:
            lives -= 1
            print("False")
'''