import pygame
import objects
import sprites


class LiveObject(objects.Object):
    def __init__(self, pos, hp=100, weapon=None):
        super().__init__(pos)
        self.image.fill('yellow')
        self.hp = hp
        self.armory = []
        if weapon:
            self.weapon = weapon

    def move(self, speed, delta_acc=None):
        pass


class Player(LiveObject):
    object_image = pygame.image.load('images/player.png')

    def __init__(self, pos, hp=100, weapon=None):
        super().__init__(pos, hp, weapon)
        self.image = self.object_image
        self.rect = self.image.get_rect().move(pos)

        self.d_press = False
        self.a_press = False

    def move(self, speed, delta_acc=None):
        if delta_acc is None:
            delta_acc = [0, 0]
        self.speed[0] = speed[0]
        self.speed[1] += speed[1]

    def command(self):
        pressed_keys = pygame.key.get_pressed()
        pressed_mouse = pygame.mouse.get_pressed(num_buttons=3)
        m_pos = pygame.mouse.get_pos()

        if self.weapon:
            self.weapon.rotate(m_pos)

            if pressed_mouse[0]:
                self.weapon.throw(m_pos)

        if pressed_keys[pygame.K_u] and pygame.sprite.spritecollideany(self, sprites.all_sprites):
            self.rect.x += 10
            self.rect.y -= 10

        if pressed_keys[pygame.K_d] and not self.d_press:
            self.move([1, 0])
            self.d_press = True

        if not pressed_keys[pygame.K_d] and self.d_press:
            self.move([0, 0], [0.1, 0])
            self.d_press = False

        if pressed_keys[pygame.K_a] and not self.a_press:
            self.move([-1, 0])
            self.a_press = True

        if not pressed_keys[pygame.K_a] and self.a_press:
            self.move([0, 0], [-0.1, 0])
            self.a_press = False

        if pressed_keys[pygame.K_SPACE]:
            if pressed_keys[pygame.K_d]:
                if not self.IN_AIR:
                    self.rect.y -= 10
                    self.move([1, -3])
            elif pressed_keys[pygame.K_a]:
                if not self.IN_AIR:
                    self.rect.y -= 10
                    self.move([-1, -3])
            else:
                if not self.IN_AIR:
                    self.rect.y -= 10
                    self.move([0, -3])






