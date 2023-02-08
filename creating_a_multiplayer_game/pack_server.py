import socket
import struct
import json

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(("127.0.0.1",8081))
server_sock.listen()

client_sock, client_address = server_sock.accept()
data_dict_head = client_sock.recv(4)

data_dict_len = struct.unpack("i",data_dict_head)[0]
data_dict_bytes = client_sock.recv(data_dict_len)
data_dict = json.loads(data_dict_bytes)
print(data_dict)

total_size = data_dict.get("file_size")
recv_size = 0
with open("f"+data_dict.get("file_name"),"wb") as file:
    while recv_size < total_size:
        data = client_sock.recv(1024)
        file.write(data)
        recv_size += len(data)
        print(recv_size)
