import socket
import os
import struct
import json

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8081))

file_size = os.path.getsize("./hello.txt")
data_dict = {
    "file_name": "hello.txt",
    "file_size": file_size,
}

data_dict_bytes = json.dumps(data_dict).encode("utf-8")
data_dict_len = struct.pack("i",len(data_dict_bytes))
client.send(data_dict_len)
client.send(data_dict_bytes)

with open("./hello.txt","rb") as file:
    for line in file:
        client.send(line)
