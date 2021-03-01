import pygame
import sprites
import math
import environment
import main

STUCK = []


class Weapon(pygame.sprite.Sprite):

    def __init__(self, wearer):
        super().__init__(sprites.all_sprites, sprites.weapon_group)
        self.wearer = wearer
        self.pos = self.wearer.rect.center
        self.damage = 20
        self.image = pygame.Surface((15, 20))
        self.image.fill('pink')
        self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])
        print(self.pos)


class Knife(Weapon):
    weapon_image = pygame.image.load('images/knife.png')

    def __init__(self, wearer):
        super().__init__(wearer)
        self.speed = [0 ,0]
        self.image = self.weapon_image
        self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])
        self.in_hands = True
        self.thrown = False

    def rotate(self, pos):
        if self.in_hands:
            mouse_x, mouse_y = pos
            x, y = self.pos
            rel_x, rel_y = mouse_x - x, mouse_y - y
            angle = (360 / math.pi) * -math.atan2(rel_y, rel_x)
            self.image = pygame.transform.rotate(self.weapon_image, int(angle))
            self.rect = self.image.get_rect()

    def throw(self, pos):
        self.in_hands = False
        self.throw_coords = pos

    def reload(self):
        STUCK.append(environment.StuckKnife(image=self.image, pos=(self.rect.x, self.rect.y)))
        self.in_hands = True
        self.thrown = False
        self.image = self.weapon_image
        self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])

    def update(self):
        if self.in_hands:
            x, y = self.wearer.rect.center
            self.rect = self.image.get_rect().move(x, y)

        if not self.in_hands and not self.thrown:
            m_x, m_y = self.throw_coords
            x, y = self.pos
            distance = [m_x - x, m_y - y]
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            direction = [distance[0] / norm, distance[1] / norm]
            bullet_vector = [direction[0] * math.sqrt(2), direction[1] * math.sqrt(2)]
            self.speed = [int(i * 5) for i in bullet_vector]
            self.thrown = True

        if not self.in_hands and self.thrown:
            if pygame.sprite.spritecollide(self, sprites.vertical_environment_group, False):
                self.speed = [0, 0]
                self.reload()
            elif pygame.sprite.spritecollide(self, sprites.horizontal_environment_group, False):
                self.speed = [0, 0]
                self.reload()
            elif self.rect.x > main.WIDTH or 0 > self.rect.y > 720:
                self.in_hands = True
                self.thrown = False
                self.image = self.weapon_image
                self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])

            else:
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
            print(self.speed)
