import socket
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


while client == True:
        s = socket.socket()

        port = 5251

        try:
                s.connect(('10.0.1.6', port))
                print(s.recv(1024).decode()) #Decode the message
                s.close() #Close
        except ConnectionRefusedError:
                print("Cannot CREATE connection!!!")

while server == True:
        port = 5251

        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Client socket has been created")

        s.bind(('', port))
        print("Socket has been binded to %s" %(port))

        s.listen(1)
        print("The socket of client is listening...")

        while True:
                c, addr = s.accept()
                print("Connection formed", addr)
                Crazy8.mainGame()
                c.send(message.encode())

                c.close()
                break
