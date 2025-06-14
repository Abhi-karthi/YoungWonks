import socket
import atexit
from tkinter import *
import threading


def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()

atexit.register(handle_exit)
host = '172.30.22.0'
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. connect ( (host, port))
print("connected")

root = Tk()
root.title("Chat Client")
chat_widget = Frame(root)
labels = []
chat_info = []
data_sent = []
entry = Entry(root)
client2_key = "client2"


def button_command():
    labels.append(Label(chat_widget, text=f"{entry.get()}"))
    chat_info.append("hello")
    send_data()
    labels[-1].pack()
    print(labels)


def send_data():
    global client2_key
    if chat_info[-1] not in data_sent:
        data = chat_info[-1] + client2_key
        s.sendall(data.encode())


def receive_data():
    while True:
        new_data = s.recv(1024).decode()

        real_data = new_data[0:-7]
        key = new_data[-7:-1] + new_data[-1]
        if key == "server7":
            labels.append(Label(chat_widget, text=real_data, background="red"))
        elif key == "client1":
            labels.append(Label(chat_widget, text=real_data, background="blue"))

        labels[-1].pack()


recp = threading.Thread(target=receive_data)
recp.start()

button = Button(root, text="Enter", command=button_command)
button_command()
chat_widget.pack()
entry.pack()
button.pack()

root.mainloop()