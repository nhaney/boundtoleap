import os

import pygame
from pygame.locals import *
import esper

from game import Game

RESOLUTION = 1280, 720

IMAGES = [os.path.join("resources", "images", "frog", "frogsprite.png")]


def run():
    """
    Runner that initializes pygame, handles scenes, and handles system events.
    """
    DEBUG_FONT = pygame.font.Font("resources/fonts/digital-7.ttf", 26)

    window = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("boundtoleap")
    clock = pygame.time.Clock()

    # Initialize Game (ECS world)
    game = Game(IMAGES, [])

    scene = 1

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if scene == 1:
            frame = game.update(delta=clock.tick(60)/1000.0)
            frame = pygame.transform.scale(frame, RESOLUTION)
            window.blit(frame, frame.get_rect())

        draw_fps(DEBUG_FONT, clock, window)

        # flip the framebuffers
        pygame.display.flip()


def draw_fps(font, clock, window):
    fps = str(int(clock.get_fps()))
    textsurface = font.render(fps, False, (255, 255, 255))
    window.blit(textsurface, (0, 0))


if __name__=='__main__':
    pygame.init()
    pygame.font.init()
    run()
    pygame.quit()
