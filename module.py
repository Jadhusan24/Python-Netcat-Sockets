#!/usr/bin/python
#COHNDNE201f-021

"""
This file serves as a module for this project.
It has some variables and functions used globally amongst other modules/files.
"""
import socket
#https://www.youtube.com/watch?v=3QiPPX-KeSc
# variables for socket connection
HEADER = 64
PORT = 8888
SERVER = socket.gethostbyname(socket.gethostname())  # gets the IP address of the current machine
ADDR = (SERVER, PORT)  # connection tuple used by socket
FORMAT = "utf-8"  # encoding format


def handle_conn(conn: socket.socket, addr):
    """
    :param:
        conn: a socket connection object used to receive/send messages.
        addr: a connection tuple returned when a connection is made, example; (server, port)
    :return: None
    """

    while True:
        try:
            msg_len = conn.recv(HEADER).decode(FORMAT)  # first value received is the header size of the message
            if msg_len:  # until the message is still left, keep receiving it.
                msg_len = int(msg_len)  # this reduces the message length after each receive.
                msg = conn.recv(msg_len).decode(FORMAT)  # receive and decode message

                print(msg)
        except ConnectionResetError:  # catch socket connection error
            print(f"{addr} disconnected forcibly")
            break

    conn.close()  # close connection once loop is broken


def send_message(conn: socket.socket):
    """
    :param conn: a socket connection object used to receive/send messages.
    :return: None
    """

    while True:
        try:
            msg = ""
            while not msg:  # run until the user inputs a valid (non empty) message
                msg = input("")

            # firstly, send the message's length
            send_len = str(len(msg)).encode(FORMAT)
            send_len += b' ' * (HEADER - len(send_len))  # padding
            conn.send(send_len)

            # now send the message itself
            conn.send(msg.encode(FORMAT))
        except ConnectionResetError:
            pass
        except Exception as e:
            print(f"[ERR] {e}")
            break
