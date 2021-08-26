# from the socket module import all
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
server_address = ('localhost', 10000)
# get value for domain name
domain_name = gethostname()
# find ip address using hostname
ip_address = gethostbyname(domain_name)
# output to terminal some info on the address details
print('connecting to server at %s with ip address %s ***' % (domain_name, ip_address))
# Connect the socket to the host and port
sock.connect(server_address)

try:

    # prompt for data to be sent via command line
    print('Type something to be sent: ')
    # take data input
    message = input()
    # send to server
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(16).decode()
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()