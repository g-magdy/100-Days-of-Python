import os
import random
from Art_of_w2 import BlackJack_logo
def dealCard(deck):
    '''takes a deck and appends a random card to it'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck.append(random.choice(cards))

def calcScore(deck):
    '''returns a score of a given deck of cards: either sum or zero'''
    if sum(deck) == 21 and len(deck) == 2:
        return 0 # BlackJack
    if 11 in deck and sum(deck) > 21:
        deck[deck.index(11)] = 1 # replace the ace with 1 if the total is larger than 11
    
    return sum(deck)

def compare(my_deck, his_deck):
    '''Takes two decks of cards and decides the winner'''
    myScore = calcScore(my_deck)
    hisScore = calcScore(his_deck)
    print(f"You : {my_deck}, score = {myScore}")
    print(f"Him : {his_deck}, score = {hisScore}")
    if myScore > 21:
        print("I am busted")
    elif hisScore > 21:
        print("he is busted")
    elif hisScore == 0:
        print("You win: BlackJack!")
    elif hisScore == 0:
        print("The dealer wins: BlackJack!")
    elif myScore > hisScore:
        print("You win")
    elif hisScore > myScore:
        print("You lose")
    else:
        print("draw")

def PlayGame():
    os.system("cls")
    print(BlackJack_logo)
    user_cards = []
    dealer_cards =[]
    for _ in range(2):
        dealCard(user_cards)
        dealCard(dealer_cards)
    user_score = calcScore(user_cards)
    dealer_score = calcScore(dealer_cards)
    
    print("Game has started")
    print(f"Your deck is {user_cards}, your score is {user_score}")
    print(f"The first card with the dealer is {dealer_cards[0]}")
    
    if user_score == 0:
        print("You win:  BlackJack!")
        return
    elif dealer_score == 0:
        print("The dealer wins: BlackJack!")
        return
    
    decision = input("Type Hit (h) or Stand (s)")
    if decision == 'h':
        dealCard(user_cards)
    else:
        while calcScore(dealer_cards) < 17:
            dealCard(dealer_cards)
    compare(user_cards, dealer_cards)
    
#############################################    
while input("let's play (y) or (n) : ") == 'y':
    PlayGame()
print("goodbye")