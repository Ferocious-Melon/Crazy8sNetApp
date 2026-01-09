import socket
import server
import card

class player:
    #Host constructor
    def __init__(self,id:int,name:str):
        self.conn = None
        self.addr = None
        self.name = name
        self.id   = id
        self.host = True

        self.hand = []
    #Client connections constructor
    def __init__(self,conn,addr,id:int, name:str):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.id   = id
        self.host = False

        self.hand = []

    #Update connection associated with player
    def update_connection(self,conn,addr):
        self.conn = conn
        self.addr = addr

    def send_message(self,msg):
        if not self.host:
            server.sendMessage(self.conn,msg)
        else:
            print(msg)
    def get_input(self,prompt=""):
        if not self.host:
            return server.getInput(self.conn,prompt)
        else:
            return input(prompt)

    #Return if the player can play given the current card
    def can_play(self,card):
        for c in self.hand: #Iterate through hand
            if(c.compare(card) == True): #Check c is playable on the card
                return True
        return False

    #String representation of player's hand
    def handToString(self):
        msg = ''
        for i in range(len(self.hand)):
            msg += "[ "+ str(i) + " ] " + self.hand[i].__str__() + '\n'
        return msg