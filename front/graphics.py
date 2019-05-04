import pygame
import numpy as np

pygame.init()


def main():
    screen = pygame.display.set_mode((400, 400))

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()


if __name__ == '__main__':
    main()
