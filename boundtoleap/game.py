import pygame
from pygame.locals import *
import esper

from boundtoleap.components import *
from boundtoleap.systems import *

RESOLUTION = 1280, 720

player_img = pygame.image.load("boundtoleap/resources/images/frog/frogsprite.png")


def run():
    # Initialize Pygame stuff
    pygame.init()

    window = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("boundtoleap")
    clock = pygame.time.Clock()

    # Initialize Esper world, and create a "player" Entity with a few Components.
    world = esper.World()
    player = world.create_entity(
        Velocity(),
        Position(100, 100),
        Shape(0, rect=pygame.Rect((360, 450), (100, 20))),
        Renderable(player_img, window),
        Input()
    )
    world.add_processor(InputProcessor(player))
    world.add_processor(MovementProcessor(0, 1280, 0, 720))
    world.add_processor(RenderProcessor(window, clock))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # A single call to world.process() will update all Processors:
        world.process(delta=clock.tick(200)/1000.0)


run()
pygame.quit()
