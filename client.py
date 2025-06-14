import socket
import atexit
def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()

atexit.register(handle_exit)
host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. connect ( (host, port))
print("connected")

while True:
    data = s.recv(1024)
    print(data.decode())
    data = input ("Client:")
    s.sendall(data.encode())