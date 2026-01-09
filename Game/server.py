import json
import socket #Import socket library
import threading
from queue import Queue

config=json.loads(open("config.json").read())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket has been created!")

#Byte sizes for different kinds of messages
MSG_LARGE = 201480
MSG_MED = 1024

NUM_THREADS = 2
JOB_NUMBER = [1, 2]

OTHER_PLAYERS = config["players"]-1

jobQ = Queue()
connections = []
addresses = []

accepting = True

port = config["port"]
hostIP = None
client = None
addr = None

def create_socket():
    global hostIP, port, s

    '''CHANGE THIS TO YOUR LOCAL IP ADDRESS. WILL BREAK IF NOT SET UP PROPERLY'''
    hostIP = '172.17.155.196' #Machine's local IP

    s = socket.socket()

def bind_socket():
    global hostIP
    global port
    global s

    try:
        s.bind((hostIP, port)) #Bind socket to host IP and port
        s.listen(OTHER_PLAYERS)
        print("Socket has been binded to %s" %(port))

    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n")


#JOB 1
#Accepting connections from several clients
def accepting_connection():
    #Clear all previous connections
    for c in connections:
        c.close()
    del connections[:]
    del addresses[:]

    while True:
        try:
            conn, addr = s.accept() #Get Connections
            s.setblocking(1)     #Prevents connection timeouts

            connections.append(conn)
            addresses.append(addr)

            #Print IP of machine connected to
            print("Connection established with : " + addr[0])

        except Exception as error:
            print("Socket connections error",error)

#2nd Thread - Communicating with clients
#Run the game code

#Display all current active connections
'''CURRENTLY UNACCESIBLE DURING EXECUTION'''
def list_connections():
    global connections
    global addresses

    results = ''

    for id, conn in enumerate(connections):
        #Check to see if connection is still active
        try:
            conn.send(str.encode(' '))
            conn.recv(MSG_LARGE)         #Receive a large # of bytes for lack of knowing size
        except:
            del connections[id]
            del addresses[id]
            continue                  #Skip to next connection

        results += str(id) + "     " + str(addresses[id]) + "\n"

    print("------ Clients ------")
    print(results)

#Return the specific connection of a target client
def get_target(args):
    try:
        #Grab target id
        target = int(args[0])
        flags = args[1:]

        #Try accessing connection from list
        conn = connections[target]

        print("You are connected to : " + str(addresses[target]))
        print(str(addresses[target][0]) + ">",end="")

        return conn
    except:
        print("Invalid Selection") #Due to invalid index or input

#Threading logic begins below

def create_threads():
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        task = jobQ.get()
        if task == 1:
            create_socket()
            bind_socket()
            accepting_connection()
        elif task == 2:
            start_shell()
        jobQ.task_done()

def create_jobs():
    for x in JOB_NUMBER:
        jobQ.put(x)

    jobQ.join()

#Run the server
def startServer():
    global port, client, addr

    create_jobs()
    create_threads()

    print("Server online. Host IP : ", hostIP)

#Set a client's associated player id
def setClientID(conn,id):
    conn.send((' IDSET '+ str(id)).encode())

#Sends a message to the client
def sendMessage(conn,msg):
    conn.send((' MSG ' + msg).encode())

#Get input from the client
def getInput(conn,prompt=""):
    conn.send((' INP ' + str(prompt)).encode())
    return client.recv(MSG_MED).decode()

#Close both the server and client connection
def closeServer():
    for c in connections:
        c.close()
    s.close()


'''CODE CURRENTLY INACCESSIBLE:

- From testing multi client connections.

'''
#Main function to run the shell
def start_shell():

    while True:
        #Output command UI
        cmd = input("C8> ").split(' ')

        act = cmd[0]
        args = cmd[1:]

        match act:
            case 'list':
                list_connections()

            case 'select':
                conn = get_target(args)
                if conn is not None:
                    send_comms(conn)

            case _: #No recognized commands
                print(act, "command not recognized")

                #While true loop to send commands to the connected client
'''CURRENTLY INACCESSIBLE'''
def send_comms(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),"utf-8")
                print(client_response,end="")
        except:
            print("Error sending commands")
            break

