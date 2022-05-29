import pygame
from player import Player

pygame.init()
X = 600
Y = 800
FPS = 60
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Animations")


def game_loop():
    player = Player()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill((0, 0, 0))
        player.update()
        display_surface.blit(player.image, player.rect)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    game_loop()
