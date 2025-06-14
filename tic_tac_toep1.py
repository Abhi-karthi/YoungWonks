import pygame
import socket
import atexit

def handle_exit():
    print("This runs after keyboard interrupt")
    s.close()

atexit.register(handle_exit)
host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("connected")
conn, addr = s.accept()
print("accepted")
white = (255, 255, 255)



def show_text(msg, xx, yy, color, size, font="Arial"):
    font_object = pygame.font.SysFont(font, size)
    msgobj = font_object.render(msg, False, color)
    screen.blit(msgobj, (xx, yy))

pygame.init()
screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Tic Tac Toe P1 (X)")



turn = "X"
space_clicked = ""
spaces_clicked = []
client_space_clicked = ""
client_spaces_clicked = []

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # turn = "O"
                if event.pos[0] in range(8, 175) and event.pos[1] in range(150, 250):
                    space_clicked = "1"
                elif event.pos[0] in range(175, 325) and event.pos[1] in range(150, 250):
                    space_clicked = "2"
                elif event.pos[0] in range(325, 492) and event.pos[1] in range(150, 250):
                    space_clicked = "3"
                else:
                    # turn = "X"
                    space_clicked = ""
                print("click")

    if turn == "X":
        pygame.draw.polygon(screen, white, ((290, 17), (300, 22), (300, 12)))
    elif turn == "Y":
        pygame.draw.polygon(screen, white, ((290, 37), (300, 42), (300, 32)))

    show_text("Player X", 200, 10, white, 20)
    show_text("Player Y", 200, 30, white, 20)

    pygame.draw.line(screen, white, (175, 150), (175, 450)) # First vertical line
    pygame.draw.line(screen, white, (325, 150), (325, 450)) # Second vertical line
    pygame.draw.line(screen, white, (8, 250), (492, 250)) # First horizontal line
    pygame.draw.line(screen, white, (8, 350), (492, 350)) # Second horizontal line

    if turn == "X":
        if space_clicked == "1":
            pygame.draw.line(screen, white, (8, 150), (175, 250))
            pygame.draw.line(screen, white, (175, 150), (8, 250))
        elif space_clicked == "2":
            pygame.draw.line(screen, white, (175, 150), (325, 250))
            pygame.draw.line(screen, white, (325, 150), (175, 250))
        elif space_clicked == "3":
            pygame.draw.line(screen, white, (325, 150), (492, 250))
            pygame.draw.line(screen, white, (492, 150), (325, 250))
    else:
        space_clicked = ""

    if space_clicked == "1" or space_clicked == "2" or space_clicked == "3" and space_clicked not in spaces_clicked and turn == "X":
        spaces_clicked.append(space_clicked)
        turn = "O"

    pygame.display.update()

    if space_clicked != "":
        conn.sendall(space_clicked.encode())
        print("message_sent")
    else:
        conn.sendall("abc".encode())
        print("message_sent")
    # conn.sendall("abc".encode())
    client_space_clicked = conn.recv(1024).decode()
    print(space_clicked)
    # print(conn.recv(1024))

    if client_space_clicked == "1" or client_space_clicked == "2" or client_space_clicked == "3" and client_space_clicked not in client_spaces_clicked:
        client_spaces_clicked.append(client_space_clicked)

    for i in client_spaces_clicked:
        if i == "1":
            pygame.draw.circle(screen, white, (91, 200), 80)
        elif i == "2":
            pygame.draw.circle(screen, white, (250, 200), 80)
        elif i == "3":
            pygame.draw.circle(screen, white, (408, 200), 80)
    for i in spaces_clicked:
        if i == "1":
            pygame.draw.line(screen, white, (8, 150), (175, 250))
            pygame.draw.line(screen, white, (175, 150), (8, 250))
        elif i == "2":
            pygame.draw.line(screen, white, (175, 150), (325, 250))
            pygame.draw.line(screen, white, (325, 150), (175, 250))
        elif i == "3":
            pygame.draw.line(screen, white, (325, 150), (492, 250))
            pygame.draw.line(screen, white, (492, 150), (325, 250))


    pygame.display.update()