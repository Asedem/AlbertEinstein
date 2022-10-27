#!/usr/bin/env python3

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

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and EINSTEIN_POS_X - SPEED > 0 + FIGURE_WIDTH / 2:
            EINSTEIN_POS_X -= SPEED
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and EINSTEIN_POS_X + SPEED < SCREEN_WIDTH - FIGURE_WIDTH / 2:
            EINSTEIN_POS_X += SPEED

        if (keys[pygame.K_w] or keys[pygame.K_UP]) and EINSTEIN_POS_Y - SPEED > 0 + FIGURE_HEIGHT / 2:
            EINSTEIN_POS_Y -= SPEED
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and EINSTEIN_POS_Y + SPEED < SCREEN_HEIGHT - FIGURE_HEIGHT / 2:
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


def display_text(text_to_display):

    display_text = font.render(str(text_to_display), True, TEXT_COLOR)

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

text = font.render('Brief an deine kleine Schwester!', True, TEXT_COLOR)

running1 = True

while running1:

    movement()

    draw_background_rect()

    einstein.figure.center = (EINSTEIN_POS_X, EINSTEIN_POS_Y)
    screen.blit(letter.image, letter.figure)
    screen.blit(einstein.image, einstein.figure)
    screen.blit(text, (SCREEN_CENTER_X - text.get_width() / 2, (SCREEN_CENTER_Y - text.get_height() / 2) + 300))
    pygame.display.update()

    if einstein.figure.colliderect(letter.figure):
        running1 = False

    fps_clock.tick()

draw_background_rect()

written_letter = Sprite('images/LetterWritten.png', (600, 600))
written_letter.figure.center = (SCREEN_CENTER_X, SCREEN_CENTER_Y - FIGURE_HEIGHT / 2)
screen.blit(written_letter.image, written_letter.figure)

display_continue_text()
pygame.display.update()

wait_until_space()

# Display the number of the current Year

display_year(1933)

# Display the Sprite for Adolf Hitler

hitler = Sprite('images/AdolfHitler.png', FIGURE_SIZE)
hitler.figure.center = SCREEN_CENTER

# GameLoop for the flee Sequence

text = font.render('Wandere in die USA aus!', True, TEXT_COLOR)
kross_flag = Sprite('images/KreuzFlagge.png', FIGURE_SIZE)
usa_flag = Sprite('images/USAFlagge.png', FIGURE_SIZE)

stones = []
for i in range(0, 4):
    stones.append(Sprite('images/Stone.png', tuple(item // 1.4 for item in FIGURE_SIZE)))

kross_flag.figure.center = FIGURE_SIZE
usa_flag.figure.center = tuple(item - FIGURE_HEIGHT for item in SCREEN_SIZE)

EINSTEIN_POS_X = FIGURE_WIDTH * 2
EINSTEIN_POS_Y = FIGURE_HEIGHT

running2 = True
hitler_pos_x = 0 - FIGURE_WIDTH / 2

while running2:

    if einstein.figure.colliderect(hitler.figure) or einstein.figure.colliderect(kross_flag.figure):
        EINSTEIN_POS_X = FIGURE_WIDTH * 2
        EINSTEIN_POS_Y = FIGURE_HEIGHT

    for stone in stones:
        if einstein.figure.colliderect(stone.figure):
            EINSTEIN_POS_X = FIGURE_WIDTH * 2
            EINSTEIN_POS_Y = FIGURE_HEIGHT

    movement()

    draw_background_rect()

    hitler_pos_x += 0.2
    if hitler_pos_x > SCREEN_WIDTH + FIGURE_WIDTH // 2:
        hitler_pos_x = 0 - FIGURE_WIDTH // 2

    einstein.figure.center = (EINSTEIN_POS_X, EINSTEIN_POS_Y)
    screen.blit(kross_flag.image, kross_flag.figure)
    screen.blit(usa_flag.image, usa_flag.figure)
    screen.blit(einstein.image, einstein.figure)
    screen.blit(text, (SCREEN_CENTER_X - text.get_width() / 2, (SCREEN_CENTER_Y - text.get_height() / 2) + 300))

    hitler.figure.center = (hitler_pos_x, SCREEN_CENTER_Y)
    screen.blit(hitler.image, hitler.figure)

    stones[1].figure.center = (FIGURE_WIDTH, SCREEN_HEIGHT / 3)
    screen.blit(stones[1].image, stones[1].figure)
    stones[2].figure.center = (SCREEN_WIDTH - FIGURE_WIDTH, SCREEN_HEIGHT / 2.6)
    screen.blit(stones[2].image, stones[2].figure)
    stones[3].figure.center = (SCREEN_WIDTH / 2, FIGURE_HEIGHT)
    screen.blit(stones[3].image, stones[3].figure)
    stones[0].figure.center = (SCREEN_WIDTH / 2.8, SCREEN_HEIGHT - FIGURE_HEIGHT * 2)
    screen.blit(stones[0].image, stones[0].figure)

    pygame.display.update()

    if einstein.figure.colliderect(usa_flag.figure):
        running2 = False

    fps_clock.tick()

# Display cut text

draw_background_rect()

text_1933 = Sprite('images/1933.png', (600, 600))
text_1933.figure.center = SCREEN_CENTER
screen.blit(text_1933.image, text_1933.figure)

display_continue_text()
pygame.display.update()

wait_until_space()

# Display the number of the current Year

display_year(1939)

# Display 2nd cut text

draw_background_rect()

text_1939 = Sprite('images/1939.png', (600, 600))
text_1939.figure.center = SCREEN_CENTER
screen.blit(text_1939.image, text_1939.figure)

display_continue_text()
pygame.display.update()

wait_until_space()

# GameLoop for the constructing Sequence

text = font.render('Konstruiere die Atombombe!', True, TEXT_COLOR)
atombombe1 = Sprite('images/Atombombe1.png', FIGURE_SIZE)
atombombe2 = Sprite('images/Atombombe2.png', FIGURE_SIZE)
atombombe3 = Sprite('images/Atombombe3.png', FIGURE_SIZE)

atombombe1.figure.center = (FIGURE_WIDTH, SCREEN_HEIGHT / 3)
atombombe2.figure.center = (SCREEN_WIDTH - FIGURE_WIDTH, SCREEN_HEIGHT / 2.6)
atombombe3.figure.center = (SCREEN_WIDTH / 2, FIGURE_HEIGHT)

EINSTEIN_POS_X = SCREEN_CENTER_X
EINSTEIN_POS_Y = SCREEN_CENTER_Y

collected1 = False
collected2 = False
collected3 = False

running3 = True

while running3:

    movement()

    draw_background_rect()
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH - FIGURE_WIDTH, 0, FIGURE_WIDTH, FIGURE_HEIGHT))

    einstein.figure.center = (EINSTEIN_POS_X, EINSTEIN_POS_Y)
    screen.blit(einstein.image, einstein.figure)
    screen.blit(text, (SCREEN_CENTER_X - text.get_width() / 2, (SCREEN_CENTER_Y - text.get_height() / 2) + 300))

    if einstein.figure.colliderect(atombombe1.figure):
        collected1 = True
        atombombe1.figure.center = (SCREEN_WIDTH - FIGURE_WIDTH / 2, FIGURE_HEIGHT / 2)
    elif einstein.figure.colliderect(atombombe2.figure):
        collected2 = True
        atombombe2.figure.center = (SCREEN_WIDTH - FIGURE_WIDTH / 2, FIGURE_HEIGHT / 2)
    elif einstein.figure.colliderect(atombombe3.figure):
        collected3 = True
        atombombe3.figure.center = (SCREEN_WIDTH - FIGURE_WIDTH / 2, FIGURE_HEIGHT / 2)

    screen.blit(atombombe1.image, atombombe1.figure)
    screen.blit(atombombe2.image, atombombe2.figure)
    screen.blit(atombombe3.image, atombombe3.figure)

    pygame.display.update()

    if collected1 and collected2 and collected3:
        running3 = False

    fps_clock.tick()

pygame.draw.rect(screen, BACKGROUND_COLOR, (0, SCREEN_HEIGHT - SCREEN_WIDTH // 4, SCREEN_WIDTH, SCREEN_WIDTH // 4))

display_continue_text()
pygame.display.update()

wait_until_space()

display_year(1945)

hiroshima = Sprite('images/Hiroshima.png', SCREEN_SIZE)
hiroshima.figure.center = SCREEN_CENTER
atombombe = Sprite('images/Atombombe.png', FIGURE_SIZE)
atombombe.figure.center = SCREEN_CENTER
atompilz = Sprite('images/Atompilz.png', FIGURE_SIZE)
atompilz.figure.center = (SCREEN_CENTER_X, SCREEN_CENTER_Y - FIGURE_HEIGHT / 2)

draw_background_rect()
screen.blit(hiroshima.image, hiroshima.figure)
display_continue_text()
pygame.display.update()

wait_until_space()

draw_background_rect()
screen.blit(hiroshima.image, hiroshima.figure)
screen.blit(atombombe.image, atombombe.figure)
display_continue_text()
pygame.display.update()

wait_until_space()

draw_background_rect()
screen.blit(hiroshima.image, hiroshima.figure)
screen.blit(atombombe.image, atombombe.figure)
screen.blit(atompilz.image, atompilz.figure)
display_continue_text()
pygame.display.update()

wait_until_space()

# Display 3rd cut text

draw_background_rect()

text_1945 = Sprite('images/1945.png', (600, 600))
text_1945.figure.center = SCREEN_CENTER
screen.blit(text_1945.image, text_1945.figure)

display_continue_text()
pygame.display.update()

wait_until_space()

# display the end text

display_text('Ende')

# Display the end picture

end = Sprite('images/Zitat.png', SCREEN_SIZE)
end.figure.center = SCREEN_CENTER

running4 = True

while running4:

    screen.blit(end.image, end.figure)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running4 = False

pygame.quit()
sys.exit(0)
