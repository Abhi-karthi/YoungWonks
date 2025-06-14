import pygame
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
pygame.display.set_caption("Space Invaders")
pygame.init()
ship_display = pygame.image.load("/Users/aaavi/Downloads/Spaceship_use.png")
enemy_display = pygame.image.load("/Users/aaavi/Downloads/enemy_spaceship_2.png")
ship_display = pygame.transform.flip(ship_display, False, True)
ship_display = pygame.transform.scale(ship_display, (50, 50))
enemy_display = pygame.transform.scale(enemy_display, (50, 46))
up = False
down = False
right = False
left = False
blasts = []


class Blast:
    def __init__(self, x: int, y: int, player: bool, moving=""):  # Use player attribute to check if the blast is from the player or from the enemy
        self.x = x
        self.y = y
        self.player = player
        self.moving = moving

    def get_hit_box(self):
        hit_box = pygame.Rect(self.x, self.y, 5, 16)
        return hit_box

    def get_color(self):
        if self.player:  # If the player shot it, the blast will be blue, else it will be orange
            color = (0, 207, 255)
        else:
            color = (255, 98, 0)
        return color

    def move(self):  # moving the blast
        self.y -= 4
        if self.player:
            if self.moving == "up":
                self.y -= 3
            elif self.moving == "down":
                self.y += 3
            elif self.moving == "right":
                self.x += 3
            elif self.moving == "left":
                self.x -= 3


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "right"
        self.change_direction_buffer = time.time()

    def change_direction(self):
        if time.time() - self.change_direction_buffer > .5:
            if self.direction == "left":
                if self.x <= 300:
                    self.y += 50
                    self.x += 35
                    self.direction = "right"
            if self.direction == "right":
                if self.x >= 500:
                    self.x -= 35
                    self.y += 50
                    self.direction = "left"
            self.change_direction_buffer = time.time()

    def get_hit_box(self):
        return pygame.Rect(self.x, self.y, 50, 46)

    def move(self):
        if self.direction == "right":
            self.x += 3
        if self.direction == "left":
            self.x -= 3


class Player:
    def __init__(self, x=300, y=450):
        self.x = x
        self.y = y
        self.up_time = time.time()
        self.down_time = time.time()
        self.right_time = time.time()
        self.left_time = time.time()

        self.up_time2 = time.time()
        self.down_time2 = time.time()
        self.right_time2 = time.time()
        self.left_time2 = time.time()

    def wrap(self):
        if self.x >= 800:
            self.x = -50
        elif self.x <= -50:
            self.x = 800

    def move(self, direction: str):  # lowercase right, left, up, or down
        if direction == "up":
            if self.y >= 0:
                if (time.time() - self.up_time) * 3 <= 3:
                    self.y -= (time.time() - self.up_time) * 3
                else:
                    self.y -= 3
        if direction == "down":
            if self.y <= 450:
                if (time.time() - self.down_time) * 3 <= 3:
                    self.y += (time.time() - self.down_time) * 3
                else:
                    self.y += 3
        if direction == "right":
            if self.x <= 700:
                if (time.time() - self.right_time) * 3 <= 3:
                    self.x += (time.time() - self.right_time) * 3
                else:
                    self.x += 3
        if direction == "left":
            if self.x >= 0:
                if (time.time() - self.left_time) * 3 <= 3:
                    self.x -= (time.time() - self.left_time) * 3
                else:
                    self.x -= 3


def show_text(msg, x, y, color, size):
    font_object = pygame.font.SysFont("Comic Sans", size)
    msgobj = font_object.render(msg, False, color)
    screen.blit(msgobj, (x, y))


enemy_ships = []
for i in range(5):
    enemy_ships.append(Enemy(i * 40, 0))
ship = Player()
shoot_buffer = time.time()
while True:
    screen.fill((0, 0, 0))
    for i in blasts:
        pygame.draw.rect(screen, i.get_color(), i.get_hit_box())
        i.move()
    for i in enemy_ships:
        screen.blit(enemy_display, (i.x, i.y))
        if 700 >= i.x >= 0:
            i.move()
        else:
            i.change_direction()
        for x in blasts:
            if i.get_hit_box().colliderect(x.get_hit_box()):
                blasts.remove(x)
                enemy_ships.remove(i)
# comment :) if you see this
    screen.blit(ship_display, (ship.x, ship.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
                ship.up_time = time.time()
            if event.key == pygame.K_DOWN:
                down = True
                ship.down_time = time.time()
            if event.key == pygame.K_RIGHT:
                right = True
                ship.right_time = time.time()
            if event.key == pygame.K_LEFT:
                left = True
                ship.left_time = time.time()
            if event.key == pygame.K_SPACE:
                if time.time() - shoot_buffer > .5:
                    if up:
                        blasts.append(Blast(ship.x + 12, ship.y, True, "up"))
                        blasts.append(Blast(ship.x + 35, ship.y, True, "up"))
                        ship.up_time = time.time()
                    elif down:
                        blasts.append(Blast(ship.x + 12, ship.y, True, "down"))
                        blasts.append(Blast(ship.x + 35, ship.y, True, "down"))
                        ship.down_time = time.time()
                    elif right:
                        blasts.append(Blast(ship.x + 12, ship.y, True, "right"))
                        blasts.append(Blast(ship.x + 35, ship.y, True, "right"))
                        ship.right_time = time.time()
                    elif left:
                        blasts.append(Blast(ship.x + 12, ship.y, True, "left"))
                        blasts.append(Blast(ship.x + 35, ship.y, True, "left"))
                        ship.left_time = time.time()
                    else:
                        blasts.append(Blast(ship.x + 12, ship.y, True, ""))
                        blasts.append(Blast(ship.x + 35, ship.y, True, ""))
                    shoot_buffer = time.time()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
                ship.up_time2 = time.time()
            if event.key == pygame.K_DOWN:
                down = False
                ship.down_time2 = time.time()
            if event.key == pygame.K_RIGHT:
                right = False
                ship.right_time2 = time.time()
            if event.key == pygame.K_LEFT:
                left = False
                ship.left_time2 = time.time()
    if up:
        ship.move("up")
    if down:
        ship.move("down")
    if right:
        ship.move("right")
    if left:
        ship.move("left")
    clock.tick(60)
    pygame.display.update()
