import pygame
import sprites


class Construct(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(50, 50), color='pink'):
        super().__init__(sprites.all_sprites)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect().move(pos)


class Floor(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(500, 10), color='green'):
        super().__init__(sprites.all_sprites, sprites.horizontal_environment_group)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect().move(pos)


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(10, 500), color='blue'):
        super().__init__(sprites.all_sprites, sprites.vertical_environment_group)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect().move(pos)


class StuckKnife(Floor):
    def __init__(self, image, pos=(0, 0), size=(500, 10), color='green'):
        super().__init__(pos, size, color)
        self.image = image
        self.rect = self.image.get_rect().move(pos)
