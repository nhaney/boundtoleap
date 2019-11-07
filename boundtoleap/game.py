import pygame
from pygame.locals import *
import esper

from boundtoleap.components import *
from boundtoleap.systems import *

RESOLUTION = 720, 480

player_img = pygame.image.load('boundtoleap/resources/frogsprite.png')


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
    world.add_processor(MovementProcessor(0, 720, 0, 450))
    world.add_processor(RenderProcessor(window))

    running = True
    p_t = pygame.time.get_ticks()

    while running:
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        delta = (t - p_t) / 1000.0
        p_t = t

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # A single call to world.process() will update all Processors:
        world.process(delta=delta)


run()
pygame.quit()
