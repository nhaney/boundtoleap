import os

import pygame as pg
import esper

from components.components import Collider, Input, Position, Sprite


class Game(esper.World):
    """
    Handles all gameplay logic
    """
    def __init__(self, images, sounds):
        super.__init__()
        # load resources
        self.load_resources(images, sounds)
    
    def load_resources(self, images, sounds):
        # load images
        self.images = []
        for image in images:
            self.images.append(pg.image.load(image))
        
    def start(self):
        # start fresh
        self.clear_database()
        # add player
        self.initialize_player()

    def update(self, delta):
        super.process(delta=delta)
        

    def initialize_player(world, width, height):
        position = Position(width / 2, height / 2)
        collider = Collider(
            0b1, 
            0b11111110, 
            pg.Rect(position.x, position.y, 32, 32),
            {
                # lily pad
                0b00000010: player_floor
            },
            debug=DEBUG
        )
        Sprite(
            
        )



    def player_floor():
        pass