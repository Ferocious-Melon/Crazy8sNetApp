import socket
import server
import client
import Crazy8 as c8

#Prompts user for how they want their program to 
runType = input("Host or Join? (h/j): ")

if runType == 'h':

    server.startServer()

    c8.game() #Starts the game

    while True: #Asks if user wants to continue playing

        print("Continue playing? ([y]/[n])") #Prompt for input
        response = input() 
        while response != 'y' and response != 'n': #If response invalid, ask again
            print("Invalid input: Enter again([y]/[n]): ")
            response = input()

        if response == 'y': #Calls game function if they want to play again
            c8.game()
        elif response == 'n': #Program ends
            server.closeServer()
            break

elif runType == 'j':
    #Enters client mode
    client.runClient()