import pygame
import sprites
import live_objects
import environment
import weapons
import main


class Execute:
    screen = pygame.display.set_mode((main.WIDTH, main.HEIGHT))
    screen.fill('black')

    clock = pygame.time.Clock()
    fps = 300

    player = live_objects.Player((50, 200))
    knife = weapons.Knife(player)
    floor = environment.Floor((0, 400), (1000, 30))
    wall = environment.Wall((1000, 0), (20, 400))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                player.command()

            if event.type == pygame.MOUSEMOTION:
                knife.rotate(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                knife.throw(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill('black')

        sprites.all_sprites.update()
        sprites.all_sprites.draw(screen)

        clock.tick(fps)

        pygame.display.flip()