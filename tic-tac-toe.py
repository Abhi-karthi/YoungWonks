import pygame
import random
import time


def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
# # # # # # # # # # # # # # #   # #  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
grey = (127, 127, 127)
black = (0, 0, 0)
pygame.init()
colors = [white, red, green, blue, purple]
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Tic tac toe")
turn = "X"
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
game_mode = 0
first = 0
a = 0
while True:

    while game_mode == 0:
        pygame.draw.rect(screen, white, (275, 50, 200, 50))
        pygame.draw.rect(screen, white, (275, 150, 200, 50))
        show_text("Single Player", 275, 50, black, 30)
        show_text("Multi Player", 275, 150, black, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(275, 475) and pygame.mouse.get_pos()[1] in range(50, 100):
                    game_mode = 1
                if pygame.mouse.get_pos()[0] in range(275, 475) and pygame.mouse.get_pos()[1] in range(150, 200):
                    game_mode = 2
        pygame.display.update()
        screen.fill(black)
    pygame.draw.line(screen, white, (275, 100), (275, 400), 5)
    pygame.draw.line(screen, white, (425, 100), (425, 400), 5)
    pygame.draw.line(screen, white, (150, 200), (550, 200), 5)
    pygame.draw.line(screen, white, (150, 300), (550, 300), 5)
    if game_mode == 1:
        if first == 0:
            screen.fill(black)
            pygame.draw.rect(screen, white, (275, 50, 200, 50))
            pygame.draw.rect(screen, white, (275, 150, 200, 50))
            pygame.draw.rect(screen, white, (0, 450, 100, 50))
            show_text("X", 275, 50, black, 30)
            show_text("O", 275, 150, black, 30)
            show_text("Back", 0, 450, black, 30)
            show_text("What letter do you want to be? X goes first.", 0, 0, white, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] in range(275, 475) and pygame.mouse.get_pos()[1] in range(50, 100):
                        first = 1
                        screen.fill(black)
                    if pygame.mouse.get_pos()[0] in range(275, 475) and pygame.mouse.get_pos()[1] in range(150, 200):
                        first = 2
                        screen.fill(black)
                    if pygame.mouse.get_pos()[0] in range(0, 100) and pygame.mouse.get_pos()[1] in range(450, 500):
                        game_mode = 0
                        screen.fill(black)
        if first == 1:
            pygame.draw.rect(screen, white, (0, 450, 100, 50))
            show_text("Quit", 0, 450, black, 30)
            if turn == "O":
                if board[0] == "X" and board[1] == "X" and board[2] != "O" and board[2] != "X":
                    board[2] = "O"
                    turn = "X"
                elif board[0] == "X" and board[2] == "X" and board[1] != "O" and board[1] != "X":
                    board[1] = "O"
                    turn = "X"
                elif board[1] == "X" and board[2] == "X" and board[0] != "O" and board[0] != "X":
                    board[0] = "O"
                    turn = "X"

                elif board[3] == "X" and board[4] == "X" and board[5] != "O" and board[5] != "X":
                    board[5] = "O"
                    turn = "X"
                elif board[3] == "X" and board[5] == "X" and board[4] != "O" and board[4] != "X":
                    board[4] = "O"
                    turn = "X"
                elif board[5] == "X" and board[4] == "X" and board[3] != "O" and board[3] != "X":
                    board[3] = "O"
                    turn = "X"

                elif board[6] == "X" and board[7] == "X" and board[8] != "O" and board[8] != "X":
                    board[8] = "O"
                    turn = "X"
                elif board[6] == "X" and board[8] == "X" and board[7] != "O" and board[7] != "X":
                    board[7] = "O"
                    turn = "X"
                elif board[8] == "X" and board[7] == "X" and board[6] != "O" and board[6] != "X":
                    board[6] = "O"
                    turn = "X"

                elif board[0] == "X" and board[3] == "X" and board[6] != "O" and board[6] != "X":
                    board[6] = "O"
                    turn = "X"
                elif board[0] == "X" and board[6] == "X" and board[3] != "O" and board[3] != "X":
                    board[3] = "O"
                    turn = "X"
                elif board[6] == "X" and board[3] == "X" and board[0] != "O" and board[0] != "X":
                    board[0] = "O"
                    turn = "X"

                elif board[1] == "X" and board[4] == "X" and board[7] != "O" and board[7] != "X":
                    board[7] = "O"
                    turn = "X"
                elif board[1] == "X" and board[7] == "X" and board[4] != "O" and board[4] != "X":
                    board[4] = "O"
                    turn = "X"
                elif board[7] == "X" and board[4] == "X" and board[1] != "O" and board[1] != "X":
                    board[1] = "O"
                    turn = "X"

                elif board[2] == "X" and board[5] == "X" and board[8] != "O" and board[8] != "X":
                    board[8] = "O"
                    turn = "X"
                elif board[2] == "X" and board[8] == "X" and board[5] != "O" and board[5] != "X":
                    board[5] = "O"
                    turn = "X"
                elif board[8] == "X" and board[5] == "X" and board[2] != "O" and board[2] != "X":
                    board[2] = "O"
                    turn = "X"

                elif board[0] == "X" and board[4] == "X" and board[8] != "O" and board[8] != "X":
                    board[8] = "O"
                    turn = "X"
                elif board[0] == "X" and board[8] == "X" and board[4] != "O" and board[4] != "X":
                    board[4] = "O"
                    turn = "X"
                elif board[8] == "X" and board[4] == "X" and board[0] != "O" and board[0] != "X":
                    board[0] = "O"
                    turn = "X"

                elif board[2] == "X" and board[4] == "X" and board[6] != "O" and board[6] != "X":
                    board[8] = "O"
                    turn = "X"
                elif board[2] == "X" and board[6] == "X" and board[4] != "O" and board[4] != "X":
                    board[4] = "O"
                    turn = "X"
                elif board[4] == "X" and board[6] == "X" and board[2] != "O" and board[2] != "X":
                    board[2] = "O"
                    turn = "X"

                else:
                    while a == 0:
                        b = random.randint(0, 8)
                        if board[b] == 0:
                            board[b] = "O"
                            turn = "X"
                            a = 1
                    a = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(100, 200) and board[0] != "X" and board[0] != "O":
                        board[0] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(100, 200) and board[1] != "X" and board[1] != "O":
                        board[1] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(100, 200) and board[2] != "X" and board[2] != "O":
                        board[2] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(200, 300) and board[3] != "X" and board[3] != "O":
                        board[3] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(200, 300) and board[4] != "X" and board[4] != "O":
                        board[4] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(200, 300) and board[5] != "X" and board[5] != "O":
                        board[5] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(300, 400) and board[6] != "X" and board[6] != "O":
                        board[6] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(300, 400) and board[7] != "X" and board[7] != "O":
                        board[7] = "X"
                        turn = "O"
                    if turn == "X" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(300, 400) and board[8] != "X" and board[8] != "O":
                        board[8] = "X"
                        turn = "O"
                    if pygame.mouse.get_pos()[0] in range(0, 100) and pygame.mouse.get_pos()[1] in range(450, 500):
                        game_mode = 0
                        first = 0
                        turn = "X"
                        for i in range(0, 9):
                            board[i] = 0
        if first == 2:
            pygame.draw.rect(screen, white, (0, 450, 100, 50))
            show_text("Quit", 0, 450, black, 30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(100, 200) and board[0] != "X" and board[0] != "O":
                        board[0] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(100, 200) and board[1] != "X" and board[1] != "O":
                        board[1] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(100, 200) and board[2] != "X" and board[2] != "O":
                        board[2] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(200, 300) and board[3] != "X" and board[3] != "O":
                        board[3] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(200, 300) and board[4] != "X" and board[4] != "O":
                        board[4] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(200, 300) and board[5] != "X" and board[5] != "O":
                        board[5] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(300, 400) and board[6] != "X" and board[6] != "O":
                        board[6] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(300, 400) and board[7] != "X" and board[7] != "O":
                        board[7] = "O"
                        turn = "X"
                    if turn == "O" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(300, 400) and board[8] != "X" and board[8] != "O":
                        board[8] = "O"
                        turn = "X"
                    if pygame.mouse.get_pos()[0] in range(0, 100) and pygame.mouse.get_pos()[1] in range(450, 500):
                        game_mode = 0
                        first = 0
                        turn = "X"
                        for i in range(0, 9):
                            board[i] = 0
            if turn == "X":

                if board[0] == "O" and board[1] == "O" and board[2] != "X" and board[2] != "O":
                    board[2] = "X"
                    turn = "O"
                elif board[0] == "O" and board[2] == "O" and board[1] != "X" and board[1] != "O":
                    board[1] = "X"
                    turn = "O"
                elif board[1] == "O" and board[2] == "O" and board[0] != "X" and board[0] != "O":
                    board[0] = "X"
                    turn = "O"

                elif board[3] == "O" and board[4] == "O" and board[5] != "X" and board[5] != "O":
                    board[5] = "X"
                    turn = "O"
                elif board[3] == "O" and board[5] == "O" and board[4] != "X" and board[4] != "O":
                    board[4] = "X"
                    turn = "O"
                elif board[5] == "O" and board[4] == "O" and board[3] != "X" and board[3] != "O":
                    board[3] = "X"
                    turn = "O"

                elif board[6] == "O" and board[7] == "O" and board[8] != "X" and board[8] != "O":
                    board[8] = "X"
                    turn = "O"
                elif board[6] == "O" and board[8] == "O" and board[7] != "X" and board[7] != "O":
                    board[7] = "X"
                    turn = "O"
                elif board[8] == "O" and board[7] == "O" and board[6] != "X" and board[6] != "O":
                    board[6] = "X"
                    turn = "O"

                elif board[0] == "O" and board[3] == "O" and board[6] != "X" and board[6] != "O":
                    board[6] = "X"
                    turn = "O"
                elif board[0] == "O" and board[6] == "O" and board[3] != "X" and board[3] != "O":
                    board[3] = "X"
                    turn = "O"
                elif board[6] == "O" and board[3] == "O" and board[0] != "X" and board[0] != "O":
                    board[0] = "X"
                    turn = "O"

                elif board[1] == "O" and board[4] == "O" and board[7] != "X" and board[7] != "O":
                    board[7] = "X"
                    turn = "O"
                elif board[1] == "O" and board[7] == "O" and board[4] != "X" and board[4] != "O":
                    board[4] = "X"
                    turn = "O"
                elif board[7] == "O" and board[4] == "O" and board[1] != "X" and board[1] != "O":
                    board[1] = "X"
                    turn = "O"

                elif board[2] == "O" and board[5] == "O" and board[8] != "X" and board[8] != "O":
                    board[8] = "X"
                    turn = "O"
                elif board[2] == "O" and board[8] == "O" and board[5] != "X" and board[5] != "O":
                    board[5] = "X"
                    turn = "O"
                elif board[8] == "O" and board[5] == "O" and board[2] != "X" and board[2] != "O":
                    board[2] = "X"
                    turn = "O"

                elif board[0] == "O" and board[4] == "O" and board[8] != "X" and board[8] != "O":
                    board[8] = "X"
                    turn = "O"
                elif board[0] == "O" and board[8] == "O" and board[4] != "X" and board[4] != "O":
                    board[4] = "X"
                    turn = "O"
                elif board[8] == "O" and board[4] == "O" and board[0] != "X" and board[0] != "O":
                    board[0] = "X"
                    turn = "O"

                elif board[2] == "O" and board[4] == "O" and board[6] != "X" and board[6] != "O":
                    board[8] = "X"
                    turn = "O"
                elif board[2] == "O" and board[6] == "O" and board[4] != "X" and board[4] != "O":
                    board[4] = "X"
                    turn = "O"
                elif board[4] == "O" and board[6] == "O" and board[2] != "X" and board[2] != "O":
                    board[2] = "X"
                    turn = "O"

                else:
                    while a == 0:
                        b = random.randint(0, 8)
                        if board[b] == 0:
                            board[b] = "X"
                            turn = "O"
                            a = 1
                    a = 0

    if game_mode == 2:
        pygame.draw.rect(screen, white, (0, 450, 100, 50))
        show_text("Quit", 0, 450, black, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == "X" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(100, 200) and board[0] != "X" and board[0] != "O":
                    board[0] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(100, 200) and board[1] != "X" and board[1] != "O":
                    board[1] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(100, 200) and board[2] != "X" and board[2] != "O":
                    board[2] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(200, 300) and board[3] != "X" and board[3] != "O":
                    board[3] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(200, 300) and board[4] != "X" and board[4] != "O":
                    board[4] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(200, 300) and board[5] != "X" and board[5] != "O":
                    board[5] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(300, 400) and board[6] != "X" and board[6] != "O":
                    board[6] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(300, 400) and board[7] != "X" and board[7] != "O":
                    board[7] = "X"
                    turn = "O"
                if turn == "X" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(300, 400) and board[8] != "X" and board[8] != "O":
                    board[8] = "X"
                    turn = "O"

                if turn == "O" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(100, 200) and board[0] != "X" and board[0] != "O":
                    board[0] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(100, 200) and board[1] != "X" and board[1] != "O":
                    board[1] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(100, 200) and board[2] != "X" and board[2] != "O":
                    board[2] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(200, 300) and board[3] != "X" and board[3] != "O":
                    board[3] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(200, 300) and board[4] != "X" and board[4] != "O":
                    board[4] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(200, 300) and board[5] != "X" and board[5] != "O":
                    board[5] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(150, 275) and pygame.mouse.get_pos()[1] in range(300, 400) and board[6] != "X" and board[6] != "O":
                    board[6] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(275, 425) and pygame.mouse.get_pos()[1] in range(300, 400) and board[7] != "X" and board[7] != "O":
                    board[7] = "O"
                    turn = "X"
                if turn == "O" and pygame.mouse.get_pos()[0] in range(425, 550) and pygame.mouse.get_pos()[1] in range(300, 400) and board[8] != "X" and board[8] != "O":
                    board[8] = "O"
                    turn = "X"
                if pygame.mouse.get_pos()[0] in range(0, 100) and pygame.mouse.get_pos()[1] in range(450, 500):
                    game_mode = 0
                    first = 0
                    turn = "X"
                    for i in range(0, 9):
                        board[i] = 0
    if board[0] == "X":
        show_text("X", 150, 100, white, 100)
    if board[1] == "X":
        show_text("X", 275, 100, white, 100)
    if board[2] == "X":
        show_text("X", 425, 100, white, 100)
    if board[3] == "X":
        show_text("X", 150, 200, white, 100)
    if board[4] == "X":
        show_text("X", 275, 200, white, 100)
    if board[5] == "X":
        show_text("X", 425, 200, white, 100)
    if board[6] == "X":
        show_text("X", 150, 300, white, 100)
    if board[7] == "X":
        show_text("X", 275, 300, white, 100)
    if board[8] == "X":
        show_text("X", 425, 300, white, 100)

    if board[0] == "O":
        show_text("O", 150, 100, white, 100)
    if board[1] == "O":
        show_text("O", 275, 100, white, 100)
    if board[2] == "O":
        show_text("O", 425, 100, white, 100)
    if board[3] == "O":
        show_text("O", 150, 200, white, 100)
    if board[4] == "O":
        show_text("O", 275, 200, white, 100)
    if board[5] == "O":
        show_text("O", 425, 200, white, 100)
    if board[6] == "O":
        show_text("O", 150, 300, white, 100)
    if board[7] == "O":
        show_text("O", 275, 300, white, 100)
    if board[8] == "O":
        show_text("O", 425, 300, white, 100)

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 150), (550, 150), 3)
        pygame.display.update()
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 150), (550, 150), 3)
        pygame.display.update()
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 250), (550, 250), 3)
        pygame.display.update()
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 250), (550, 250), 3)
        pygame.display.update()
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 350), (550, 350), 3)
        pygame.display.update()
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 350), (550, 350), 3)
        pygame.display.update()
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (212, 100), (212, 400), 3)
        pygame.display.update()
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (212, 100), (212, 400), 3)
        pygame.display.update()
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (350, 100), (350, 400), 3)
        pygame.display.update()
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (350, 100), (350, 400), 3)
        pygame.display.update()
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (487, 100), (487, 400), 3)
        pygame.display.update()
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (487, 100), (487, 400), 3)
        pygame.display.update()
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 100), (550, 400), 3)
        pygame.display.update()
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (150, 100), (550, 400), 3)
        pygame.display.update()
    if board[2] == "X" and board[4] == "X" and board[6] == "X":
        show_text("X Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (550, 100), (150, 400), 3)
        pygame.display.update()
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        show_text("O Wins!", 0, 0, white, 35)
        pygame.draw.line(screen, white, (550, 100), (150, 400), 3)
        pygame.display.update()
    if board[0] != 0 and board[1] != 0 and board[2] != 0 and board[3] != 0 and board[4] != 0 and board[5] != 0 and board[6] != 0 and board[7] != 0 and board[8] != 0:
        show_text("Draw!", 0, 0, white, 35)
        pygame.display.update()
    pygame.display.update()
