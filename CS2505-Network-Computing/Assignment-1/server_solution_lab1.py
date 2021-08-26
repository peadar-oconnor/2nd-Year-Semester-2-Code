# from the socket module import all
from socket import *
# for finding the current date and time
from datetime import datetime

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get value for domain name
domain_name = gethostname()
# find ip address using hostname
ip_address = gethostbyname(domain_name)
# output to terminal some info on the address details
print('*** Server is starting up on %s with ip address %s ***' % (domain_name, ip_address))
# Bind the socket to the host and port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    
    try:
        print('connection from', client_address)

        # initialize variable to record all the data sent by client
        save_data = ""
        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            # records all the data sent by client
            save_data += data
            if data:
                print('received "%s"' % data)
                print('sending data back to the client')
                # encode() function returns bytes object
                connection.sendall(data.encode())
            else:
                # capture current date and time
                date_time = datetime.now()
                # open the log file
                log = open("log.txt", "a")
                # write to file
                log.write("\"%s\", sent at %s \n" % (save_data, date_time))
                log.close()
                # inform user that message was logged
                print("message has been saved to log file")
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()

# now close the socket
sock.close();