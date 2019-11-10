import esper

from components import Position, Physics, Input, Path


class MovementProcessor(esper.Processor):
    def __init__(self):
        super().__init__()
        self.has_registered = False
        self.player_movement = None

    def process(self, *args, **kwargs):
        if not self.world:
            raise ValueError("Cannot process if system isn't registered.")
        if not self.has_registered:
            self.player_movement = PlayerMovementSubProcessor(self.world)
            self.has_registered = True

        self.player_movement.process(kwargs['delta'])


class PlayerMovementSubProcessor:
    def __init__(self, world):
        self.world = world

    def process(self, delta):
        ent, (pos, physics, _) = self.world.get_components(Position, Physics, Input)[0]
        pos.y += physics.gravity * delta


class PathMovementSubProcessor:
    def __init__(self, world):
        self.world = world

    def process(self, delta):
        pass

