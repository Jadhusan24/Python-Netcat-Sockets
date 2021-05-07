#!/usr/bin/python3
import socket
import threading
import sys, time
from module import handle_conn, send_message


def main(port: int, server: str):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server, port))
        print("Connection establised to host. ")
        get_msg = threading.Thread(target=handle_conn, args=(
            client, (server, port)), daemon=True)
        send_msg = threading.Thread(
            target=send_message, args=(client,))
        
        get_msg.setDaemon(True)
        send_msg.setDaemon(True)
        # Here, I used threading to asynchronously receive and send data between the client and server.
        # Threading simply creates a separate set of threads in memory. This helps the script to run without
        # having to wait for loops to end
        get_msg.start() # this thread is used for receiving messages/data
        send_msg.start()  # this thread is used for sending messages/data

        while True:
            for _ in range(10):
                time.sleep(.2)
    except KeyboardInterrupt:
        print("\nDisconneccting from server")
        exit(1)
    except ConnectionRefusedError:
        print("[CONN ERR] Server refused connection!")
        exit()
    except Exception as e:
        print(f"[ERR] {e}")
        client.close()
        exit()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
            if port > 65535 or port < 1:
                print("[ERR] Invalid port number.")
                exit()
        except Exception as e:
            print(f"[ERR] {e}")
        except KeyboardInterrupt:
            print("[ERR] : Disconnected from host")
            exit()

        main(port, host)
    else:
        print("Arguement missing: python3 listener.py <host address> <portnumber>")
