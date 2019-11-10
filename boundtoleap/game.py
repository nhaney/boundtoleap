import pygame as pg
import esper

from components import (
    Collider, Input, Position, Sprite, Physics
)

from systems import (
    MovementProcessor, RenderProcessor
)


DEBUG = True

FRAME_SIZE = 640, 360


class Game(esper.World):
    """
    Handles all gameplay logic
    """
    def __init__(self, images, sounds):
        super().__init__()
        # load resources
        self.images = []
        self.load_resources(images, sounds)
        # screen size initialization
        self.width = FRAME_SIZE[0]
        self.height = FRAME_SIZE[1]
        # start game (will go somewhere else later)
        self.start()
        # register systems
        self.add_processor(MovementProcessor())
        # surface that is reused for each frame
        self.surface = pg.Surface(FRAME_SIZE)
        self.add_processor(RenderProcessor(self.surface))

    def load_resources(self, images, sounds):
        # load images
        for image in images:
            self.images.append(pg.image.load(image))

    def start(self):
        # start fresh
        self.clear_database()
        # add player
        self.initialize_player(self.width / 2, self.height / 2 - 200)
        # add a floor beneath player
        self.initialize_floor(self.width / 2, self.height / 2 + 50)

    def update(self, delta):
        super().process(delta=delta)
        return self.surface

    def initialize_player(self, x, y):
        """ initializes a player entity at x, y
        """
        position = Position(x, y)
        player_rect = pg.Rect(position.x, position.y, 32, 32)
        collider = Collider(
            layer=0b00000001,
            mask=0b11111110,
            rect=player_rect,
            callbacks={
                # floor
                0b00000010: self.player_floor,
            },
            debug=DEBUG
        )
        sprite = Sprite(
            base_image=self.images[0],
            anims=[],
            rect=player_rect,
        )
        physics = Physics(
            gravity=75,
            air_friction=0,
            ground_friction=1,
        )
        player_id = self.create_entity(position)
        self.add_component(player_id, collider)
        self.add_component(player_id, sprite)
        self.add_component(player_id, Input())
        self.add_component(player_id, physics)

    def initialize_floor(self, x, y):
        position = Position(x, y)
        floor_rect = (x, y, 100, 20)
        collider = Collider(
            layer=0b00000010,
            mask=0b00000000,
            rect=floor_rect,
            callbacks={},
            debug=DEBUG
        )
        sprite = Sprite(
            base_image=None,
            anims=[],
            rect=floor_rect
        )
        floor_id = self.create_entity(position, collider)
        self.add_component(floor_id, position)
        self.add_component(floor_id, collider)
        self.add_component(floor_id, sprite)

    @staticmethod
    def player_floor():
        """ collision Reaction between player and floor
        """
        print("Player collided with a floor")