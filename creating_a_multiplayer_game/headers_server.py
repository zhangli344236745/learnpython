import socket

#Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
server_socket.listen()

message_1 = "Hello, we are learning more about sockets!"
message_2 = "Goodbye, now we know about HEADERS!"

while True:
    client_socket,client_address = server_socket.accept()
    print(f"Conected to {client_address}\n")
    header = str(len(message_1))
    while len(header) < 10:
        header += " "
    client_socket.send(header.encode("utf-8"))
    client_socket.send(message_1.encode("utf-8"))

    header = str(len(message_2))
    while len(header) < 10:
        header += " "

    client_socket.send(header.encode('utf-8'))
    client_socket.send(message_2.encode('utf-8'))

