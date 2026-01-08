import socket

#Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client socket has been created!")

'''CHANGE THIS TO THE SERVER'S LOCAL IP ADDRESS'''
host = '192.168.68.136' #Assign host device IP (found manually)
port = None             #Set global port variable

codes = ('MSG', 'INP', 'EXT') #List of possible codes that can be received from server

#toMessage (String)
#Returns the string format of split data taken across the network
def toMessage(l):
    message = ''
    for token in l:
        message += token + ' '
    return message

#runClient (void)
#Executes the client's basic functions
def runClient():

    comms = [] #List of commands on most recent signal received
    msgs = []  #List of msgs that come along with them
    data = []  #Raw data taken from server

    port = int(input('Enter port: ')) #Grab a user inputted port

    #Try to connect to host
    s.connect((host, port))
    print("Succesfully connected to host")

    #Enter main loop
    while True:
        #Grab data from server and split it into space separated tokens
        data = s.recv(1024).decode().split(' ')

        #Loop through data
        for i in range(len(data)):

            token = data[i]

            #If the token is an opp code
            if token in codes:
                #Create a new command to be processed
                comms.append(token)
                msgs.append([])
            #Otherwise...
            elif len(msgs) != 0:                    #(Edge case from blank string before first OP code)
                msgs[-1].append(token)              #Add to the current message

        #Loop through queue of operations
        for i in range(len(comms)):
            #Grab the code and message
            code = comms[i]
            msg = msgs[i]

            #Based on op code...
            if code == 'MSG':
                #Print out message received
                print(toMessage(msg))
            elif code == 'INP':
                #Prompt for input and send back to server
                inp = input(toMessage(msg))
                s.send(inp.encode())
            elif code == 'EXT':
                #Close down the client
                s.close()
                break

        #Clear all information for next loop
        data.clear()
        comms.clear()
        msgs.clear()
