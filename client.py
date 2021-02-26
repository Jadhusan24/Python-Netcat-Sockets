#!/usr/bin/python
#COHNDNE201f-021

import socket
import threading
from module import handle_conn, send_message, ADDR
#sockets - https://docs.python.org/3/library/socket.html
#threading - https://realpython.com/intro-to-python-threading/

def main():
    try:
        # create socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)  # connect to an address

        # Here, I used threading to asynchronously receive and send data between the client and server.
        # Threading simply creates a separate set of threads in memory. This helps the script to run without
        # having to wait for loops to end
        get_msg = threading.Thread(target=handle_conn,args=(client, ADDR))  # this thread is used for receiving messages/data
        send_msg = threading.Thread(target=send_message,args=(client,))  # this thread is used for sending messages/data

        # start both threads
        get_msg.start()
        send_msg.start()
    except ConnectionRefusedError:
        print("[CONN ERR] Server refused connection!")
    except Exception as e:
        print(f"[ERR] {e}")


if __name__ == "__main__":
    main()
