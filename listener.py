#!/usr/bin/python
#COHNDNE201f-021

import socket
import threading
from module import handle_conn, send_message, ADDR

#https://www.techwithtim.net/tutorials/socket-programming/
def main():
    try:
        # create socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)  # bind socket to port and server
        server.listen()  # start listening

        conn, addr = server.accept()  # accept 1 connection

        # Here, I used threading to asynchronously receive and send data between the client and server.
        # Threading simply creates a separate set of threads in memory. This helps the script to run without
        # having to wait for loops to end
        get_msg = threading.Thread(target=handle_conn,args=(conn, addr))  # this thread is used for receiving messages/data
        send_msg = threading.Thread(target=send_message,args=(conn,))  # this thread is used for sending messages/data

        # start both threads
        get_msg.start()
        send_msg.start()
    except Exception as e:
        print(f"[ERR] {e}")
        pass


if __name__ == "__main__":
    main()
