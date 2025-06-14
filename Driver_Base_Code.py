import RPi.GPIO as GPIO
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Driving Base")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

f = False
r = False
l = False
d = False

TRIG_PIN = 11
ECHO_PIN = 5
buffer1 = time.time
buffer2 = time.time


class Ultrasonic:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        self.start = 0
        self.stop = 0
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def get_distance(self):
        # d = s * t

        speed = 34300
        GPIO.output(self.trig, 1)
        time.sleep(.001)
        GPIO.output(self.trig, 0)
        while GPIO.input(self.echo) == 0:
            self.start = time.time()
        print("start")
        while GPIO.input(self.echo) == 1:
            self.stop = time.time()
        print("stop")
        duration = self.stop - self.start
        if (speed * duration) / 2 <= 100:
            return (speed * duration) / 2
        else:
            return 999


f_left = Ultrasonic(13, 11)
f_right = Ultrasonic(7, 5)
back = Ultrasonic(19, 21)


def forward():
    GPIO.output(38, 1)
    GPIO.output(40, 0)
    GPIO.output(29, 1)
    GPIO.output(31, 0)


def backward():
    GPIO.output(38, 0)
    GPIO.output(40, 1)
    GPIO.output(29, 0)
    GPIO.output(31, 1)


def left():
    GPIO.output(38, 0)
    GPIO.output(40, 0)
    GPIO.output(29, 1)
    GPIO.output(31, 0)


def right():
    GPIO.output(38, 1)
    GPIO.output(40, 0)
    GPIO.output(29, 0)
    GPIO.output(31, 0)


def stop():
    GPIO.output(38, 0)
    GPIO.output(40, 0)
    GPIO.output(29, 0)
    GPIO.output(31, 0)


clock = pygame.time.Clock()
while True:
    # print(get_distance())
    # print("HI")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GPIO.cleanup()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                f = True
            elif event.key == pygame.K_RIGHT:
                r = True
            elif event.key == pygame.K_LEFT:
                l = True
            elif event.key == pygame.K_DOWN:
                d = True
            # elif event.key == pygame.K_SPACE:
            # GPIO.output(38, 0)
            # GPIO.output(40, 0)
            # GPIO.output(29, 0)
            # GPIO.output(31, 0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                f = False
            if event.key == pygame.K_RIGHT:
                r = False
            if event.key == pygame.K_LEFT:
                l = False
            if event.key == pygame.K_DOWN:
                d = False

    if f:
        if f_right.get_distance() > 15 and f_left.get_distance() > 15:
            forward()
            print("forward")
    elif r:
        if f_right.get_distance() > 15:
            right()
    elif l:
        if f_left.get_distance() > 15:
            left()
    elif d:
        if back.get_distance() > 15:
            backward()
    else:
        stop()

    clock.tick(60)
    pygame.display.update()
