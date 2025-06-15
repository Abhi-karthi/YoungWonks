import socket
import atexit
from tkinter import *
import threading

number_of_clients = 3


def send_all(data):
    global clients
    for i in clients:
        i.sendall(data.encode())


def receive_data(conn):
    print(1)
    while True:
        # print(data)
        new_data = conn.recv(1024).decode()
        real_data = new_data[0:-7]
        key = new_data[-7:-1] + new_data[-1]
        print(real_data)
        if key[0:-1] == "client":
            data.append([key, real_data])
            print("Received", new_data)

        # labels[-1].pack()


def send_data(conn):
    global data
    main_string = ""
    for i in data:
        main_string += "||"
        main_string += i

    send_all(main_string)

    # global server_key
    # if chat_info[-1] not in data_sent:
    #     data = chat_info[-1] + server_key
    #     conn.sendall(data.encode())
    #     data_sent.append(chat_info[-1])
    # print("sent")


def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()


atexit.register(handle_exit)

s = socket.socket(socket.AF_INET, socket .SOCK_STREAM)
threads = []

host = '172.30.22.0'
port = 10000
s.bind((host, port))
s.listen(5)
clients = {}
data = []
threads_in_server_for_receive_and_send = []


def new_thread_for_receive_and_send(conn):
    global threads_in_server_for_receive_and_send
    print("running")
    threads_in_server_for_receive_and_send.append(threading.Thread(receive_data, args=(conn,)))
    threads_in_server_for_receive_and_send.append(threading.Thread(send_data, args=(conn,)))
    threads_in_server_for_receive_and_send[-2].start()
    threads_in_server_for_receive_and_send[-1].start()


def accept():
    global threads
    while True:
        conn, addr = s.accept()
        clients[conn] = addr
        threads.append(threading.Thread(target=new_thread_for_receive_and_send, args=(conn,)))
        print(threads)
        threads[-1].start()


root = Tk()
root.title("Chat Server")

chat_widget = Frame(root)
labels = []
chat_info = []
data_sent = []
entry = Entry(root)
server_key = "server7"


# def button_command():
#     labels.append(Label(chat_widget, text=f"{entry.get()}"))
#     chat_info.append(entry.get())
#     send_data("sdf")
#     print(chat_info)
#     labels[-1].pack()







# recp = threading.Thread(target=receive_data)

# recp.start()



# button = Button(root, text="Enter", command=button_command)

chat_widget.pack()
# label.pack()
# for i in labels:
#     i.pack()
entry.pack()
# button.pack()

root.mainloop()