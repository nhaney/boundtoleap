# **Things to do**:
### Programming:
- Create all components:
  - Collision:
    - collision_mask (8 bits)
    - collider_mask (8 bits)
    - Bounding boxes (list(Rect))
    - Debug flag to show collider
    - Collision handler (callback depending on what type of collision occured)
  - Sprite
    - States - (enum of different states of this sprite)
    - Animations
    - sprite size (should be same as bb from collider)
  - Physics
    - Forces (list of Vector2)
  - Position
    - x
    - y
  - PlayerInput
    - player movement constants
  - Path
    - function x (x = function)
    - function y
    - follow entity (id to follow, speed)
  - GameManager
    - Spawn rates
    - difficulty
    - score
  - 
  
- Create all systems:
  - Player Movement system
    - Physics
    - Input
    - Keeps track of state of player
  - Collision System
    - Collision
    - Loops through and checks collisions and then applies the callback if they happen
  - Path Movement system:
    - Position
    - Path
    - Moves position to next place on path
  
- Create jump and physics system for frog
- Create random seed generation to make game deterministic
- Spin up simple server to track high scores with replay
  - Flask/Go app with celery workers connected to a database
    - Need headless version of game (that can execute quicker than normal)
    - Need networking layer (simple http requests)
  
  