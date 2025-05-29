class card:
    def __init__(self,suit,num):
        self.suit = suit
        self.num = num

        '''Suits are represented by the first character of their name'''
        '''Jack, Queen, King = 11, 12, 13'''
    #String representation of the card
    def __str__(self):
        return self.suit+str(self.num)

    #Returns whether or not this card is playable
    def compare(self,active):
        return active.suit==self.suit or active.num==self.num

# myCard = card('C',8)
# otherCard = card ('C',10)
# print(myCard)
# print(myCard.compare(otherCard))