import socket #Import socket library
import sys
import threading
import time
from queue import Queue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket has been created!")


NUM_THREADS = 2
JOB_NUMBER = [1, 2]

jobQ = Queue()
connections = []
addresses = []

'''CHANGE THIS TO YOUR LOCAL IP ADDRESS'''
hostIP = '192.168.68.136' #Use private IP address of host machine
port = None               #Set port as a global variable

#Set default values for connection and address
client = None
addr = None

def bindSocket():
    global hostIP 
    global port 
    global s

    try:
        s.bind((hostIP, port)) #Bind socket to host IP and port
        print("Socket has been binded to %s" %(port))
    
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n")

def acceptingConnection():
    #Clear all previous connections
    for c in connections:
        c.close()
    connections.clear()
    addresses.clear()

    while True:
        try:
            conn, addr = s.accept() #Get Connections
            s.setblocking(True)     #Prevents connection timeouts

            connections.append(conn)
            addresses.append(addr)

            print("Connection established with : " + addr[0])


        except:
            print("Socket connections error")




#Run the server
def runServer():        
    global port, client, addr

    #Prompt user for their desired port
    port = int(input('Enter port: '))

    bindSocket()

    client, addr = s.accept()
    print("Connections established :", addr)

#Sends a message to the client
def sendMessage(msg):
    client.send((' MSG ' + msg).encode())

#Get input from the client
def getInput(prompt=""):
    client.send((' INP ' + str(prompt)).encode())
    return client.recv(1024).decode()

#Close both the server and client connection
def closeServer():
    client.send(' EXT '.encode())
    s.close()
