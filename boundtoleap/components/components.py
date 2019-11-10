class Collider:
    def __init__(self, layer, mask, rect, callbacks, debug=False,):
        self.layer = layer
        self.mask = mask
        self.bb = rect
        self.callbacks = callbacks
        self.debug = debug


class Sprite:
    def __init__(self, base_image, anims, rect):
        self.base_image = base_image
        self.anims = anims
        self.rect = rect


class Position:
    def __init__(self, x, y, facing_right=True):
        self.x = x
        self.y = y
        self.facing_right = facing_right


class Physics:
    def __init__(self, gravity, air_friction, ground_friction):
        self.gravity = gravity
        self.air_friction = air_friction
        self.ground_friction = ground_friction


class Path:
    def __init__(self, x_t, y_t, follow_id, follow_speed):
        self.x_t = x_t
        self.y_t = y_t
        self.follow_id = follow_id
        self.follow_speed = follow_speed


class Input:
    pass
