import pygame


class Sprite:

    def __init__(self, filename, size):
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.figure = self.image.get_rect()
