import pygame
import sprites


class Crosshair(pygame.sprite.Sprite):
    cross_image = pygame.image.load('images/crosshair.png')

    def __init__(self):
        super().__init__(sprites.all_sprites)
        self.image = self.cross_image
        self.rect = self.image.get_rect()

    def draw(self, pos):
        self.rect = self.image.get_rect()
        self.rect.center = pos
