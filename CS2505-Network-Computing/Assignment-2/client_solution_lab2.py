# from the socket module import all
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# the machine address and port number have to be the same as the server is using.
server_address = ('cs1dev.ucc.ie', 9864)
# get value for domain name
domain_name = gethostname()
# find ip address using hostname
ip_address = gethostbyname(domain_name)
# output to terminal some info on the address details
print('connecting to server at %s with ip address %s ***' % (domain_name, ip_address))
# Connect the socket to the host and port
sock.connect(server_address)

# we want the client to run all the time, so set up a forever true while loop
while True:

    # prompt for data to be sent via command line
    print('Type something to be sent: ')
    # take data input
    message = input()
    # send to server
    print('Client: "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())

    # receive data from the server, which is the message the server user typed
    data = sock.recv(64).decode()
    # show what the server sent
    print('Server: "%s"' % data)

# this code should never be reached since the client doesn't stop
print('closing socket')
sock.close()
