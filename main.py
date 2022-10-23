import pygame

SPEED = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = (27, 207, 107)
CAPTION = 'Albert Einstein zur Zeit des dritten Reiches'

CHARACTER_POSITION = CHARACTER_POS_X, CHARACTER_POS_Y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
screen.fill(BACKGROUND_COLOR)
pygame.display.flip()

character_image = pygame.image.load('images/AlberEinstein.png')
character_image = pygame.transform.scale(character_image, (100, 100))
character_sprite = character_image.get_rect()
character_sprite.center = CHARACTER_POSITION

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            CHARACTER_POS_X -= SPEED
        elif keys[pygame.K_d]:
            CHARACTER_POS_X += SPEED

        if keys[pygame.K_w]:
            CHARACTER_POS_Y -= SPEED
        elif keys[pygame.K_s]:
            CHARACTER_POS_Y += SPEED

    pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    character_sprite.center = (CHARACTER_POS_X, CHARACTER_POS_Y)
    screen.blit(character_image, character_sprite)
    pygame.display.update()

pygame.quit()
