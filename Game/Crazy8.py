#Import libraries
import socket
import server
import client
import card
import random

#Boolean to determine which player's turn it is
turn = False

#Lists - stores cards of deck and each player's hand
deck = []
hand1 = []
hand2 = []

#Variables used for processing the current turn
cardInPlay = None
currentHand = None
currPlayer = None

#Input function which takes from different sources based on turn
def grabInput(prompt):
    if turn:
        return input(prompt)
    else:
        return server.getInput(prompt)

#Output function which takes from different sources based on turn
def sendMessage(msg):
    if turn:
        print(msg,end='')
    else:
        server.sendMessage(msg)

def statusToString():
    msg = ''
    #Displays what card is in play, # of cards your opponent has, and who's turn it is
    msg += "Player " + currPlayer + "'s turn. \n"
    msg += "Card currently in play: " + cardInPlay.__str__() + '\n'
    msg += "Number of cards your opponent has: " + str(len(hand2 if currentHand==hand1 else hand1))
    return msg

def handToString():
    msg = ''
    for i in range(len(currentHand)):
        msg += "[ "+ str(i) + " ] " + currentHand[i].__str__() + '\n'
    return msg

def displayWin():
    global turn
    
    sendMessage("Congratulations! Player " + currPlayer + " has won the game!")
    turn = not turn
    sendMessage("Congratulations! Player " + currPlayer + " has won the game!")

def game(): #Main game
    global deck, currentHand, currPlayer, cardInPlay, turn

    runGame = True

    #Clear player hands and dec
    deck.clear()
    hand1.clear()
    hand2.clear()

    suits = ('D','C','H','S') #Suits of the cards [Diamond, Club, Heart, Spade]
    
    #Add all of the corresponding cards from each suit
    for suit in suits: 
        for i in range(1,13+1): #Assign each number according to the symbol, suit, from 1 - 13
            deck.append(card.card(suit,i)) #Create card, add to deck


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

    #Sets the first card in play
    cardInPlay = deck.pop()

    #Main loop, runs the game
    while runGame == True:
        #Stores hand1 or 2 in current hand depending on who's turn it is
        #Does the same for player number
        currentHand = hand1 if turn else hand2
        currPlayer = '1' if turn else '2'

        #Clears screen, displays game status, and current player's hand
        sendMessage("\x1b[2J" + statusToString() + '\n' + handToString())
        
        #Checks if a player has a playable card
        canPlay = False 
        for c in currentHand: #For loop to go through current hand
            if(c.compare(cardInPlay) == True): #Check if currentHand[c] matches cardInPlay
                canPlay = True                 #Set to true
        
        if canPlay:
            #Ask the player to choose a card 
            choice = int(grabInput("Choose a card (by index): "))
            #While choice is invalid
            while not (choice in range(0,len(currentHand)) and cardInPlay.compare(currentHand[choice])):
                sendMessage("Cannot play that card\n")
                choice = int(grabInput("Choose another (by index): "))

            #Set cardInPlay as the chosen card
            cardInPlay = currentHand.pop(choice)
            
            #Check for other cards available to play
            possibleCards = ['temp'] #Create list with temporary value
            #While there are still cards to play...
            while(len(possibleCards) != 0):
                
                possibleCards.clear()
                for i in range(len(currentHand)): #Go through the currentHand list
                    if cardInPlay.num == currentHand[i].num: #Check if the num value of cardInPlay & currentHand are the same
                        possibleCards.append(i) #Add card to possibleCards list
                        sendMessage('['+str(i)+'] '+ currentHand[i].__str__() + '\n')
                    
                #Ask player to pick a card to play or void the rest of their turn
                choice = int(grabInput("Choose an index to play or another input to continue: ")) 
                
                if choice in possibleCards and cardInPlay.compare(currentHand[choice]): #If valid choice
                    cardInPlay = currentHand.pop(choice)    #Play the card
                    possibleCards.remove(choice)            #Remove it from possible optoins

                    sendMessage("Card In Play " + cardInPlay.__str__() + '\n') #Print so
                
                else: #User decides to skip turn
                    possibleCards.clear() #Clear possible cards to forcibly end loop

            #Checks if the player has won and ends the game
            if len(currentHand) == 0: 
                displayWin()
                runGame = False
        
        
        else: #If player has no valid cards, they will draw a card
            
            #Draw card and display what it is
            newCard = deck.pop()
            sendMessage("Card Drawn: " + newCard.__str__() + '\n')
            
            currentHand.append(newCard) #Add the drawn card to the hand

            #Ask if user wants to play the card drawn (regardless of viability)
            toPlay = grabInput("Do you want to play it? [y/n]: ") 
            while toPlay != "y" and toPlay != "n":
                toPlay = grabInput("Enter proper response: [y/n]: ")

            #If they wish to play card...
            if toPlay == 'y':
                #Check if it is viable to play...
                if cardInPlay.compare(newCard):
                    cardInPlay = newCard    #Update card in play
                    currentHand.pop()       #Remove card from hand
                    sendMessage('Card in play: ' + cardInPlay.__str__() + '\n') #Print success
                else:
                    sendMessage('Card is not playable' + '\n') #Print failure
        
        turn = not turn #Switches to other player's turn



def shuffle(): #Shuffles the deck
    deckLen = len(deck) 
    for i in range(0, deckLen): #Goes through the length of the deck
        r = random.randint(0, deckLen-1)
        deck[i], deck[r] = deck[r], deck[i] #Swaps the content of i and r(Randomized number)

def distribute(list): #Distributes the deck to hand
    for i in range(7): #Distributes a total of 7 cards
        list.append(deck.pop()) #Adds card from deck to the list

#----------------------------------------Main program begins here----------------------------------------

#Prompts user for how they want their program to 
runType = input("Client or Server? (c/s): ")

if runType == 's':

    server.runServer()
    
    server.runServer()

    game() #Starts the game
    
    while True: #Asks if user wants to continue playing

        print("Continue playing? ([y]/[n])") #Prompt for input
        response = input() 
        while response != 'y' and response != 'n': #If response invalid, ask again
            print("Invalid input: Enter again([y]/[n]): ")
            response = input()

        if response == 'y': #Calls game function if they want to play again
            game()
        elif response == 'n': #Program ends
            server.closeServer()
            break

elif runType == 'c':
    #Enters client mode
    client.runClient()
