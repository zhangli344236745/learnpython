import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("www.baidu.com",80))
client_socket.send("GET / HTTP/1.0\r\n\r\n".encode("utf-8"))
data = client_socket.recv(4096)
client_socket.close()
print(data.decode("utf-8"))