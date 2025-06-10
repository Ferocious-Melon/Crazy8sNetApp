import socket #Import socket library
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket has been created!")
                
port = 5251 #Create a port

c, addr = None

#Run the server
def runServer():        
        s.bind(('', port)) #Bind socket, allows it to receive from all >        print("Socket has been binded to %s" %(port))

        s.listen(1) #Server is only listening to 1 address
        print("The socket of server is listening...")
        
        c, addr = s.accept() #Accept connection
        print("Connection formed", addr)

#Send message
def sendMessage(msg):
    c.send(('MSG' + msg).encode())

#Get input from the client
def getInput(prompt):
    c.send(("INP" + str(prompt)).encode())
    return c.recv(1024).decode()

def closeServer():
    c.send('EXT'.encode())
    s.close()
