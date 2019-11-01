
from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST  = 3
    WEST  = 4

class Action(Enum):
    SHOOT = 1
    MOVE  = 2
