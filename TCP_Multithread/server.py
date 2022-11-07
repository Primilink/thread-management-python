import socket
import threading
import logging
from time import sleep

# define logging format with date, time, and message
logging.basicConfig(
    format='(%(threadName)-10s) %(asctime)s %(message)s', level=logging.DEBUG)


def client_handler(conn, addr):
    """ Handle client connection """
    # log the connection
    logging.debug('Connected by ' + str(addr))

    for i in range(15):
        # wait for a message from the client
        message = conn.recv(1024)

        response = {
            'status': 'OK',
            'data': message.decode(),
            'count': i
        }

        # send json data to client
        conn.sendall(str(response).encode())

        # long running process
        sleep(2)

    # close connection
    conn.close()

    # print closing message
    logging.debug('Connection closed by ' + str(addr))


if __name__ == '__main__':
    # create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define host and port
    host = 'localhost'
    port = 9999

    # bind to the port
    server.bind((host, port))

    # queue up to 5 requests
    server.listen(5)

    # log the server start
    logging.debug("Listening on " + host + ":" + str(port))

    while True:
        # establish a connection
        conn, addr = server.accept()

        # logging.debug("Got a connection from %s" % str(addr))

        # create a thread to handle the client
        clientThread = threading.Thread(
            target=client_handler, args=(conn, addr))

        # start the thread
        clientThread.start()
