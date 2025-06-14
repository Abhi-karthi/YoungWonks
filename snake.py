import pygame
import random
import time


def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Comic Sans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


def check_collision(snake):
    # Check head collision with body (except the first element)
    for body_part in snake[1:]:
        if snake[0][0] == body_part[0] and snake[0][1] == body_part[1]:
            return True
    return False


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
grey = (127, 127, 127)
black = (0, 0, 0)
clock = pygame.time.Clock()
pygame.init()
colors = [white, red, green, blue, purple]
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
foodx = (random.randint(0,590) // 10) * 10
foody = (random.randint(0,590) // 10) * 10
snakex = (random.randint(0,590) // 10) * 10
snakey = (random.randint(0,590) // 10) * 10
up = False
right = True
down = False
left = False
snake = [[snakex, snakey, 0]]
move = time.time()
popper = True
x = 0
mylist = []
frame = True
score = 0
while True:
    screen.fill(black)
    for i in snake:
        pygame.draw.rect(screen, green, (i[0], i[1], 10,10))
    pygame.draw.rect(screen, red, (foodx, foody, 10, 10))
    frame = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if frame:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if not up:
                        down = True
                        left = False
                        up = False
                        right = False
                elif event.key == pygame.K_RIGHT:
                    if not left:
                        down = False
                        left = False
                        up = False
                        right = True
                elif event.key == pygame.K_UP:
                    if not down:
                        down = False
                        left = False
                        up = True
                        right = False
                elif event.key == pygame.K_LEFT:
                    if not right:
                        down = False
                        left = True
                        up = False
                        right = False
                frame = False
    if right:
        if time.time() - move >= .1:
            snakex += 10
            move = time.time()
    elif left:
        if time.time() - move >= .1:
            snakex -= 10
            move = time.time()
    elif up:
        if time.time() - move >= .1:
            snakey -= 10
            move = time.time()
    elif down:
        if time.time() - move >= .1:
            snakey += 10
            move = time.time()
    if snakex == 610:
        snakex = 0
    if snakex == -10:
        snakex = 590
    if snakey == -10:
        snakey = 590
    if snakey == 610:
        snakey = 0
    if foodx == snakex and foody == snakey:
        foodx = (random.randint(0, 590) // 10) * 10
        foody = (random.randint(0, 590) // 10) * 10
        snake.append([snakex, snakey])
        score += 1
    clock.tick(5)
    snake.append([snakex, snakey])
    snake.pop(0)
    if len(snake) > 3:
        if snake[-1] in snake[:-2]:
            quit()
    show_text(f"{score}", 0, 0, white, 50)
    pygame.display.update()