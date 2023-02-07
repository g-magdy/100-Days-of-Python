import os
import random
from Art_of_w2 import BlackJack_logo
# the goal of the game is to collect the largest sum which s less than or equal 21
# if you exceed 21 -> you lose (called a bust)
# ace == 11, normal 10, king, queen, jack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def showDecks(me, dealer):
    print("\n***********************************************")
    print(f"Your deck : {me}, score = {sum(me)}")
    print("- - - - - - - - - - - - - - - - - - - - - - - -")
    print(f"dealer's deck {dealer}, score = {sum(dealer)}")
    print("***********************************************\n")

def deal_card_for(collection):
    #this adds one random card to the given deck
    collection.append(random.choice(cards))

def check_busted(me, dealer):
    if sum(me) > 21:
        print("Busted 😑")
        return True
    elif sum(dealer) > 21:
        print("The dealer went over 21 : you win 😄")
        return True

def judgeDecks(me, dealer):
    # recieves the two decks of cards and apply the rules of the game
    showDecks(me, dealer)
    busted = check_busted(me, dealer)
    
    if busted:
        return
    
    while sum(dealer) < 17:
        deal_card_for(dealer)
        showDecks(me, dealer)
        busted = check_busted(me, dealer)
        if busted:
            return
    
    if sum(me) == sum(dealer):
        print("draw 🙃")
    elif sum(me) > sum(dealer):
        print("You win 😀")
    else:
        print("You lose 😥")
    

        
def PlayGame():
    #runs the main function of the game
    os.system("cls")
    print(BlackJack_logo)
    print("Welcome to black jack")
    mycards = []
    dealerCards = []
    for _ in range(2):
        deal_card_for(mycards)
        deal_card_for(dealerCards)
    print(f"Your cards are : {mycards}, current score = {sum(mycards)}")
    print(f"Computer's first card is {dealerCards[0]}")
    decision = input("Type 'y' to get another card or 'n' to pass : ")
    if decision == 'y':
        deal_card_for(mycards)
    judgeDecks(me = mycards, dealer = dealerCards)
    


play = input("Do you want to play a Blackjack game ? ")
while play == 'y':
    PlayGame()
    play = input("Do you want to play a Blackjack game ? ")
print("Good bye 👋")