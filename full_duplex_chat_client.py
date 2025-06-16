import socket
import atexit
from tkinter import *
import threading

client_number = 1
number_of_clients = 3
client_colors = ["red", "green", "blue", "white", "orange"]


def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()


atexit.register(handle_exit)
host = '172.30.22.0'
port = 10010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print(s)
print("connected")

root = Tk()
root.title(f"Chat Client {client_number}")
chat_widget = Frame(root)
labels = []
chat_info = []
data_sent = 0
entry = Entry(root, fg=client_colors[client_number - 1])
client_key = f"client{client_number}"


def button_command():
    # labels.append(Label(chat_widget, text=f"{entry.get()}"))
    entry_text = entry.get()
    entry.delete(0, END)
    send_valid = True
    for i in range(len(entry_text)):
        if entry_text[i] == "|" and entry_text[i + 1] == "|":
            send_valid = False

    if send_valid:
        if len(entry_text) != 0:
            chat_info.append(entry_text)
    else:
        entry.insert(0, 'Sending "||" is invalid')
    # print(chat_info)
    # send_data()
    # labels[-1].pack()
    # print(labels)


def send_data():
    global client_key, data_sent
    while True:
        try:
            if len(chat_info) >= data_sent + 1:
                data = chat_info[-1] + client_key
                s.sendall(data.encode())
                data_sent += 1
            else:
                s.sendall("traaaaaaash".encode())
        except IndexError:
            pass


def receive_data():
    global labels, s
    print("1, 2")
    while True:
        print("hello")
        new_data = s.recv(1024).decode()
        print(new_data)
        new_data_list = new_data.split("||")
        clients_list = []
        main_data_list = []
        new_labels = []
        for i, v in enumerate(new_data_list):
            if i % 2 == 0:
                clients_list.append(v)
            else:
                main_data_list.append(v)

        for i in range(len(clients_list)):
            color_of_label = ""
            for x in range(number_of_clients):
                if clients_list[i] == f"client{x + 1}":
                    color_of_label = client_colors[x]
                    break
            try:
                print(i)
                new_labels.append(Label(chat_widget, text=main_data_list[i + 1], fg=f"{color_of_label}"))
            except TclError:
                pass

        if new_labels != labels:
            labels.append(new_labels[-1])
            labels[-1].pack()


recp = threading.Thread(target=receive_data)
send = threading.Thread(target=send_data)
recp.start()
send.start()

button = Button(root, text="Enter", command=button_command)

chat_widget.pack()
entry.pack()
button.pack()

root.mainloop()
