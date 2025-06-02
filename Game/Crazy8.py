import card

#Player1
#Player2
player1 = 7
player2 = 7

turn2 = False
turn1 = False

deck = []
hand1 = []
hand2 = []


suits = ('D','C','H','S') #Suits of the cards [Diamond, Club, Heart, Spade]

for suit in suits: #Assign each symbol with numbers 1 - 13
    for i in range(1,13+1): #Assign each number according to the symbol, suit, from 1 - 13
        deck.append(card.card(suit,i)) #Create card, add to deck

def game(): #Main game
    while True:
        goesFirst = random.randint(1, 10) #Decides who goes first
        if random.randint(1, 10) >= 5: #Number greater than 5, player 2 goes first
            turn2 = True
    
        else: #Any number (Less than 5) means it's player 1's turn
            turn1 = True

        #Call the shuffle function 3 times
        shuffle()
        shuffle()
        shuffle()

        distribute(hand1)
        distribute(hand2)

        cardInPlay = deck[deck.pop()]

        print("Card currently in play: ", cardInPlay)
        print("Number of cards your opponent has: ", len(hand2))

        if turn1 = True:
            print("Choose a card player1 (by index): ")
            for i in range(len(hand1)):
                print("[" + i + "] ", hand1[i])
                print(\n)
        
            choice = int(input())
            while not (choice in range(0,len(hand1)) and cardInPlay.compareCard(hand1[choice])):
                print("Cannot play that card")
                choice = input("Choose another (by index): ")

            cardInPlay = hand1[hand1.pop(choice)]
            turn1 = False
            turn2 = True


        else:
            print("Choose a card player2 (by index): ")
            for i in range(len(hand2)):
                print("[" + i + "] ", hand2[i])
                print(\n)
            choice = int(input())
            while not (choice in range(0,len(hand2)) and cardInPlay.compareCard(hand2[choice])):
                print("Cannot play that card")
                choice = input("Choose another (by index): ") 

            cardInPlay = hand2[hand2.pop(choice)]
            turn2 = False
            turn1 = True

        


def shuffle(): #Shuffles the deck
    deckLen = len(deck)
    for i in range(0, deckLen)
        r = random.randint(0, deckLen)
        a[i], a[r] = a[r], a[i]

def distribute(list[]):
    for i in range(7):
        list[i]=deck.pop()






    

    
        
    
        
    
        

