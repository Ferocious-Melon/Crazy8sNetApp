#Import libraries
import card
import random

#Player1
#Player2
player1 = 7
player2 = 7

#Boolean to determine which player's turn it is
turn = False

#Lists - stores cards of deck and each player's hand
deck = []
hand1 = []
hand2 = []


suits = ('D','C','H','S') #Suits of the cards [Diamond, Club, Heart, Spade]

for suit in suits: #Assign each symbol with numbers 1 - 13
    for i in range(1,13+1): #Assign each number according to the symbol, suit, from 1 - 13
        deck.append(card.card(suit,i)) #Create card, add to deck



def game(): #Main game
    
    runGame = True

    goesFirst = random.randint(1, 10) #Decides who goes first
    if random.randint(1, 10) >= 5: #Number greater than 5, player 2 goes first
        turn = False

    else: #Any number (Less than 5) means it's player 1's turn
        turn = True #True - Player 1, False - Player 2

    #Call the shuffle function 3 times
    shuffle()
    shuffle()
    shuffle()

    #Distribute the shuffled deck to player 1 and 2
    distribute(hand1)
    distribute(hand2)

    #Stores either hand1 or 2, depending on who's turn it is
    currentHand=None
    cardInPlay = deck.pop()

    #Main loop, runs the game
    while runGame == True:

        print("\x1b[2J") #Clear console
        print("\x1b[2J")

        #Displays what card is in play, # of cards your opponent has, and who's turn it is
        print("Card currently in play: ", cardInPlay)
        print("Number of cards your opponent has: ", len(hand2))

        #Stores hand1 or 2 in current hand depending on who's turn it is
        currentHand = hand1 if turn else hand2
        currPlayer = '1' if turn else '2'
        print("Player ",currPlayer,"'s turn",sep="")

        #Prints out the hand using a for-loop, going through each index
        for i in range(len(currentHand)):
                print("[", i, "] ", currentHand[i], sep="")
                print("\n")
        
        #When player decides to play a card
        canPlay = False 
        for c in currentHand: #For loop to go through current hand
            if(c.compare(cardInPlay) == True): #Check if currentHand[c] matches cardInPlay
                canPlay = True #Set to true
        if canPlay: #If true, player can play a card
            print("Choose a card (by index): ") #Prompt user
            choice = int(input())
            #If input is unplayable, ask the user again
            while not (choice in range(0,len(currentHand)) and cardInPlay.compare(currentHand[choice])):
                print("Cannot play that card")
                choice = int(input("Choose another (by index): "))

            #Set cardInPlay as the chosen card, the pop returns the card, setting cardInPlay as that card while also removing it from currentHand
            cardInPlay = currentHand.pop(choice)
            
            #Check for other cards available to play
            possibleCards = [] #Create list
            for i in range(len(currentHand)): #Go through the currentHand list
                if cardInPlay.num == currentHand[i].num: #Check if the num value of cardInPlay & currentHand are the same
                    possibleCards.append(i) #Add card to possibleCards list
                    print("[", i, "] ", currentHand[i], sep="") #Print out possible choices
                    print("\n")

            while(len(possibleCards) != 0): #While the length of possible cards isn't 0
                choice = int(input("Choose an index to play or another input to continue")) #Prompt user
                if choice in possibleCards and cardInPlay.compare(currentHand[choice]): #If choice is valid, set cardInPlay as chosen card, while deleting the card from currentHand
                    cardInPlay = currentHand.pop(choice)
                    possibleCards.remove(choice)
                    print("Card In Play", cardInPlay)
                else: #User decides to skip turn
                    possibleCards.clear()

            if len(currentHand) == 0: #If currentHand is 0, the currPlayer has won the game
                print("Congratulations! Player", currPlayer, " has won the game!")
                runGame = False
        else: #If player has no valid cards, they will draw a card
            newCard = deck.pop() #Card drawn
            print("Card Drawn: ",newCard) #Prints out what card they drew
            currentHand.append(newCard) #Add the drawn card to the hand

            if newCard.compare(cardInPlay):#If the drawn card is valid, will ask user if they want to use
                toPlay = input("Do you want to play it? [y/n]: ") #Prompt
                while toPlay != "y" and toplay != "n": #If response invalid, will ask to enter again
                    toPlay = input("Enter proper response: [y/n]: ")
                if toPlay == "y": #Plays the drawn card
                    cardInPlay = currentHand.pop()

        input("Hit 'Enter' to continue.") #Confirm move
        turn = not turn #Switches to other player's turn



def shuffle(): #Shuffles the deck
    deckLen = len(deck) 
    for i in range(0, deckLen): #Goes through the length of the deck
        r = random.randint(0, deckLen-1)
        deck[i], deck[r] = deck[r], deck[i] #Swaps the content of i and r(Randomized number)

def distribute(list): #Distributes the deck to hand
    for i in range(7): #Distributes a total of 7 cards
        list.append(deck.pop()) #Adds card from deck to the list

game() #Call game

while True: #Asks if user wants to continue playing
    print("Continue playing? ([y]/[n])") #Prompt for input
    response = input() 
    while response != 'y' and response != 'n': #If response invalid, ask again
        print("Invalid input: Enter again([y]/[n]): ")
        response = input()
    if response == 'y': #Calls game function if they want to play again
        game()
    elif response == 'n': #Program ends
        break




    

    
        
    
        
    
        
