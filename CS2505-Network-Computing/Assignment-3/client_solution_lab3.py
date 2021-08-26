# from the socket module import all
from socket import *
# import sys to use the command line arguments
import sys

# get the command line arguments
command_line_list = sys.argv
# find ip address in the arguments
ip_address = command_line_list[1]
# find port number and make it an integer to use in the socket
port_num = int(command_line_list[2])
# find pathway for file
pathname = command_line_list[3]

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# set values for the server address using command line arguments
# the machine address and port number have to be the same as the server is using.
server_address = (ip_address, port_num)
# get value for domain name
domain_name = gethostname()
# output to terminal some info on the address details
print('* Connecting to server with ip address %s *' % ip_address)
# Connect the socket to the host and port
sock.connect(server_address)

try:

    print("Requesting file at path name %s" % pathname)
    # composing the message to be sent
    message_to_send = "GET %s HTTP/1.1" % pathname
    # request the file at the given pathname
    sock.sendall(message_to_send.encode())
    # the below while loop will run until there is no more data being sent by the server
    total_data = ""
    while True:
        # receive part of the data
        data = sock.recv(256).decode()
        # if it reaches the end of webpage
        if data == "\r\n":
            break
        # if theres no more data
        if not data:
            break
        total_data += data
    # print everything the server sent back
    print(total_data)

finally:
    print('closing socket')
    sock.close()
