import socket, threading

#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

#Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def send_message():
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))

def recieve_message():
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if message == "NAME":
                name = input("what is your name")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            print("An error occured...")
            client_socket.close()
            break


recieve_thread = threading.Thread(target=recieve_message)
send_thread = threading.Thread(target=send_message)

recieve_thread.start()
send_thread.start()