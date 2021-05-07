#!/usr/bin/python3
import socket
import threading, time
from module import handle_conn, send_message, get_ip
import sys

# gets the IP address of the current machine
SERVER = get_ip()


def main(port: int):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((SERVER, port))
        server.listen()
        print(f"Listening on {SERVER}:{port}")
        conn, addr = server.accept()  # accept 1 connection
        get_msg = threading.Thread(
            target=handle_conn, args=(conn, addr), daemon=True)
        send_msg = threading.Thread(
            target=send_message, args=(conn,))

        get_msg.setDaemon(True)
        send_msg.setDaemon(True)
        get_msg.start()
        send_msg.start()
        while True:
            for _ in range(10):
                time.sleep(.2)
    except KeyboardInterrupt:
        print("\nEnding server")
        exit(1)
    except Exception as e:
        print(f"[ERR] {e}")
        return


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            port = int(sys.argv[1])
            if port > 65535 or port < 1:
                print("[ERR] Invalid port number.")
                exit()
            main(port)
        else:
            print("Arguement missing: python3 listener.py <portnumber>")
    except Exception as e:
        print(f"[ERR] {e}")
        exit()
    except KeyboardInterrupt:
        print("[ERR] : Stopping listener")
        exit()
