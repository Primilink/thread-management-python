# import socket
import socket
from random import randint

# create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client.connect(('localhost', 9999))

# send messages to server
for i in range(15):
    # send random message
    client.sendall(f'Hi message {randint(1,500)}'.encode())

    # wait for a message from the server
    message = client.recv(1024)

    # print the message
    print(f'From server: {message.decode()}')

# close the connection
client.close()
