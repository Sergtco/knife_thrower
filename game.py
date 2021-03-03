import pygame
import sprites
import live_objects
import environment
import weapons
import constants
import HUD


class Execute:
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    clock = pygame.time.Clock()
    fps = 300
    cross = HUD.Crosshair()
    pygame.mouse.set_visible(False)

    player = live_objects.Player((50, 200))
    player.weapon = weapons.Knife(player)
    floor = environment.Floor((0, constants.HEIGHT - 20), (constants.WIDTH, 20))
    second_floor = environment.Floor((constants.WIDTH - 150 - 700, 150), (700, 20))
    ceiling = environment.Floor((0, 0), (constants.WIDTH, 20))
    left_wall = environment.Wall((0, 0), (20, constants.HEIGHT))
    middle_wall = environment.Wall((constants.WIDTH - 150, 150), (20, constants.HEIGHT - 270))
    right_wall = environment.Wall((constants.WIDTH - 20, 0), (20, constants.HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                player.command()

            if event.type == pygame.MOUSEMOTION:
                cross.draw(event.pos)
                player.rotate_weapon(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(event.pos)

        screen.fill('black')

        sprites.all_sprites.update()
        sprites.all_sprites.draw(screen)

        clock.tick(fps)

        pygame.display.flip()