import socket
import select

server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)
server.setblocking(False)
read_list = [server]

while True:
    r_list,w_list,x_list = select.select(read_list,[],[])
    for item in r_list:
        if item is server:
            conn, addr = item.accept()
            read_list.append(conn)
        else:
            res = item.recv(1024)
            if len(res) == 0:
                item.close()
                read_list.remove(item)
                continue
            print(res.decode("utf-8"))
            item.send("hello python".encode("utf-8"))


