 # 客户端
import socket

client = socket.socket()
client.connect(('127.0.0.1',8080))

while True:

    client.send('hello world'.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode("utf-8"))
