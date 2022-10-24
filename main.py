import sys

import pygame

from custom import Sprite

# Insert the important global variables

FPS = 240
SPEED = 10
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 800)
FIGURE_SIZE = FIGURE_WIDTH, FIGURE_HEIGHT = (100, 100)
TEXT_COLOR = (27, 27, 27)
BACKGROUND_COLOR = (27, 207, 107)
CAPTION = 'Albert Einstein zur Zeit des dritten Reiches'

SCREEN_CENTER = SCREEN_CENTER_X, SCREEN_CENTER_Y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
EINSTEIN_POSITION = EINSTEIN_POS_X, EINSTEIN_POS_Y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def movement():
    global EINSTEIN_POS_X
    global EINSTEIN_POS_Y

    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and EINSTEIN_POS_X - SPEED > 0 + FIGURE_WIDTH / 2:
            EINSTEIN_POS_X -= SPEED
        elif keys[pygame.K_d] and EINSTEIN_POS_X + SPEED < SCREEN_WIDTH - FIGURE_WIDTH / 2:
            EINSTEIN_POS_X += SPEED

        if keys[pygame.K_w] and EINSTEIN_POS_Y - SPEED > 0 + FIGURE_HEIGHT / 2:
            EINSTEIN_POS_Y -= SPEED
        elif keys[pygame.K_s] and EINSTEIN_POS_Y + SPEED < SCREEN_HEIGHT - FIGURE_HEIGHT / 2:
            EINSTEIN_POS_Y += SPEED


def wait_until_space():
    running = True

    while running:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if eve.type == pygame.KEYDOWN and eve.key == pygame.K_SPACE:
                running = False


def draw_background_rect():
    pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))


def display_continue_text():
    screen.blit(continue_text,
                (SCREEN_CENTER_X - continue_text.get_width() / 2,
                 (SCREEN_CENTER_Y - continue_text.get_height() / 2) + 300))


def display_year(year):

    display_text = font.render('Jahr: ' + str(year), True, TEXT_COLOR)

    draw_background_rect()
    screen.blit(display_text,
                (SCREEN_CENTER_X - display_text.get_width() / 2, SCREEN_CENTER_Y - display_text.get_height() / 2))

    display_continue_text()
    pygame.display.update()
    wait_until_space()


# Init the Pygame Python library that is used for the UI

pygame.init()
fps_clock = pygame.time.Clock()

# Creation of the continue text

font = pygame.font.Font(pygame.font.get_default_font(), 36)
continue_text = font.render('Drücke LEERTASTE um fortzufahren:', True, TEXT_COLOR)

# Set the icon of the application

icon = pygame.image.load('images/Formel.png')
pygame.display.set_icon(icon)

# Create the Window that displays the Game

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(CAPTION)
screen.fill(BACKGROUND_COLOR)
pygame.display.flip()

# Display the number of the current Year

display_year(1922)

# Create the Sprite for Albert Einstein

einstein = Sprite('images/AlbertEinstein.png', FIGURE_SIZE)
einstein.figure.center = EINSTEIN_POSITION

# Einsteins letter to his little Sister

letter = Sprite('images/Letter.png', tuple(item // 1.5 for item in FIGURE_SIZE))
letter.figure.center = FIGURE_SIZE

running1 = True

while running1:

    movement()

    draw_background_rect()
    text = font.render('Brief an deine kleine Schwester!', True, TEXT_COLOR)

    einstein.figure.center = (EINSTEIN_POS_X, EINSTEIN_POS_Y)
    screen.blit(letter.image, letter.figure)
    screen.blit(einstein.image, einstein.figure)
    screen.blit(text, (SCREEN_CENTER_X - text.get_width() / 2, (SCREEN_CENTER_Y - text.get_height() / 2) + 300))
    pygame.display.update()

    if einstein.figure.colliderect(letter.figure):
        running1 = False

    fps_clock.tick()

draw_background_rect()
einstein.figure.center = SCREEN_CENTER

speach_image = pygame.image.load('images/Nachricht.png')
speach_sprite = speach_image.get_rect()
speach_sprite.center = (SCREEN_CENTER_X + 200, SCREEN_CENTER_Y - 125)

display_continue_text()
screen.blit(einstein.image, einstein.figure)
screen.blit(speach_image, speach_sprite)
pygame.display.update()

wait_until_space()

# Display the number of the current Year

display_year(1933)

# Display the Sprite for Adolf Hitler

hitler = Sprite('images/AdolfHitler.png', FIGURE_SIZE)
hitler.figure.center = SCREEN_CENTER

# GameLoop for the First Sequence

running2 = True

while running2:
    movement()

    draw_background_rect()

    einstein.figure.center = (EINSTEIN_POS_X, EINSTEIN_POS_Y)
    screen.blit(einstein.image, einstein.figure)
    screen.blit(hitler.image, hitler.figure)
    pygame.display.update()

    fps_clock.tick()

pygame.quit()
sys.exit(0)
