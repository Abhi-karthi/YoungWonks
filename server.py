import socket
import atexit
def handle_exit():
    print("This runs after keyboard interrupt")
    s. close()

atexit.register(handle_exit)

s = socket.socket(socket.AF_INET, socket .SOCK_STREAM)

host = ''
port = 12345
s.bind ( (host, port))

s.listen(5)
print('Socket is listening')
conn, addr = s.accept()
print('Got a connection from ', addr, conn)

while True:
    data = input()
    conn. sendall(data.encode())
    data = conn.recv(1024)
    print (addr,":",data. decode())