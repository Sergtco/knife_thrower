import pygame
import sprites

GRAVITY = 0.05


class Object(pygame.sprite.Sprite):
    IN_AIR = False

    def __init__(self, pos=(0, 0)):
        super().__init__(sprites.object_group, sprites.all_sprites)
        self.speed = [0, 0]
        self.image = pygame.Surface((50, 70))
        self.image.fill('red')
        self.rect = self.image.get_rect().move(pos)
        self.acc = [0, GRAVITY]

    def update(self):
        if pygame.sprite.spritecollideany(self, sprites.horizontal_environment_group):
            self.speed[1] = 0
            self.acc[1] = 0
            self.IN_AIR = False
        else:
            self.IN_AIR = True
            self.acc[1] = GRAVITY
            self.speed[1] += self.acc[1]
            self.rect.y += self.speed[1]

        speed = self.speed[:]
        if pygame.sprite.spritecollide(self, sprites.vertical_environment_group, False):
            self.speed[0] = 0
            print(speed)
            if speed[0] > 0:
                self.rect.x -= 1
            elif speed[0] < 0:
                self.rect.x += 1

        else:
            self.speed[0] += self.acc[0]
            self.rect.x += self.speed[0]

