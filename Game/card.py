numtocard = ('-1','A','2','3','4','5','6','7','8','9','10','J','Q','K')
suits = ('D','C','H','S')

class card:
    def __init__(self,suit,num):
        self.suit = suit
        self.num = num

        '''Suits are represented by the first character of their name'''
        '''Jack, Queen, King = 11, 12, 13'''
    #String representation of the card
    def __str__(self):
        return numtocard[self.num]+self.suit 

    #Returns whether or not this card is playable
    def compare(self,active):
        return self.num == 8 or active.suit==self.suit or active.num==self.num

# myCard = card('C',8)
# otherCard = card ('C',10)
# print(myCard)
# print(myCard.compare(otherCard))
