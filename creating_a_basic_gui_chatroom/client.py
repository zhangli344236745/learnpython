#Client Side GUI Chat Room
import tkinter, socket, threading
from tkinter import DISABLED, VERTICAL, END, NORMAL

#Define window
root = tkinter.Tk()
root.title("Chat Client")
root.iconbitmap("message_icon.ico")
root.geometry("600x600")
root.resizable(0,0)

#Define fonts and colors
my_font = ('SimSun', 14)
black = "#010101"
light_green = "#1fc742"
root.config(bg=black)

#Define socket constants
ENCODER = 'utf-8'
BYTESIZE = 1024
global client_socket

def connect():
    global client_socket
    my_listbox.delete(0,END)

    name = name_entry.get()
    ip = ip_entry.get()
    port = port_entry.get()

    if name and ip and port:
        my_listbox.insert(0,f"{name} is waiting to connect to {ip} at {port}...")
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((ip,int(port)))
        verify_connection(name)
    else:
        my_listbox.insert(0,"Insufficient information for connection...")

def verify_connection(name):
    global  client_socket
    flag = client_socket.recv(BYTESIZE).decode(ENCODER)
    if flag == "NAME":
        client_socket.send(name.encode(ENCODER))
        message = client_socket.recv(BYTESIZE).decode(ENCODER)
        if message:
            # Server sent a verification, connection is valid!
            my_listbox.insert(0, message)

            # Change button/entry states
            connect_button.config(state=DISABLED)
            disconnect_button.config(state=NORMAL)
            send_button.config(state=NORMAL)

            name_entry.config(state=DISABLED)
            ip_entry.config(state=DISABLED)
            port_entry.config(state=DISABLED)

            # Create a thread to contiuously recieve messages from the server
            recieve_thread = threading.Thread(target=recieve_message)
            recieve_thread.start()
        else:
            # No verification message was recieved
            my_listbox.insert(0, "Connection not verified.  Goodbye...")
            client_socket.close()
    else:
        # No name flag was sent, connection was refused
        my_listbox.insert(0, "Connection refused.  Goodbye...")
        client_socket.close()
def disconnect():
    global client_socket

    # Close the socket
    client_socket.close()

    # Change button/entry states
    connect_button.config(state=NORMAL)
    disconnect_button.config(state=DISABLED)
    send_button.config(state=DISABLED)

    name_entry.config(state=NORMAL)
    ip_entry.config(state=NORMAL)
    port_entry.config(state=NORMAL)

def send_message():
    global client_socket
    message = input_entry.get()
    client_socket.send(message.encode(ENCODER))
    input_entry.delete(0,END)

def recieve_message():
    global client_socket
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            my_listbox.insert(0,message)
        except:
            my_listbox.insert(0,"Closing the connection.  Goodbye...")
            disconnect()
            break

info_frame = tkinter.Frame(root,bg=black)
output_frame = tkinter.Frame(root,bg=black)
input_frame = tkinter.Frame(root,bg=black)

info_frame.pack()
output_frame.pack(pady=10)
input_frame.pack()

name_label = tkinter.Label(info_frame, text="Client Name:", font=my_font, fg=light_green, bg=black)
name_entry = tkinter.Entry(info_frame,borderwidth=3, font=my_font)
ip_label = tkinter.Label(info_frame, text="Host IP:", font=my_font, fg=light_green, bg=black)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
port_label = tkinter.Label(info_frame, text="Port Num:", font=my_font, fg=light_green, bg=black)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)
connect_button = tkinter.Button(info_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10, command=connect)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font, bg=light_green, borderwidth=5, width=10, state=DISABLED, command=disconnect)


name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)

#Output Frame Layout
my_scrollbar = tkinter.Scrollbar(output_frame, orient=VERTICAL)
my_listbox = tkinter.Listbox(output_frame, height=20, width=55, borderwidth=3, bg=black, fg=light_green, font=my_font, yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)

my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

#Input Frame Layout
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tkinter.Button(input_frame, text="send", borderwidth=5, width=10, font=my_font, bg=light_green, state=DISABLED, command=send_message)
input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)

#Run the root window's mainloop()
root.mainloop()
