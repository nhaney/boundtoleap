
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
    # Initialize Pygame stuff
    pygame.init()
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
            game.update(delta=clock.tick(200)/1000.0)

if __name__=='__main__':
    run()
    pygame.quit()
