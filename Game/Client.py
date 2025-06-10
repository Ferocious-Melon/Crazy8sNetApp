import socket
s = socket.socket()
print("Client socket has been created!")

port = 5251
host = '10.0.1.6'


def toMessage(data):
    message = ''
    for token in data:
        message += token + ' '
    return message

def runClient():
        try:
                s.connect((host, port))
                print("Succesfully connected to host")
        except ConnectionRefusedError:
                print("Cannot CREATE connection!!!")
        
        while True:
            data = s.recv(1024).decode().split(' ')
            code = data[0]

            if code == 'MSG':
                print(toMessage(data[1:]))
            elif code == 'INP':
                s.send(input(toMessage(data[1:])))
            elif code == 'EXT':
                s.close()
                break
