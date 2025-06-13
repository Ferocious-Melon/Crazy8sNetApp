import socket #Import socket library

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket has been created!")
                
port = 5259 #Create a default port

#Set default values for connection and address
c = None
addr = None

#Run the server
def runServer():        
    global c, addr #Specify that we want to modify global variables

    #Prompt user for their desired port
    port = int(input('Enter port: '))

    s.bind(('', port)) #Bind socket, allows it to receive from all 
    print("Socket has been binded to %s" %(port))

    s.listen(1) #Server is only listening to 1 address
    print("The socket of server is listening...")
    
    c, addr = s.accept() #Accept connection
    print("Connection formed", addr)

#Sends a message to the client
def sendMessage(msg):
    c.send((' MSG ' + msg).encode())

#Get input from the client
def getInput(prompt=""):
    c.send((' INP ' + str(prompt)).encode())
    return c.recv(1024).decode()

#Close both the server and client connection
def closeServer():
    c.send(' EXT '.encode())
    s.close()
