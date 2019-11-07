import esper
import pygame

from boundtoleap.components.components import Position, Renderable


class RenderProcessor(esper.Processor):
    def __init__(self, window, clock, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clock = clock
        self.clear_color = clear_color
        pygame.font.init()
        self.fps_font = pygame.font.Font("boundtoleap/resources/fonts/digital-7.ttf", 26)

    def process(self, *args, **kwargs):
        # clear window
        self.window.fill(self.clear_color)

        for ent, (pos, render) in self.world.get_components(Position, Renderable):
            self.window.blit(render.img, (pos.x, pos.y))

        self.draw_fps()
        # flip the framebuffers
        pygame.display.flip()

    def render_circle(self, pos, render, shape):
        pygame.draw.circle(self.window, render.color, (pos.x, pos.y), shape.radius)

    def render_rect(self, pos, render, shape):
        pygame.draw.rect(self.window, render.color, (pos.x, pos.y, shape.rect.width, shape.rect.height))

    def draw_fps(self):
        fps = str(int(self.clock.get_fps()))
        textsurface = self.fps_font.render(fps, False, (255, 255, 255))
        self.window.blit(textsurface, (0, 0))
