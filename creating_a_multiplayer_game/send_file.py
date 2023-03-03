from __future__ import annotations

import socket

def send_file(filename:str = "mytext.txt",testing:bool = False) -> None:
    port = 12312
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    sock.bind((host,port))
    sock.listen(5)

    print("Server listening....")
    while True:
        conn,addr = sock.accept()
        print(f"Got connection from {addr}")
        data = conn.recv(1024)
        print(f"Server received:{data}")
        with open(filename,"rb") as in_file:
            data = in_file.read(1024)
            while data:
                conn.send(data)
                print(f"send {data}")
                data = in_file.read(1024)
        print("data sending")
        conn.close()
        if  testing:
            break
    sock.shutdown(1)
    sock.close()


if __name__ == "__main__":
    print("hello")
    send_file()