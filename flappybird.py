
import random
import serial
import sys
import pgzrun
from threading import Thread

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

# These constants control the difficulty of the game
GAP = 200
GRAVITY = 0.25
FLAP_STRENGTH = 5.5
SPEED = 1.5

is_shaking = False

bird = Actor('bird1', (75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

pipe_top = Actor('top', anchor=('left', 'bottom'), pos=(-100, 0))
pipe_bottom = Actor('bottom', anchor=('left', 'top'), pos=(-100, 0))


def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)


def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        bird.score += 1


def update_bird():
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y += (uy + bird.vy) / 2
    bird.x = 75

    if not bird.dead:
        if bird.vy < -3:
            bird.image = 'bird2'
        else:
            bird.image = 'bird1'

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'birddead'

    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.score = 0
        bird.vy = 0
        reset_pipes()


def update():
   update_pipes()
   update_bird()
   global is_shaking
   if is_shaking and not bird.dead:
        bird.vy = -FLAP_STRENGTH
        is_shaking = False

def on_key_down():
    if not bird.dead:
        bird.vy = -FLAP_STRENGTH


def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(
        str(bird.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )

def leitura_serial():
    PORTA = sys.argv[1]
    global is_shaking
    with serial.Serial(PORTA, 115200) as porta:
            while True:
                line = porta.readline().decode('UTF8').strip()
                if line == "shake":
                    is_shaking = True

thread = Thread(target=leitura_serial)
thread.start()
pgzrun.go()
    