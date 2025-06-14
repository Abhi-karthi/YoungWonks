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
print(s)
print("connected")

root = Tk()
root.title("Chat Client")
chat_widget = Frame(root)
labels = []
chat_info = []
data_sent = []
entry = Entry(root)
client1_key = "client1"


def button_command():
    labels.append(Label(chat_widget, text=f"{entry.get()}"))
    chat_info.append(entry.get())
    send_data()
    labels[-1].pack()
    print(labels)


def send_data():
    global client1_key
    if chat_info[-1] not in data_sent:
        data = chat_info[-1] + client1_key
        s.sendall(data.encode())
        data_sent.append(chat_info[-1])


def receive_data():
    global labels
    while True:
        new_data = s.recv(1024).decode()

        new_data_list = new_data.split("||")
        for i in new_data_list[::2]:
            if new_data_list[i] == "client1":
                labels.append(Label(chat_widget, text=f"{new_data_list[i]}", font="green"))
            elif new_data_list[i-1] == "client2":
                labels.append(Label(chat_widget, text=f"{new_data_list[i]}", font="red"))




        labels[-1].pack()


recp = threading.Thread(target=receive_data)
recp.start()

button = Button(root, text="Enter", command=button_command)

chat_widget.pack()
entry.pack()
button.pack()

root.mainloop()