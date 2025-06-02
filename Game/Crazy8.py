import card
import random

#Player1
#Player2
player1 = 7
player2 = 7

turn = False

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
        turn = True

    #Call the shuffle function 3 times
    shuffle()
    shuffle()
    shuffle()

    distribute(hand1)
    distribute(hand2)

    currentHand=None
    cardInPlay = deck.pop()

    while runGame == True:

        print("Card currently in play: ", cardInPlay)
        print("Number of cards your opponent has: ", len(hand2))

        currentHand = hand1 if turn else hand2
        currPlayer = '1' if turn else '2'

        print("Player ",currPlayer,"'s turn",sep="")
        for i in range(len(currentHand)):
                print("[", i, "] ", currentHand[i], sep="")
                print("\n")
        
        canPlay = False
        for c in currentHand:
            if(c.compare(cardInPlay) == True):
                canPlay = True
        if canPlay:
            print("Choose a card (by index): ")
            choice = int(input())
            while not (choice in range(0,len(currentHand)) and cardInPlay.compare(currentHand[choice])):
                print("Cannot play that card")
                choice = int(input("Choose another (by index): "))

            cardInPlay = currentHand.pop(choice)
            
            #Check for other cards available to play
            possibleCards = []
            for i in range(len(currentHand)):
                if cardInPlay.num == currentHand[i].num:
                    possibleCards.append(i)
                    print("[", i, "] ", currentHand[i], sep="")
                    print("\n")

            while(len(possibleCards) != 0):
                choice = int(input("Choose an index to play or another input to continue"))
                if choice in possibleCards and cardInPlay.compare(currentHand[choice]):
                    cardInPlay = currentHand.pop(choice)
                    possibleCards.remove(choice)
                    print("Card In Play", cardInPlay)
                else:
                    possibleCards.clear()

            if len(currentHand) == 0:
                print("Congratulations! Player 1 has won the game!")
                runGame = False
        else:
            newCard = deck.pop()
            print("Card Drawn: ",newCard)
            currentHand.append(newCard)

            if newCard.compare(cardInPlay):
                toPlay = input("Do you want to play it? [y/n]: ")
                while toPlay != "y" and toplay != "n":
                    toPlay = input("Enter proper response: [y/n]: ")
                if toPlay == "y":
                    cardInPlay = currentHand.pop()

        input("Hit 'Enter' to continue.")
        turn = not turn



def shuffle(): #Shuffles the deck
    deckLen = len(deck)
    for i in range(0, deckLen):
        r = random.randint(0, deckLen-1)
        deck[i], deck[r] = deck[r], deck[i]

def distribute(list):
    for i in range(7):
        list.append(deck.pop())

game()

while True:
    print("Continue playing? ([y]/[n])")
    response = input()
    while response != 'y' and response != 'n':
        print("Invalid input: Enter again([y]/[n]): ")
        response = input()
    if response == 'y':
        game()
    elif response == 'n':
        break




    

    
        
    
        
    
        
