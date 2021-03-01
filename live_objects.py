import pygame
import objects
import sprites


class LiveObject(objects.Object):
    def __init__(self, pos, hp=100):
        super().__init__(pos)
        self.image.fill('yellow')
        self.hp = hp

    def move(self, speed, delta_acc=None):
        pass


class Player(LiveObject):
    object_image = pygame.image.load('images/player.png')

    def __init__(self, pos, hp=100):
        super().__init__(pos, hp)
        self.image = self.object_image
        self.rect = self.image.get_rect().move(pos)
        self.d_press = False
        self.a_press = False

    def move(self, speed, delta_acc=None):
        if delta_acc is None:
            delta_acc = [0, 0]
        self.speed[0] = speed[0]
        self.speed[1] += speed[1]
        print(self.rect.x, self.rect.y)

    def command(self):
        pressed_keys = pygame.key.get_pressed()

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
            if not self.IN_AIR:
                self.rect.y -= 10
                self.move([0, -3])





