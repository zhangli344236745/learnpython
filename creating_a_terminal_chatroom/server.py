#Server Side Chat Room
import socket, threading

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

#Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

client_socket_list = []
client_name_list = []

def broadcast_message(message):
    for client_socket in client_socket_list:
        client_socket.send(message)

def recieve_message(client_socket):
    while True:
        try:
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            message = f"\033[1;92m\t{name}: {message}\033[0m".encode(ENCODER)
            broadcast_message(message)
        except:
            # Find the index of the client socket in our list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # Close the client socket
            client_socket.close()

            # Broadcast that the client has left the chat.
            broadcast_message(f"\033[5;91m\t{name} has left the chat!\033[0m".encode(ENCODER))
            break

def connect_client():
    while True:
        client_socket,client_address = server_socket.accept()
        print(f"Connected with {client_address}...")
        client_socket.send("Name".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        print(f"Name of new client is {client_name}\n")
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER))
        broadcast_message(f"{client_name} has joined the chat!".encode(ENCODER))

        recieve_thread = threading.Thread(target=recieve_message,args=(client_socket,))
        recieve_thread.start()


#Start the server
print("Server is listening for incoming connections...\n")
connect_client()
