import socket #Import socket library
import Crazy8
import card

client = False
server = False

response = input("Will this be the server(host) or the client (s/c): ")
while response != "s" and response != "c":
        response = input("Invalid response, enter again (s/c): ")

if response == "s":
        server = True
else:
        client = True


while server == True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server socket has been created!")
        port = 5251 #Create a port

        s.bind(('', port)) #Bind socket, allows it to receive from all >        print("Socket has been binded to %s" %(port))

        s.listen(1) #Server is only listening to 1 address
        print("The socket of server is listening...")
        
        while True: #Run while true
                c, addr = s.accept() #Accept connection
                print("Connection formed", addr)
                Crazy8.mainGame()
                c.close() #Close
                break

while client == True:
        s = socket.socket()

        port = 5251

        try:
                s.connect(('10.0.1.5', port))
                print(s.recv(1024).decode())
                s.close()
        except ConnectionRefusedError:
                print("Cannot CREATE CONNECTION!!!!!!!")

