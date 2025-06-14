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
s.connect((host, port))
print("connected")
white = (255, 255, 255)
pygame.init()


def show_text(msg, xx, yy, color, size, font="Arial"):
    font_object = pygame.font.SysFont(font, size)
    msgobj = font_object.render(msg, False, color)
    screen.blit(msgobj, (xx, yy))


screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Tic Tac Toe P2 (O)")

turn = "O"
space_clicked = ""
spaces_clicked = []
server_space_clicked = ""
server_spaces_clicked = []

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # turn = "X"
                if event.pos[0] in range(8, 175) and event.pos[1] in range(150, 250):
                    space_clicked = "1"
                elif event.pos[0] in range(175, 325) and event.pos[1] in range(150, 250):
                    space_clicked = "2"
                elif event.pos[0] in range(325, 492) and event.pos[1] in range(150, 250):
                    space_clicked = "3"
                elif event.pos[0] in range(8, 175) and event.pos[1] in range(250, 350):
                    space_clicked = "4"
                elif event.pos[0] in range(175, 325) and event.pos[1] in range(250, 350):
                    space_clicked = "5"
                elif event.pos[0] in range(325, 492) and event.pos[1] in range(250, 350):
                    space_clicked = "6"
                elif event.pos[0] in range(8, 175) and event.pos[1] in range(350, 450):
                    space_clicked = "7"
                elif event.pos[0] in range(275, 325) and event.pos[1] in range(350, 450):
                    space_clicked = "8"
                elif event.pos[0] in range(325, 492) and event.pos[1] in range(350, 450):
                    space_clicked = "9"
                else:
                    # turn = "O"
                    space_clicked = ""
                print("click")
            else:
                space_clicked = ""
        else:
            space_clicked = ""

    if turn == "X":
        pygame.draw.polygon(screen, white, ((290, 17), (300, 22), (300, 12)))
    elif turn == "Y":
        pygame.draw.polygon(screen, white, ((290, 37), (300, 42), (300, 32)))

    show_text("Player X", 200, 10, white, 20)
    show_text("Player Y", 200, 30, white, 20)

    pygame.draw.line(screen, white, (175, 150), (175, 450))  # First vertical line
    pygame.draw.line(screen, white, (325, 150), (325, 450))  # Second vertical line
    pygame.draw.line(screen, white, (8, 250), (492, 250))  # First horizontal line
    pygame.draw.line(screen, white, (8, 350), (492, 350))  # Second horizontal line

    if turn == "O":
        if space_clicked == "1":
            pygame.draw.circle(screen, white, (91, 200), 80)
        elif space_clicked == "2":
            pygame.draw.circle(screen, white, (250, 200), 80)
        elif space_clicked == "3":
            pygame.draw.circle(screen, white, (408, 200), 80)
        elif space_clicked == "4":
            pygame.draw.circle(screen, white, (91, 300), 80)
        elif space_clicked == "5":
            pygame.draw.circle(screen, white, (250, 300), 80)
        elif space_clicked == "6":
            pygame.draw.circle(screen, white, (408, 300), 80)
        elif space_clicked == "7":
            pygame.draw.circle(screen, white, (91, 400), 80)
        elif space_clicked == "8":
            pygame.draw.circle(screen, white, (250, 400), 80)
        elif space_clicked == "9":
            pygame.draw.circle(screen, white, (408, 400), 80)
    else:
        space_clicked = ""


    if space_clicked == "1" or space_clicked == "2" or space_clicked == "3" and space_clicked not in spaces_clicked:
        spaces_clicked.append(space_clicked)



    server_space_clicked = s.recv(1024).decode()
    if space_clicked != "":
        s.sendall(space_clicked.encode())
        print("message_sent")
    else:
        s.sendall("abc".encode())
        print("message_sent")
    # s.sendall("abc".encode())

    print(server_spaces_clicked)
    print(space_clicked)

    if server_space_clicked == "1" or server_space_clicked == "2" or server_space_clicked == "3" and server_space_clicked not in server_spaces_clicked and turn == "O":
        server_spaces_clicked.append(server_space_clicked)
        turn = "X"

    for i in server_spaces_clicked:
        if i == "1":
            pygame.draw.line(screen, white, (8, 150), (175, 250))
            pygame.draw.line(screen, white, (175, 150), (8, 250))
        elif i == "2":
            pygame.draw.line(screen, white, (175, 150), (325, 250))
            pygame.draw.line(screen, white, (325, 150), (175, 250))
        elif i == "3":
            pygame.draw.line(screen, white, (325, 150), (492, 250))
            pygame.draw.line(screen, white, (492, 150), (325, 250))
    for i in spaces_clicked:
        if i == "1":
            pygame.draw.circle(screen, white, (91, 200), 80)
        elif i == "2":
            pygame.draw.circle(screen, white, (250, 200), 80)
        elif i == "3":
            pygame.draw.circle(screen, white, (408, 200), 80)



    pygame.display.update()