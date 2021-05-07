#!/usr/bin/python3
import socket

HEADER = 64
PORT = 8888
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)  # connection tuple used by socket
FORMAT = "utf-8"  # encoding format


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def handle_conn(conn: socket.socket, addr):
    while True:
        try:
            msg_len = conn.recv(HEADER).decode(FORMAT)
            if msg_len:
                msg_len = int(msg_len)
                msg = conn.recv(msg_len).decode(FORMAT)
                print(msg)
        except ConnectionResetError:
            print(f"{addr} disconnected forcibly")
            break
    conn.close()


def send_message(conn: socket.socket):
    while True:
        try:
            msg = ""
            while not msg:
                msg = input("")
            send_len = str(len(msg)).encode(FORMAT)
            send_len += b' ' * (HEADER - len(send_len))
            conn.send(send_len)
            conn.send(msg.encode(FORMAT))
        except ConnectionResetError:
            pass
        except Exception as e:
            print(f"[ERR] {e}")
            break
