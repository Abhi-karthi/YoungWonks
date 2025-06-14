import pygame
import random
import time
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
grey = (127, 127, 127)
black = (0, 0, 0)
clock = pygame.time.Clock()
colors = [white, red, green, blue, purple]
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Pong")
pygame.init()


def show_text(msg, x, y, color, size):
    font_object = pygame.font.SysFont("Comic Sans", size)
    msgobj = font_object.render(msg, False, color)
    screen.blit(msgobj, (x, y))


game_mode = "hard"


class Ball:
    global game_mode
    score_l = 0
    score_r = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        self.speedx = random.randint(1, 3)
        self.speedy = random.randint(1, 3)
        if a == 1:
            self.speedx *= -1
        if b == 1:
            self.speedy *= -1
        self.radius = 25
        self.visible = True

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

    def bounce(self, up: bool):
        if game_mode == "normal":
            if self.speedx > 0:
                self.speedx += 1
            else:
                self.speedx -= 1
            if self.speedy > 0:
                self.speedy += 1
            else:
                self.speedy -= 2
        elif game_mode == "hard":
            if self.speedx > 0:
                self.speedx += 2
            else:
                self.speedx -= 2
            if self.speedy > 0:
                self.speedy += 2
            else:
                self.speedy -= 2
        if up:
            self.speedy *= -1
        self.speedx *= -1

    def hit_wall(self):
        if self.x >= 775:
            score_l = True
        if self.x <= -25:
            score_r = True
        if self.y <= 25 or self.y >= 475:
            self.speedy *= -1

    def blink(self):
        ball.x = 375
        ball.y = 250
        for i in range(5):
            self.visible = False
            time.sleep(.2)
            self.visible = True
            time.sleep(.2)


class Paddle:
    def __init__(self, x):
        self.x = x
        self.y = 210
        self.score = 0

    def up(self):
        if self.y >= 0:
            self.y -= 5

    def down(self):
        if self.y <= 420:
            self.y += 5


p1 = Paddle(0)
p2 = Paddle(740)
ball = Ball(375, 250)
left_u = False
left_d = False
right_u = False
right_d = False
p1_hit_box = 0
p2_hit_box = 0
ball_hit_box = 0
prev_score_r = ball.score_r
prev_score_l = ball.score_l
buffer = False
while True:
    screen.fill((0, 0, 0))
    if ball.score_r > prev_score_r or ball.score_l > prev_score_l:
        prev_score_r = ball.score_r
        prev_score_l = ball.score_l
        ball.blink()

    pygame.draw.rect(screen, white, (p1.x, p1.y, 10, 80), 2)
    pygame.draw.rect(screen, white, (p2.x, p2.y, 10, 80), 2)
    p1_hit_box = pygame.Rect(pygame.draw.rect(screen, white, (p1.x, p1.y, 10, 80), 2))
    p2_hit_box = pygame.Rect(pygame.draw.rect(screen, white, (p2.x, p2.y, 10, 80), 2))
    pygame.draw.circle(screen, white, (ball.x, ball.y), ball.radius, 2)
    ball_hit_box = pygame.Rect(pygame.draw.circle(screen, white, (ball.x, ball.y), ball.radius, 5))
    ball.update()
    ball.hit_wall()
    if ball_hit_box.colliderect(p1_hit_box) or ball_hit_box.colliderect(p2_hit_box):
        if not buffer:
            if 25 <= ball.x <= 725:
                ball.bounce(False)
            else:
                ball.bounce(True)
            buffer = True

    else:
        buffer = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_u = True
            elif event.key == pygame.K_s:
                left_d = True
            if event.key == pygame.K_UP:
                right_u = True
            elif event.key == pygame.K_DOWN:
                right_d = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_u = False
            if event.key == pygame.K_s:
                left_d = False
            if event.key == pygame.K_UP:
                right_u = False
            if event.key == pygame.K_DOWN:
                right_d = False
    if left_u:
        p1.up()
    if left_d:
        p1.down()
    if right_u:
        p2.up()
    if right_d:
        p2.down()
    clock.tick(60)
    pygame.display.update()
