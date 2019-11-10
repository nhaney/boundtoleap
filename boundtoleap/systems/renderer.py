import esper
import pygame

from components import Position, Sprite


class RenderProcessor(esper.Processor):
    def __init__(self, window, clear_color=(255, 0, 0)):
        super().__init__()
        self.surface = window
        self.clear_color = clear_color

    def process(self, *args, **kwargs):
        # clear window
        self.surface.fill(self.clear_color)
        # breakpoint()
        for ent, (pos, sprite) in self.world.get_components(Position, Sprite):
            if sprite.base_image:
                self.surface.blit(sprite.base_image, (pos.x, pos.y, sprite.rect.width, sprite.rect.height))
            else:
                self.surface.fill((0, 255, 0), sprite.rect)
