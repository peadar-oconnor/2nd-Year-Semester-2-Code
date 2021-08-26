# Peadar O'Connor 117302273
# from the socket module import all
from socket import *

# find the domain name of the system
domain_name = gethostname()

# DNS lookup to find the ip address
ip_address = gethostbyname(domain_name)

# port on which the server is listening
port = 6789

# Create a UDP socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DGRAM is used for UDP)
sock = socket(AF_INET, SOCK_DGRAM)

try:
    # take input from the user, which is to be sent to the server
    message = input("Type something to be sent: ")

    # send message, which was converted to bytes, to the server
    sock.sendto(message.encode(), (ip_address, port))

    # receive a response from the server
    data = sock.recv(256).decode()

    # print the received message to the screen
    print(data)

finally:
    print("Closing socket...")
    sock.close()