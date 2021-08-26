# Peadar O'Connor 117302273
# from the socket module import all
from socket import *
# for finding the path to the log file
import os.path
# for finding the current date and time
from datetime import datetime

# Create a UDP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DGRAM is used for UDP)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# assign a port number
serverPort = 6789

# bind the socket to the host and given port number
serverSocket.bind(("", serverPort))

# server runs infinitely until interrupted
while True:
    # server waits for a message to be sent
    print("Waiting for a message...")

    # server receives message (in bytes) from client. client address also received
    msg_adr = serverSocket.recvfrom(256)
    # extract and decode the message fro later use
    message = msg_adr[0].decode()
    # extract client address for later use
    client_address = msg_adr[1]

    # print the received message to the screen
    print("Received: %s" % message)

    # capture current date and time
    date_time = datetime.now()
    log_file = "log.txt"
    # open the log file (makes one of not already made)
    if os.path.isfile(log_file):
        log = open(log_file, 'a')
    else:
        log = open(log_file, 'w')
    # write to file
    log.write("\"%s\", sent at %s \n" % (message, date_time))
    # close log file
    log.close()

    # make the received message uppercase
    upper_message = message.upper()
    # send the timestamp and the uppercase sentence to the client
    full_message = "%s: %s" % (date_time, upper_message)
    serverSocket.sendto(full_message.encode(), client_address)

# close the socket (shouldn't reach here)
serverSocket.close()