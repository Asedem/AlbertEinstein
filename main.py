import pygame

# Insert the important global variables

SPEED = 10
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 800)
FIGURE_SIZE = FIGURE_WIDTH, FIGURE_HEIGHT = (100, 100)
TEXT_COLOR = (27, 27, 27)
BACKGROUND_COLOR = (27, 207, 107)
CAPTION = 'Albert Einstein zur Zeit des dritten Reiches'

EINSTEIN_POSITION = EINSTEIN_POS_X, EINSTEIN_POS_Y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Init the Pygame Python library that is used for the UI

pygame.init()

# Create the Window that displays the Game

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(CAPTION)
screen.fill(BACKGROUND_COLOR)
pygame.display.flip()

# Display the number of the current Year

font = pygame.font.Font(pygame.font.get_default_font(), 36)

text = font.render('Jahr: 1922', True, TEXT_COLOR)
screen.blit(text, (EINSTEIN_POS_X - text.get_width() / 2, EINSTEIN_POS_Y - text.get_height() / 2))

continue_text = font.render('Drücke LEHRTASTE um fortzufahren:', True, TEXT_COLOR)
screen.blit(continue_text, (EINSTEIN_POS_X - continue_text.get_width() / 2, (EINSTEIN_POS_Y - continue_text.get_height() / 2) + 300))

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False

# Create the Sprite for Albert Einstein

einstein_image = pygame.transform.scale(pygame.image.load('images/AlbertEinstein.png'), FIGURE_SIZE)
einstein_sprite = einstein_image.get_rect()
einstein_sprite.center = EINSTEIN_POSITION

# Einsteins letter to his little Sister

letter_image = pygame.transform.scale(pygame.image.load('images/Letter.png'), tuple(item // 2 for item in FIGURE_SIZE))
letter_sprite = letter_image.get_rect()
letter_sprite.center = FIGURE_SIZE

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            EINSTEIN_POS_X -= SPEED
        elif keys[pygame.K_d]:
            EINSTEIN_POS_X += SPEED

        if keys[pygame.K_w]:
            EINSTEIN_POS_Y -= SPEED
        elif keys[pygame.K_s]:
            EINSTEIN_POS_Y += SPEED

    pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    einstein_sprite.center = (EINSTEIN_POS_X, EINSTEIN_POS_Y)
    screen.blit(letter_image, letter_sprite)
    screen.blit(einstein_image, einstein_sprite)
    pygame.display.update()

    if pygame.Rect.collidedict(letter_sprite, einstein_sprite):
        running = False

pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
text = font.render('Drücke LEHRTASTE um fortzufahren:', True, TEXT_COLOR)

speach_image = pygame.image.load('images/Nachricht.png')
speach_sprite = speach_image.get_rect()
speach_sprite.center = (EINSTEIN_POS_X + 200, EINSTEIN_POS_Y - 125)

screen.blit(continue_text, (EINSTEIN_POS_X - text.get_width() / 2, (EINSTEIN_POS_Y - text.get_height() / 2) + 300))
screen.blit(einstein_image, einstein_sprite)
screen.blit(speach_image, speach_sprite)
pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False

# Display the Sprite for Adolf Hitler

hitler_image = pygame.transform.scale(pygame.image.load('images/AdolfHitler.png'), FIGURE_SIZE)
hitler_sprite = hitler_image.get_rect()
hitler_sprite.center = EINSTEIN_POSITION

# GameLoop for the First Sequence

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            EINSTEIN_POS_X -= SPEED
        elif keys[pygame.K_d]:
            EINSTEIN_POS_X += SPEED

        if keys[pygame.K_w]:
            EINSTEIN_POS_Y -= SPEED
        elif keys[pygame.K_s]:
            EINSTEIN_POS_Y += SPEED

    pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    einstein_sprite.center = (EINSTEIN_POS_X, EINSTEIN_POS_Y)
    screen.blit(einstein_image, einstein_sprite)
    screen.blit(hitler_image, hitler_sprite)
    pygame.display.update()

pygame.quit()
