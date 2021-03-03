import pygame
import sprites
import math
import environment
import constants

STUCK = []


class Weapon(pygame.sprite.Sprite):
    weapon_image = pygame.Surface((25, 5))
    weapon_image.fill('pink')

    def __init__(self, wearer):
        super().__init__(sprites.all_sprites, sprites.weapon_group)
        self.wearer = wearer
        self.pos = self.wearer.rect.center
        self.damage = 20
        self.image = self.weapon_image
        self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])
        self.in_hands = True

    def rotate(self, pos):
        if self.in_hands:
            mouse_x, mouse_y = pos
            x, y = self.pos
            rel_x, rel_y = mouse_x - x, mouse_y - y
            angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            self.image = pygame.transform.rotate(self.weapon_image, int(angle))
            self.rect = self.image.get_rect()


class Knife(Weapon):
    weapon_image = pygame.image.load('images/knife.png')

    def __init__(self, wearer):
        super().__init__(wearer)
        self.speed = [0, 0]
        self.image = self.weapon_image
        self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])
        self.throw_coords = None

        self.thrown = False

    def throw(self, m_pos):
        self.in_hands = False
        self.throw_coords = m_pos

    def reload(self, stuck=False):
        if stuck:
            STUCK.append(environment.StuckKnife(image=self.image, pos=(self.rect.x, self.rect.y)))
        self.in_hands = True
        self.thrown = False
        self.image = self.weapon_image
        self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])

    def update(self):
        x, y = self.wearer.rect.center
        if self.in_hands:
            self.rect = self.image.get_rect().move(x, y)

        if not self.in_hands and not self.thrown:
            m_x, m_y = self.throw_coords
            distance = [m_x - x, m_y - y]
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1] / norm]
            bullet_vector = [direction[0] * math.sqrt(2), direction[1] * math.sqrt(2)]
            self.speed = [int(i * 50) / 8 for i in bullet_vector]
            self.thrown = True

        if not self.in_hands and self.thrown:
            if pygame.sprite.spritecollide(self, sprites.vertical_environment_group, False):
                self.speed = [0, 0]
                self.reload(True)
            elif pygame.sprite.spritecollide(self, sprites.horizontal_environment_group, False):
                self.speed = [0, 0]
                self.reload(True)
            elif self.rect.x > constants.WIDTH or self.rect.x < 0 or self.rect.y > constants.HEIGHT or self.rect.y < 0:
                self.reload()

            else:
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
