import socket,json

message_packet = {
    "flag": "MESSAGE",
    "name": "Mile",
    "message": "This is my message coming through!",
    "color": "#00ff3f",
}

print(message_packet)
print(type(message_packet))

message_json = json.dumps(message_packet)
print(message_json)
print(type(message_json))

print(message_json.encode('utf-8'))
print(type(message_json.encode('utf-8')))

#Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
server_socket.listen()

while True:
    client_socket , client_address = server_socket.accept()
    print(f"Connect to {client_address} !\n")

    client_socket.send(message_json.encode('utf-8'))
    server_socket.close()
    break
