import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

mesage = client_socket.recv(1024)
print(mesage.decode("utf-8"))
client_socket.close()