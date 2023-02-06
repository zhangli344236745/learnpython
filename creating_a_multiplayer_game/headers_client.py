#An intro to using fixed lenght headers client
import socket, time

#Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

time.sleep(2)
header = client_socket.recv(10)
print(header)
print(len(header))

message = client_socket.recv(int(header))
print(message.decode('utf-8'))

time.sleep(2)
header = client_socket.recv(10)
print(header)
print(len(header))
message = client_socket.recv(int(header))
print(message.decode('utf-8'))